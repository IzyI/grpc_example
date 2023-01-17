import grpc
from protos import todo_pb2_grpc, approver_pb2_grpc, user_pb2_grpc
from fastapi import Request
from settings import (
    TODO_GRPC_SERVER_ADDR,
    USER_GRPC_SERVER_ADDR,
    APPROVER_GRPC_SERVER_ADDR,
)
from fastapi import Request
from utils import KeyAuthClientInterceptor
from fastapi import Request


async def grpc_todo_client():
    channel = grpc.aio.insecure_channel(TODO_GRPC_SERVER_ADDR)
    client = todo_pb2_grpc.TodoServiceStub(channel)
    return client


async def grpc_approver_client():
    channel = grpc.aio.insecure_channel(APPROVER_GRPC_SERVER_ADDR)
    client = approver_pb2_grpc.ApproverServiceStub(channel)
    return client


async def grpc_user_client(request: Request):
    auth = request.headers.get("rpc-auth")
    print(f"auth {auth}")
    channel = grpc.aio.insecure_channel(
        USER_GRPC_SERVER_ADDR,
        interceptors=[
            KeyAuthClientInterceptor(auth),
        ],
    )
    client = user_pb2_grpc.UserServiceStub(channel)
    return client
