from grpc import aio, StatusCode

from protos import todo_pb2
from protos import todo_pb2_grpc, approver_pb2
from model.todo import Todo
from clients import grpc_approver_client
from grpc_reflection.v1alpha import reflection

from opentelemetry import trace
from opentelemetry.instrumentation.grpc import (
    GrpcAioInstrumentorServer,
    GrpcAioInstrumentorClient,
)
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.proto.grpc import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource


class TodoService(todo_pb2_grpc.TodoServiceServicer):
    # all todos
    async def ListTodos(self, request, context):
        todo = await Todo.select()
        print("ListTodos")
        return todo_pb2.ListTodosResponse(todos=todo)

    # single todo
    async def ReadTodo(self, request, context):
        todo = await Todo.select().where(Todo.id == request.id).first()
        print("ReadTodo")
        return todo_pb2.ReadTodoResponse(todo=todo)

    # create todo
    async def CreateTodo(self, request, context):
        if not (0 <= request.day <= 7):
            context.set_code(StatusCode.INVALID_ARGUMENT)
            context.set_details('0<= day <=7')
            return todo_pb2.CreateTodoResponse()
        todo = await Todo.insert(
            Todo(name=request.name, completed=request.completed, day=request.day)
        )
        print("CreateTodo", )
        return todo_pb2.CreateTodoResponse(todo=todo[0])

    # update todo
    async def UpdateTodo(self, request, context):
        if request.name.lower() == "work":
            await context.abort(StatusCode.INVALID_ARGUMENT, 'No wooo000OOOoork.')
        await Todo.update(
            {Todo.name: request.name, Todo.completed: request.completed}
        ).where(Todo.id == request.id)
        todo = await Todo.select().where(Todo.id == request.id).first()
        print("UpdateTodo")
        return todo_pb2.UpdateTodoResponse(todo=todo)

    # delete todo
    async def DeleteTodo(self, request, context):
        await Todo.delete().where(Todo.id == request.id)
        print("DeleteTodo")
        return todo_pb2.DeleteTodoResponse(success=True)

    async def ReadTodoApprover(self, request, context):
        todo = await Todo.select().where(Todo.id == request.id).first()
        client = await grpc_approver_client()
        print(context.time_remaining())
        # time.sleep(5)
        print(context.time_remaining())
        if todo:
            req = await client.ReadApprover(
                approver_pb2.ReadApproverRequest(day=todo["day"]),
                timeout=context.time_remaining(),
            )
            return todo_pb2.ReadTodoApproverResponse(todo=todo, approver=req.approver)
        else:
            return todo_pb2.ReadTodoApproverResponse(todo=None, approver=None)


async def start(addr, jaeger_addr):
    jaeger_exporter = JaegerExporter(
        collector_endpoint=jaeger_addr,
        insecure=True,
    )
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.set_tracer_provider(
        TracerProvider(resource=Resource.create({SERVICE_NAME: "Todo"}))
    )
    trace.get_tracer_provider().add_span_processor(span_processor)
    grpc_server_instrumentor = GrpcAioInstrumentorServer()
    grpc_server_instrumentor.instrument()
    grpc_client_instrumentor = GrpcAioInstrumentorClient()
    grpc_client_instrumentor.instrument()

    await Todo.create_table(if_not_exists=True)

    server = aio.server()
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port(addr)
    SERVICE_NAMES = (
        todo_pb2.DESCRIPTOR.services_by_name["TodoService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    print(f"TodoService {addr}")

    await server.start()
    await server.wait_for_termination()
