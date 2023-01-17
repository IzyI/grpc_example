from grpc import aio

from protos import approver_pb2
from protos import approver_pb2_grpc

from google.protobuf import wrappers_pb2 as _wrappers_pb2

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


async def start(addr):
    server = aio.server()
    approver_pb2_grpc.add_ApproverServiceServicer_to_server(ApproverService(), server)
    server.add_insecure_port(addr)
    print(f"ApproverService {addr}")
    await server.start()
    await server.wait_for_termination()
