import grpc
import abc
from typing import Callable, Awaitable, Any

from grpc_interceptor.server import _get_factory_and_method


class ServerInterceptorAsyncBase(grpc.aio.ServerInterceptor, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    async def intercept(
            self,
            method: Callable,
            request: Any,
            context: grpc.aio.ServicerContext,
            method_name: str,
    ) -> Any:
        return await method(request, context)  # pragma: no cover

    async def intercept_service(self,
                                continuation: Callable[[grpc.HandlerCallDetails], Awaitable[grpc.RpcMethodHandler]],
                                handler_call_details):
        next_handler = await continuation(handler_call_details)
        handler_factory, next_handler_method = _get_factory_and_method(next_handler)

        async def invoke_intercept_method(request, context):
            method_name = handler_call_details.method
            return await self.intercept(next_handler_method, request, context, method_name, )

        return handler_factory(
            invoke_intercept_method,
            request_deserializer=next_handler.request_deserializer,
            response_serializer=next_handler.response_serializer,
        )
