"""
Websocket server base class.
"""
from __future__ import annotations

import asyncio
import json
import urllib.parse
from dataclasses import dataclass
from enum import Enum
from http import HTTPStatus
from typing import Iterable, Mapping, Type

import websockets
from websockets.datastructures import Headers


def parse_path(path: str) -> tuple[str, dict]:
    # Returns the path requested along with a dictionary corresponding to GET parameters
    # Example:
    # await parse_path('ws://beacon:8082/abacus?date=2020-12-18') => ('/abacus', {'date': '2020-12-18'})
    parse_result = urllib.parse.urlparse(path)
    requested_path = parse_result.path
    if len(requested_path) > 1 and requested_path[-1] == '/':
        requested_path = requested_path[:-1]  # Remove trailing '/' if a path is selected
    return requested_path, dict(urllib.parse.parse_qsl(parse_result.query))


@dataclass
class ClientInfo:
    client_id: int
    client_path: Enum
    client_get_arguments: dict
    _number_of_messages: int = 0

    def __str__(self):
        return f'<{self.__class__.__name__} id={self.client_id}, path={self.client_path.value}, get_arguments={self.client_get_arguments}>'


class WebsocketServer:
    def __init__(self, path_class: Type[Enum]):
        self.path_class = path_class

        self.client_dict: dict[websockets.WebSocketServerProtocol, ClientInfo] = {}
        self.websocket_server = None
        self.__new_client_id = -1

    def print(self, message: str, associated_websocket_client: websockets.WebSocketServerProtocol = None):
        if associated_websocket_client is None:
            print(f'{self.__class__.__name__}: {message}')
        else:
            print(f'Client {self.client_dict[associated_websocket_client]}: {message}')

    async def on_connect(self, websocket: websockets.WebSocketServerProtocol, path: str):
        await self.register_client(websocket, path)

    async def on_disconnect(self, websocket: websockets.WebSocketServerProtocol):
        await self.unregister_client(websocket)

    async def _process_request(self, path: str, request_headers: Headers) -> tuple[int | HTTPStatus, Headers | Mapping[
        str, str] | Iterable[tuple[str, str]], bytes] | None:
        path, args = parse_path(path)

        try:
            http_path = self.path_class(path)
        except ValueError:
            return HTTPStatus.BAD_REQUEST, {}, f'Invalid {path=}. Options: {" , ".join([x.value for x in self.path_class])}'.encode()

        return await self.process_request(http_path, args, request_headers)

    async def process_request(self, path: Enum, get_args: dict, request_headers: Headers):
        pass

    async def broadcast_message(self, message: str, path: Enum | None = None):
        if path is None:
            send_coroutines = [client.send(message) for client in self.client_dict]
        else:
            send_coroutines = [client.send(message) for client, client_info in self.client_dict.items() if
                               client_info.client_path is path]

        if len(send_coroutines):
            await asyncio.gather(*send_coroutines,
                                 return_exceptions=True)  # Set return_exceptions=True to ignore any errors that come from send()

    async def register_client(self, websocket: websockets.WebSocketServerProtocol, path: str):
        request_path, request_get_params = parse_path(path)
        self.client_dict[websocket] = ClientInfo(
            client_id=self._new_client_id,
            client_path=self.path_class(request_path),
            client_get_arguments=request_get_params,
        )
        self.print('Connected', websocket)

    async def unregister_client(self, websocket: websockets.WebSocketServerProtocol):
        self.print('Disconnected', websocket)
        del self.client_dict[websocket]

    @property
    def _new_client_id(self):
        self.__new_client_id += 1
        return self.__new_client_id

    async def handler(self, websocket: websockets.WebSocketServerProtocol, path: str):
        await self.on_connect(websocket, path)

        try:
            await self.client_message_handler(websocket, path)
        except websockets.ConnectionClosedError as e:
            self.print(f'Connection closed unexpectedly with code {e.code}: {e.reason}', websocket)
        except Exception as e:
            self.print(f'Unexpected error: {e}', websocket)
        finally:
            await self.on_disconnect(websocket)

    async def client_message_handler(self, websocket: websockets.WebSocketServerProtocol, path: str):
        async for message in websocket:
            response = await self.handle_message(websocket, message)
            if response is not None:
                if isinstance(response, dict):
                    response = json.dumps(response)
                await websocket.send(response)

    async def handle_message(self, websocket: websockets.WebSocketServerProtocol, message: str) -> str | dict | None:
        pass

    def start(self, host: str = '0.0.0.0', port: int = 9000):
        websocket_largs = [self.handler, host, port]
        websocket_kwargs = {
            'process_request': self._process_request,
        }
        self.websocket_server = websockets.serve(*websocket_largs, **websocket_kwargs)
        print(f'Starting server at {host}:{port}')
        asyncio.get_event_loop().run_until_complete(self.websocket_server)
        asyncio.get_event_loop().run_forever()