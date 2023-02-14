# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import metal
from metal.paths.connections_connection_id import delete  # noqa: E501
from metal import configuration, schemas, api_client

from .. import ApiTestMixin


class TestConnectionsConnectionId(ApiTestMixin, unittest.TestCase):
    """
    ConnectionsConnectionId unit test stubs
        Delete interconnection  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 202




if __name__ == '__main__':
    unittest.main()
