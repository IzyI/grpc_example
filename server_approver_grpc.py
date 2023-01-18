from grpc_services import approver
import asyncio
from settings import APPROVER_GRPC_SERVER_ADDR, JAEGER_SERVER_ADDR

if __name__ == "__main__":
    print("start Approver grpc server")
    asyncio.run(approver.start(APPROVER_GRPC_SERVER_ADDR, JAEGER_SERVER_ADDR))
