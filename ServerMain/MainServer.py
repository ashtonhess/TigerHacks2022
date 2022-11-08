"""
Main Server.
"""
from __future__ import annotations

from WebsocketServerBase import WebsocketServer
import asyncio
import json
from enum import Enum
import websockets


class HTTPPath(Enum):
    DATA = '/mainserver'
    SUBSCRIBE = '/subscribe'


class MessageType(Enum):
    pass


class UsefulData:
    def __init__(self):
        self.exchanges = ['coinbase', 'coinbasepro', 'binance', 'binanceus', 'gemini', 'kraken']

class DataMsg:
    def __init__(self, aws_location, current_time, exchange_avg_latency):
        self.aws_location = aws_location
        self.current_time = current_time
        self.exchange_avg_latency = exchange_avg_latency

class DataToSend:
    def __init__(self, aws_location, current_time, exchange_avg_latency):
        self.aws_location = aws_location
        self.current_time = current_time
        self.coinbase = exchange_avg_latency[0]
        self.coinbasepro = exchange_avg_latency[1]
        self.binance = exchange_avg_latency[2]
        self.binanceus = exchange_avg_latency[3]
        self.gemini = exchange_avg_latency[4]
        self.kraken = exchange_avg_latency[5]

class ExchangeData:
    def __init__(self, exchange):
        self.exchange = exchange
        self.data_points = []

class AllData:
    def __init__(self):
        self.coinbase = ExchangeData('coinbase')
        self.coinbasepro = ExchangeData('coinbasepro')
        self.binance = ExchangeData('binance')
        self.binanceus = ExchangeData('binanceus')
        self.gemini = ExchangeData('gemini')
        self.kraken = ExchangeData('kraken')

class ServerMain(WebsocketServer):
    def __init__(self):
        super().__init__(HTTPPath)
        self.client_map: dict[str, set[websockets.WebSocketServerProtocol]] = {}
        self.client_map['all_clients'] = set()
        self.client_map['web_clients'] = set()
        self.client_map['aws_servers'] = set()
        self.client_groups = []
        self.data_buffer: dict[str, list] = {}
        self.allData = AllData()
        self.data_buffer['all'] = []
        self.client_groups.append('all')

    async def on_connect(self, websocket: websockets.WebSocketServerProtocol, path: str):
        if HTTPPath(path) is HTTPPath.SUBSCRIBE:
            await super().on_connect(websocket, path)
            print('A new client has connected.')
            self.client_map['all_clients'].add(websocket)
            self.client_map['web_clients'].add(websocket)
            # self.data_buffer['all'] = []
            # Sending initial message back to connected client.
            # if HTTPPath(path) is HTTPPath.DATA:
            #     data = {
            #
            #     }
            #     await websocket.send(json.dumps(data))
            # if HTTPPath(path) is HTTPPath.SUBSCRIBE:
            #     data = {
            #         'data':'welcome'
            #     }
                # await websocket.send(json.dumps(data))
        elif HTTPPath(path) is HTTPPath.DATA:
            print("A new AWS server has connected.")
            self.client_map['all_clients'].add(websocket)
            self.client_map['aws_servers'].add(websocket)
        else:
            print("Unknown client has connected.")

    async def on_disconnect(self, websocket: websockets.WebSocketServerProtocol):
        if websocket in self.client_map['web_clients']:
            self.client_map['web_clients'].remove(websocket)
            print('A web client was removed.')
        if websocket in self.client_map['aws_servers']:
            self.client_map['aws_servers'].remove(websocket)
            print('An aws server was removed.')
        self.client_map['all_clients'].remove(websocket)

        # pass

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
        # self.client_map['all'] = set()
        # self.client_map['all'].add(websocket)
        # self.client_groups.append('all')
        message_data = json.loads(message)
        # print(message_data)
        aws_location = message_data['aws_location']
        # print("aws_location: ", aws_location)
        current_time = message_data['current_time']
        # print("current_time: ", current_time)
        exchange_avg_latency = message_data['exchange_avg_latency']
        # print("exchange_avg_latency: ", exchange_avg_latency)
        # print("lat[0]: ", exchange_avg_latency[0])
        usefulObj = UsefulData()
        dataMsgObj = DataMsg(aws_location, current_time, exchange_avg_latency)
        dataToSendObj = DataToSend(aws_location, current_time, exchange_avg_latency)
        json_string = json.dumps(dataToSendObj.__dict__)
        # print(json_string)
        if len(self.client_map['web_clients']) != 0:
            for ws in self.client_map['web_clients']:
                await ws.send(json_string)
        # for x in self.client_map['all']:
        #     send_coroutines = [x.send(json.dumps(dataToSendObj.__dict__)) for x in self.client_map['all']]
        #     await asyncio.gather(*send_coroutines, return_exceptions=True)

        # self.data_buffer['all'].append(json_string)

        # self.data_buffer




        # print()
        # print("EHEIHDSOIINOSDGNOISDFN")
        # print(dataToSendObj.aws_location)
        # print(dataToSendObj.current_time)
        # print(dataToSendObj.coinbase)
        # print(dataToSendObj.kraken)


            # if dataMsgObj.aws_location == i-1:
            #     dataMsgObj.exchange = usefulObj[i-1]

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