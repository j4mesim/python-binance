import time
from pprint import pprint
import yaml
from binance.streams import ThreadedPollingManager, AsyncClient, ThreadedSocketManager
from binance.configtools import load_config
test = False

config = load_config(test)

tpm = ThreadedPollingManager(**config)
tpm.start()
tpm.start_async_polling(print, AsyncClient.get_order_book.__name__, 5, dict(symbol='BTCUSD', limit=100))

# tpm.join()

# tsm = ThreadedSocketManager(**kwargs_prod2)
# tsm.start()
# tsm.start_aggtrade_socket(print, 'BTCUSD')

# tsm.join()
# tsm.join()

# async def start_server():
#     await tpm._start_async_polling(print, AsyncClient.get_account.__name__, 5)


if __name__ == "__main__":
    # pass
    import asyncio
    loop = asyncio.new_event_loop()
    print(f'main loop: {loop} @ {id(loop)}')
    loop.run_forever()
