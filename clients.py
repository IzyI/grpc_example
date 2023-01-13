import grpc
from protos import todo_pb2_grpc
from fastapi import Request
from settings import TODO_GRPC_SERVER_ADDR


async def grpc_todo_client():
    channel = grpc.aio.insecure_channel(TODO_GRPC_SERVER_ADDR)
    client = todo_pb2_grpc.TodoServiceStub(channel)
    return client
