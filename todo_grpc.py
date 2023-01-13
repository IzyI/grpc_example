import logging
from services.todo import run
import asyncio
from settings import TODO_GRPC_SERVER_ADDR


if __name__ == "__main__":
    asyncio.run(run(TODO_GRPC_SERVER_ADDR))