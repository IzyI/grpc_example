from grpc import aio
from protos import user_pb2
from protos import user_pb2_grpc
from grpc_reflection.v1alpha import reflection
from utils import AuthInterceptor

from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc

from opentelemetry import trace
from opentelemetry.instrumentation.grpc import GrpcAioInstrumentorServer
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.proto.grpc import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource


class UserService(user_pb2_grpc.UserServiceServicer):
    async def ReadUser(self, request, context):
        print("ReadUser")
        return user_pb2.ReadUserResponse(user={"id": 1, "name": "KAPER_IT"})

    def Check(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.SERVING
        )

    def Watch(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.UNIMPLEMENTED
        )


async def start(
        addr,
        token,
        jaeger_addr
):
    jaeger_exporter = JaegerExporter(
        collector_endpoint=jaeger_addr, insecure=True
    )
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.set_tracer_provider(
        TracerProvider(resource=Resource.create({SERVICE_NAME: "User"}))
    )
    trace.get_tracer_provider().add_span_processor(span_processor)
    grpc_server_instrumentor = GrpcAioInstrumentorServer()
    grpc_server_instrumentor.instrument()

    server = aio.server(
        interceptors=[
            AuthInterceptor(token),
        ]
    )
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    SERVICE_NAMES = (
        user_pb2.DESCRIPTOR.services_by_name["UserService"].full_name,
        reflection.SERVICE_NAME,
    )
    service = UserService()
    health_pb2_grpc.add_HealthServicer_to_server(service, server)
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port(addr)
    print(f"UserService {addr}")
    await server.start()
    await server.wait_for_termination()
