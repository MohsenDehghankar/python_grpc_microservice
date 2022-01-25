import grpc.aio

from first_service.config.protobuf import SECOND_SERVICE_ADDRESS
from first_service.protos.second_service.v1.second_service_pb2 import *
from first_service.protos.second_service.v1.second_service_pb2_grpc import SecondServiceStub


async def set_status(status_type: StatusType, status):
    async with grpc.aio.insecure_channel(SECOND_SERVICE_ADDRESS) as channel:
        stub = SecondServiceStub(channel=channel)
        response = await stub.SetStatus(SetStatusRequest(type=status_type, new_value=status))
    return response


async def get_status(status_type: StatusType):
    async with grpc.aio.insecure_channel(SECOND_SERVICE_ADDRESS) as channel:
        stub = SecondServiceStub(channel=channel)
        response = await stub.GetStatus(GetStatusRequest(type=status_type))
    return response
