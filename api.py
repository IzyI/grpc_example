import typing as t
from fastapi import Depends, FastAPI, status, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from fastapi.responses import JSONResponse
from clients import grpc_todo_client, grpc_user_client
from protos import todo_pb2
from google.protobuf.json_format import MessageToDict
from grpc.aio._call import AioRpcError
from google.protobuf import empty_pb2

api_key_header = APIKeyHeader(name="rpc-auth")

app = FastAPI()


@app.get("/")
async def ping():
    return {"ping": True}


@app.get("/todo")
async def list_todos(client: t.Any = Depends(grpc_todo_client)) -> JSONResponse:
    try:
        todos = await client.ListTodos(todo_pb2.ListTodosRequest())
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(todos))


@app.get("/todo/{id:int}")
async def single_todo(
    id: int,
    client: t.Any = Depends(grpc_todo_client),
) -> JSONResponse:
    try:
        todo = await client.ReadTodo(todo_pb2.ReadTodoRequest(id=id))
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(todo))


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(
    name: str,
    completed: bool,
    day: int,
    client: t.Any = Depends(grpc_todo_client),
) -> JSONResponse:
    try:
        todo = await client.CreateTodo(
            todo_pb2.CreateTodoRequest(name=name, completed=completed, day=day),
            timeout=5,
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(todo))


@app.patch("/todo/{id:int}")
async def update_todo(
    id: int,
    name: str,
    completed: bool,
    client: t.Any = Depends(grpc_todo_client),
) -> JSONResponse:
    try:
        todo = await client.UpdateTodo(
            todo_pb2.UpdateTodoRequest(
                id=id,
                name=name,
                completed=completed,
            )
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(todo))


@app.delete("/todo/{id:int}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(id: int, client: t.Any = Depends(grpc_todo_client)) -> None:
    try:
        await client.DeleteTodo(todo_pb2.DeleteTodoRequest(id=id))
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())


@app.get("/user")
async def get_user(
    api_key_header: str = Security(api_key_header),
    client: t.Any = Depends(grpc_user_client),
) -> JSONResponse:
    print(f"api_key_header {api_key_header}")
    try:
        u = await client.ReadUser(empty_pb2.Empty(), timeout=10)
    except AioRpcError as e:
        import traceback

        traceback.print_exc()
        raise HTTPException(status_code=400, detail=e.details())
    return JSONResponse(MessageToDict(u))


@app.get("/todo/{id:int}/approver")
async def single_approve_todo(
    id: int,
    client: t.Any = Depends(grpc_todo_client),
) -> JSONResponse:
    print("single_approver_todo")
    try:
        todo = await client.ReadTodoApprover(todo_pb2.ReadTodoRequest(id=id), timeout=3)
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())
    print("dddd")
    return JSONResponse(MessageToDict(todo))
