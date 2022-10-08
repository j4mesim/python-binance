import os.path

import yaml


def load_config(test=True):
    filename = f'python-binance.conf.{"test" if test else "prod"}'
    filepath = os.path.join("..", filename)
    return yaml.load(open(filepath), Loader=yaml.FullLoader)