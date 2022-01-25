from unittest import TestCase
from unittest.mock import patch

import grpc

from first_service.handlers.servicer import FirstService
from first_service.protos.first_service.v1.first_service_pb2 import GetRandomNumberRequest
from first_service.protos.second_service.v1.second_service_pb2 import STATUS_TYPE_ONE
from first_service.protos.second_service.v1.second_service_pb2_grpc import add_SecondServiceServicer_to_server
from first_service.service_dataaccess.second_service import get_status, set_status
from first_service.tests.mocks import MockedSecondService, SECOND_SERVICE_ADDRESS
from first_service.tests.utils import async_test


class FirstServiceTestCase(TestCase):

    @async_test
    async def setUp(self) -> None:
        self.first_service = FirstService()

        # running second service
        self.second_server = grpc.aio.server()
        add_SecondServiceServicer_to_server(MockedSecondService(), self.second_server)
        listen_address = SECOND_SERVICE_ADDRESS
        self.second_server.add_insecure_port(listen_address)
        await self.second_server.start()

    @async_test
    async def tearDown(self) -> None:
        await self.second_server.stop(1)

    @async_test
    async def test__get_random_number__handler(self):
        request = GetRandomNumberRequest()
        output = await self.first_service.GetRandomNumber(request, None)
        self.assertIsNotNone(output)
        self.assertGreater(output.random, 999)

    @patch('first_service.service_dataaccess.second_service.SECOND_SERVICE_ADDRESS',
           SECOND_SERVICE_ADDRESS)
    @async_test
    async def test__second_service__data_access(self):
        get_response = await get_status(status_type=STATUS_TYPE_ONE)
        self.assertIsNotNone(get_response)
        self.assertEqual("status", get_response.status)
        set_response = await set_status(status_type=STATUS_TYPE_ONE, status="status")
        self.assertEqual("OK", set_response.message)
