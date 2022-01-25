import grpc

from second_service.config.protobuf import FIRST_SERVICE_ADDRESS
from second_service.protos.first_service.v1.first_service_pb2 import GetRandomNumberRequest
from second_service.protos.first_service.v1.first_service_pb2_grpc import FirstServiceStub


async def get_random_number():
    async with grpc.aio.insecure_channel(FIRST_SERVICE_ADDRESS) as channel:
        stub = FirstServiceStub(channel=channel)
        response = await stub.GetRandomNumber(GetRandomNumberRequest())
    return response
