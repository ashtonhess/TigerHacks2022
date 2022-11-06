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

class ExchTime:
    def __init__(self, exchange, latency):
        self.exchange = exchange
        self.latency = latency


class ExchangeCCTX:
    def __init__(self, exchange, ccxtObj):
        self.exchange = exchange
        self.ccxtObj = ccxtObj

        # print(exch.exchangeName + ExchTime)



allTimes = []
exchangeCCXTObjs = []

coinbaseObj = ExchangeCCTX('coinbase', ccxt.coinbase())
exchangeCCXTObjs.append(coinbaseObj)
coinbaseproObj = ExchangeCCTX('coinbasepro', ccxt.coinbasepro())
exchangeCCXTObjs.append(coinbaseproObj)
binanceObj = ExchangeCCTX('binance', ccxt.binance())
exchangeCCXTObjs.append(binanceObj)
binanceusObj = ExchangeCCTX('binanceus', ccxt.binanceus())
exchangeCCXTObjs.append(binanceusObj)
geminiObj = ExchangeCCTX('gemini', ccxt.gemini())
exchangeCCXTObjs.append(geminiObj)
krakenObj = ExchangeCCTX('kraken', ccxt.kraken())
exchangeCCXTObjs.append(krakenObj)

# exchangeCCXTObjs = [ccxt.coinbase(),ccxt.coinbasepro(),ccxt.binance(),ccxt.binanceus(),ccxt.gemini(),ccxt.kraken()]
# times = []
# testcounter = 0
async def run():
    async with websockets.connect("ws://cuppong.hessdevelopments.com:11328/mainserver") as websocket:
        while True:
            times = []
            testcounter = 0
            counter = 0
            print(testcounter)
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
                object = ExchTime(exch.exchange, elapsed_time)
                object.current_time = time.time()
                object.location = aws_location
                times.append(object)
                print("Exchange: "+object.exchange)
                print("Latency: "+str(object.latency))
                print("current_time: "+str(object.current_time))
                print(response)
                print()
                print(times)
                print()
                testcounter += 1

            #testJSONstr = json.dumps(times[0].__dict__)
            #print("HEREHERE")
            #print(testJSONstr)
            json_string = json.dumps([ob.__dict__ for ob in times])
            print("HERE HERE HERE")
            print(json_string)
            await websocket.send(json_string)
                # jsonstr1 = json.dumps(s1.__dict__)
                # for obj in times:

    # Send times array to main server
    # # If needed, add times to alltimes (memory issues...)
    # times = []
    # coinbaseTimeToJSON = {
    #     "Exchange": "coinbase",
    #     "Latency": "CEO",
    #     "company_name": "Bell System",
    # }

asyncio.run(run())
