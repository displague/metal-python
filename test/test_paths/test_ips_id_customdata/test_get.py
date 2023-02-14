# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import metal
from metal.paths.ips_id_customdata import get  # noqa: E501
from metal import configuration, schemas, api_client

from .. import ApiTestMixin


class TestIpsIdCustomdata(ApiTestMixin, unittest.TestCase):
    """
    IpsIdCustomdata unit test stubs
        Retrieve the custom metadata of an IP Reservation or IP Assignment  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
