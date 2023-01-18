from grpc_services import user
import asyncio
from settings import USER_GRPC_SERVER_ADDR, TOKEN_AUTH, JAEGER_SERVER_ADDR



if __name__ == "__main__":
    print("start User grpc server")
    asyncio.run(user.start(USER_GRPC_SERVER_ADDR, TOKEN_AUTH,JAEGER_SERVER_ADDR))
