from grpc_services import user
import asyncio
from settings import USER_GRPC_SERVER_ADDR, TOKEN_AUTH, JAEGER_SERVER_ADDR

from opentelemetry import trace
from opentelemetry.instrumentation.grpc import GrpcAioInstrumentorServer
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.proto.grpc import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

if __name__ == "__main__":
    jaeger_exporter = JaegerExporter(
        collector_endpoint=JAEGER_SERVER_ADDR, insecure=True
    )
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.set_tracer_provider(
        TracerProvider(resource=Resource.create({SERVICE_NAME: "User"}))
    )
    trace.get_tracer_provider().add_span_processor(span_processor)
    grpc_server_instrumentor = GrpcAioInstrumentorServer()
    print("start User grpc server")
    asyncio.run(user.start(USER_GRPC_SERVER_ADDR, TOKEN_AUTH))
