import asyncio
import random

from first_service.protos.second_service.v1.second_service_pb2 import STATUS_TYPE_ONE, STATUS_TYPE_TWO
from first_service.service_dataaccess.second_service import set_status, get_status


async def client_task():
    """
    This task is for calling another service, for test.
    """

    await asyncio.sleep(5)
    while True:
        status_type = STATUS_TYPE_ONE if random.random() > 0.5 else STATUS_TYPE_TWO
        if random.random() > 0.5:
            status = f"mohsen-{str(random.random())}"
            result = await set_status(status_type=status_type, status=status)
            print(f"response --> {result.message}")
        else:
            result = await get_status(status_type=status_type)
            print(f"response --> {result.status}")
        await asyncio.sleep(4)
