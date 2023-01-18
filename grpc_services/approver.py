from grpc import aio

from protos import approver_pb2
from protos import approver_pb2_grpc

from google.protobuf import wrappers_pb2 as _wrappers_pb2

from opentelemetry import trace
from opentelemetry.instrumentation.grpc import GrpcAioInstrumentorServer
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.proto.grpc import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

WORK_DAY = [1, 2, 5, 7]


class ApproverService(approver_pb2_grpc.ApproverServiceServicer):
    # all todos
    async def ReadApprover(self, request, context):
        print("ReadApprover")
        print(request, context.time_remaining())
        # time.sleep(5)
        print(request, context.time_remaining())
        if request.day in WORK_DAY:
            status = True
        else:
            status = False
        return approver_pb2.ReadApproverResponse(
            approver={"status": _wrappers_pb2.BoolValue(value=status)}
        )


async def start(addr, jaeger_addr):
    jaeger_exporter = JaegerExporter(
        collector_endpoint=jaeger_addr, insecure=True
    )
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.set_tracer_provider(
        TracerProvider(resource=Resource.create({SERVICE_NAME: "Approver"}))
    )
    trace.get_tracer_provider().add_span_processor(span_processor)
    grpc_server_instrumentor = GrpcAioInstrumentorServer()
    grpc_server_instrumentor.instrument()

    server = aio.server()
    approver_pb2_grpc.add_ApproverServiceServicer_to_server(ApproverService(), server)
    server.add_insecure_port(addr)
    print(f"ApproverService {addr}")
    await server.start()
    await server.wait_for_termination()
