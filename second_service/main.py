import asyncio

from second_service.handlers.servicer import Server
from second_service.service_dataaccess.grpc_client_task import client_task


async def main():
    asyncio.ensure_future(client_task())  # calling first_service for test
    await Server.run()


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    event_loop.run_forever()
