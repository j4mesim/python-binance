from queue import PriorityQueue
from typing import Dict
from typing import Optional

from binance.threaded_stream import ThreadedApiManager
from binance.client import AsyncClient, AsyncClientPathBuilder
from binance.enums import ListerState
from binance.streams import BinancePollerManager, BinanceSocketManager

test = True

if test:
    kwargs = open('python-binance.conf.prod').read()
else:
    kwargs = open('python-binance.conf.test').read()

#
# class ListenerManager(ThreadedApiManager):
#
#     def __init__(
#         self, api_key: Optional[str] = None, api_secret: Optional[str] = None,
#         requests_params: Optional[Dict[str, str]] = None, tld: str = 'com',
#         testnet: bool = False
#     ):
#         super(ListenerManager, self).__init__(api_key, api_secret, requests_params, tld, testnet)
#         self._bm = Optional[BinancePollerManager] = None
#         self._listeners_state: Dict[str, bool] = {}
#
#     async def listen(self, key, callback: Optional[callable] = None):
#         # get most recent listener
#         while self._listeners_state[key] in (ListerState.RUN, ListerState.SWITCH):
#             q = self._listeners[key]
#             listener = await q.get()
#             async with listener as l:
#                 while self._listeners_state[key] == ListerState.RUN:
#                     msg = await l.recv()
#                     if callback and msg:
#                         callback(msg)
#             q.task_done()
#
#


async def main(**kwargs):
    client = AsyncClient(**kwargs)
    path_builder = AsyncClientPathBuilder(**kwargs)
    # bpm = BinancePollerManager(client, path_builder)
    # bsm = BinanceSocketManager(client)
    man = ListenerManager()
    tasks = [
        # listen(await bpm.method_poller(client.get_products, 3)),
        # listen(await bpm._get_listener(client.get_recent_trades.__name__, 3, dict(symbol='XNOUSD'))),
        # listen(bsm.user_socket()),
        listen(bsm.symbol_miniticker_socket('BCHUSD'), print)
    ]

    await asyncio.gather(*tasks)

if __name__ == "__main__":

    import asyncio
    # client = Client(**kwargs_prod2)
    # print(client.get_account())

    loop = asyncio.new_event_loop()
    loop.run_until_complete(main(**kwargs))
