from second_service.protos.second_service.v1.second_service_pb2 import SetStatusRequest, SetStatusReply, \
    GetStatusRequest, GetStatusReply, \
    UNKNOWN_STATUS

mem_status = ["mohsen-1", "mohsen-2"]


async def set_status(request: SetStatusRequest) -> SetStatusReply:
    global mem_status

    if request.type == UNKNOWN_STATUS:
        return SetStatusReply(message="Error; type unknown")

    print(f"set_status({request.type}, {request.new_value}) --> OK", flush=True)

    mem_status[request.type - 1] = request.new_value
    return SetStatusReply(message="OK")


async def get_status(request: GetStatusRequest) -> GetStatusReply:
    if request.type == UNKNOWN_STATUS:
        return SetStatusReply(message="Error; type unknown")

    status = mem_status[request.type - 1]

    print(f"get_status({request.type}) --> {status}", flush=True)

    return GetStatusReply(status=status)
