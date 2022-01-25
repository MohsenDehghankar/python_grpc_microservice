import asyncio

from second_service.service_dataaccess.first_service import get_random_number


async def client_task():
    """
    This task is for calling another service, for test.
    """

    await asyncio.sleep(5)
    while True:
        random_number = await get_random_number()
        print(f"response --> {random_number}")
        await asyncio.sleep(4)
