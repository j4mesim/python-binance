from contextlib import AbstractAsyncContextManager
from abc import abstractmethod


class AbstractListener(AbstractAsyncContextManager):

    async def __aenter__(self):
        return self

    @abstractmethod
    async def recv(self):
        ...
