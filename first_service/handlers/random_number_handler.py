import random
from first_service.protos.first_service.v1.first_service_pb2 import GetRandomNumberReply, GetRandomNumberRequest


async def get_random_number(empty: GetRandomNumberRequest) -> GetRandomNumberReply:
    random_number = random.randint(1000, 9999)

    print(f"get_random_number() --> {random_number}", flush=True)

    return GetRandomNumberReply(random=random_number)
