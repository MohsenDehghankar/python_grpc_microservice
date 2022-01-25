import grpc

import first_service.config.protobuf as protobuf_config
from first_service.handlers.random_number_handler import get_random_number
from first_service.interceptors.exception_interceptor import ExceptionInterceptor
from first_service.protos.first_service.v1.first_service_pb2_grpc import FirstServiceServicer, \
    add_FirstServiceServicer_to_server
from first_service.service_dataaccess.second_service import *


class FirstService(FirstServiceServicer):
    async def GetRandomNumber(self, request, context):
        return await get_random_number(request)


class Server:
    @staticmethod
    async def run() -> None:
        server = grpc.aio.server(interceptors=[ExceptionInterceptor()])
        add_FirstServiceServicer_to_server(FirstService(), server)
        listen_address = f'{protobuf_config.LISTEN_ADDRESS}:{protobuf_config.LISTEN_PORT}'
        server.add_insecure_port(listen_address)
        print(f"Starting server FIRST on {listen_address}", flush=True)
        await server.start()
        await server.wait_for_termination()
