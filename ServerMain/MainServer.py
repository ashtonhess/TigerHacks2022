"""
Flippy Switch Game Server.
"""
from __future__ import annotations

from WebsocketServerBase import WebsocketServer
import asyncio
import json
from enum import Enum
import websockets


class HTTPPath(Enum):
    DATA = '/mainserver'


class MessageType(Enum):
    pass


class ServerMain(WebsocketServer):
    def __init__(self):
        super().__init__(HTTPPath)
        self.client_map: dict[str, set[websockets.WebSocketServerProtocol]] = {}
        self.client_groups = []
        self.data_buffer: dict[str, list] = {}

    async def on_connect(self, websocket: websockets.WebSocketServerProtocol, path: str):
        await super().on_connect(websocket, path)
        print('NEW CLIENT CONNECTED')
        # Sending initial message back to connected client.
        if HTTPPath(path) is HTTPPath.DATA:
            data = {

            }
            await websocket.send(json.dumps(data))

    async def on_disconnect(self, websocket: websockets.WebSocketServerProtocol):
        pass

    async def _broadcast_task(self):
        # while True:
        if len(self.client_groups) > 0:
            for client_group in self.client_groups:
                if self.data_buffer[client_group]:
                    data = {
                        'data': self.data_buffer[client_group]
                    }
                    send_coroutines = [x.send(json.dumps(data)) for x in self.client_map[client_group]]
                    await asyncio.gather(*send_coroutines, return_exceptions=True)

    async def handle_message(self, websocket: websockets.WebSocketServerProtocol, message: str) -> str | dict | None:
        # print(message)
        message_data = json.loads(message)
        print(message_data)
        #print(f'NEW MSG:\ttype: {message_data["type"]}\tside:{message_data["side"]}')
        #message_type = message_data['type']
        #if message_type == 'subscribe':
        #    print('sub msg')
        return None


    def start(self, host: str = '0.0.0.0', port: int = 9000):
        asyncio.get_event_loop().create_task(self._broadcast_task())
        super().start(host, port)


if __name__ == '__main__':

    ServerMain().start(port=11328)