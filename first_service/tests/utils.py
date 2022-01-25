import asyncio


def async_test(func):
    def function_wrapper(*args, **kwargs):
        async def run():
            await func(*args, **kwargs)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(run())

    return function_wrapper
