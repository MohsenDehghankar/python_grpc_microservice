import grpc

import second_service.config.protobuf as protobuf_config
from second_service.interceptors.exception_interceptor import ExceptionInterceptor
from second_service.protos.second_service.v1.second_service_pb2_grpc import SecondServiceServicer, \
    add_SecondServiceServicer_to_server
from second_service.handlers.status_handler import set_status, get_status


class SecondService(SecondServiceServicer):
    async def SetStatus(self, request, context):
        return await set_status(request)

    async def GetStatus(self, request, context):
        return await get_status(request)


class Server:

    @staticmethod
    async def run() -> None:
        server = grpc.aio.server(interceptors=[ExceptionInterceptor()])
        add_SecondServiceServicer_to_server(SecondService(), server)
        listen_address = f'{protobuf_config.LISTEN_ADDRESS}:{protobuf_config.LISTEN_PORT}'
        server.add_insecure_port(listen_address)
        print(f"Starting SECOND on {listen_address}", flush=True)
        await server.start()
        await server.wait_for_termination()
