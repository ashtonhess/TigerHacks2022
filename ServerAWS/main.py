import json
import time
import ccxt
import asyncio
import websockets

# Example code
# binance = ccxt.binance()
# coinbase = ccxt.binance()
# start_time = time.perf_counter()
# btc_ticker = binance.fetch_ticker('BTC/USDT')
# elapsed_time = time.perf_counter() - start_time
# print()
# print(btc_ticker)
# print()
# print(elapsed_time)
aws_location = 'us-east-1-NVirginia'

class MainServerMessage:
    def __init__(self, current_time, aws_location):
        self.current_time = current_time
        self.exchange_avg_latency = []
        self.aws_location = aws_location

class ExchAvgData:
    def __init__(self, exchange):
        self.exchange = exchange
        self.sum = 0


class ExchTime:
    def __init__(self, exchange, latency):
        self.exchange = exchange
        self.latency = latency


class ExchangeCCTX:
    def __init__(self, exchange, ccxtObj):
        self.exchange = exchange
        self.ccxtObj = ccxtObj


exchanges = ['coinbase', 'coinbasepro', 'binance', 'binanceus', 'gemini', 'kraken']

# Array to hold CCXT objects for each exchange.
exchangeCCXTObjs = []

coinbaseObj = ExchangeCCTX(exchanges[0], ccxt.coinbase())
exchangeCCXTObjs.append(coinbaseObj)
coinbaseproObj = ExchangeCCTX(exchanges[1], ccxt.coinbasepro())
exchangeCCXTObjs.append(coinbaseproObj)
binanceObj = ExchangeCCTX(exchanges[2], ccxt.binance())
exchangeCCXTObjs.append(binanceObj)
binanceusObj = ExchangeCCTX(exchanges[3], ccxt.binanceus())
exchangeCCXTObjs.append(binanceusObj)
geminiObj = ExchangeCCTX(exchanges[4], ccxt.gemini())
exchangeCCXTObjs.append(geminiObj)
krakenObj = ExchangeCCTX(exchanges[5], ccxt.kraken())
exchangeCCXTObjs.append(krakenObj)


async def run():
    # async with websockets.connect("ws://cuppong.hessdevelopments.com:11328/mainserver") as websocket:
    # async with websockets.connect("ws://ec2-18-216-52-122.us-east-2.compute.amazonaws.com:11328/mainserver") as websocket:
    websocket = await websockets.connect("ws://ec2-18-216-52-122.us-east-2.compute.amazonaws.com:11328/mainserver")
    # try:
    main_counter = 0
    all_times = []
    while True:
        times = []
        counter = 0
        for exch in exchangeCCXTObjs:
            if counter == 0 or counter == 4:
                start_time = time.perf_counter()
                response = exch.ccxtObj.fetch_ticker('BTC/USD')
                end_time = time.perf_counter()
            else:
                start_time = time.perf_counter()
                response = exch.ccxtObj.fetch_ticker('BTC/USDT')
                end_time = time.perf_counter()
            counter += 1
            elapsed_time = end_time - start_time
            obj = ExchTime(exch.exchange, elapsed_time)
            obj.current_time = time.time()
            obj.location = aws_location
            times.append(obj)
            # print("Exchange: " + obj.exchange)
            # print("Latency: " + str(obj.latency))
            # print("current_time: " + str(obj.current_time))
            # print(response)
            # print()
            # print(times)
            # print()
            all_times += times
        # json_string = json.dumps([ob.__dict__ for ob in times])
        # print("HERE HERE HERE")
        # print(json_string)
        main_counter += 1
        if main_counter != 0 and main_counter % 10 == 0:
            print("ITERATION: " + str(main_counter))
            exch_avg_objs = []
            for exch in exchanges:
                obj = ExchAvgData(exch)
                exch_avg_objs.append(obj)
            for exch_time_obj in all_times:
                for i in range(0, 6):
                    # print("i: "+str(i))
                    if exch_time_obj.exchange == exchanges[i]:
                        # print()
                        # print(exch_time_obj.exchange)
                        # print(exchanges[i])
                        # print()
                        exch_avg_objs[i].sum += exch_time_obj.latency
                        # print(exch_avg_objs[i].sum)
                main_server_message_obj = MainServerMessage(time.time(), aws_location)
            i = 0
            for exch in exchanges:
                print("HERE DSLFKJLDSGNSD")
                print(exch_avg_objs[i].sum / 10)
                main_server_message_obj.exchange_avg_latency.append(exch_avg_objs[i].sum / 10)
                print(main_server_message_obj.exchange_avg_latency[i])
                print("HERE DSLFKJLDSGNSD")
                i+=1
            # json_string = json.dumps([obj.__dict__ for obj in main_server_message_obj])
            json_string = json.dumps(main_server_message_obj.__dict__)
            await websocket.send(json_string)
            all_times = []
        # except websockets.ConnectionClosedError:
        #     print("EXCEPTION")
        #     # websocket = websockets.connect("ws://cuppong.hessdevelopments.com:11328/mainserver")
        #     asyncio.run(run())

    # class MainServerMessage:
    #     def __init__(self, current_time):
    #         self.current_time = current_time
    #         self.exchange_avg_latency = []


    # Send times array to main server
    # # If needed, add times to alltimes (memory issues...)

while True:
    try:
        asyncio.run(run())
    except websockets.ConnectionClosedError:
        print("EXCEPTION")
        # websocket = websockets.connect("ws://cuppong.hessdevelopments.com:11328/mainserver")
        asyncio.run(run())
