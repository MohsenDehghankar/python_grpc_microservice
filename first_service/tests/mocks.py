from first_service.protos.second_service.v1.second_service_pb2 import GetStatusReply, SetStatusReply
from first_service.protos.second_service.v1.second_service_pb2_grpc import SecondServiceServicer

SECOND_SERVICE_ADDRESS = "localhost:50051"


class MockedSecondService(SecondServiceServicer):
    async def SetStatus(self, request, context):
        return SetStatusReply(message="OK")

    async def GetStatus(self, request, context):
        return GetStatusReply(status="status")
