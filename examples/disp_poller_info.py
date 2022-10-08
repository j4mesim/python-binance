from binance.streams import AsyncClient, ThreadedPollingManager,  ThreadedSocketManager
from binance.configtools import load_config


kwargs = load_config(test=False)
# tpm = ThreadedPollingManager(**common_kwargs)
# twm = ThreadedWebsocketManager(**kwargs_testnet)
# twm = ThreadedWebsocketManager(**kwargs_test)
twm = ThreadedSocketManager()

import sys


def handlemsg(*args):
    print()
    for arg in args:
        sys.stdout.write(args)


# twm.start()
twm.start_ticker_socket(handlemsg)
twm.run()

import asyncio




