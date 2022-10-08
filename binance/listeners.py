import asyncio
from contextlib import AbstractAsyncContextManager
from abc import abstractmethod
from typing import Any, Optional


class ApiListener:

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    async def recv(self) -> Optional[Any]:
        ...
