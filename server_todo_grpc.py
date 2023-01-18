from grpc_services import todo
import asyncio
from settings import TODO_GRPC_SERVER_ADDR, JAEGER_SERVER_ADDR




if __name__ == "__main__":
    print("start Todo grpc server")
    asyncio.run(todo.start(TODO_GRPC_SERVER_ADDR,JAEGER_SERVER_ADDR))
