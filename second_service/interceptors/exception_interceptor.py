from typing import Callable, Any

import grpc

from second_service.interceptors.base_server_interceptor import ServerInterceptorAsyncBase


class ExceptionInterceptor(ServerInterceptorAsyncBase):
    async def intercept(
            self,
            method: Callable,
            request: Any,
            context: grpc.aio.ServicerContext,
            method_name: str,
    ) -> Any:
        try:
            return await method(request, context)
        except Exception as e:
            # log exception, send metric to prometheus, etc
            raise
