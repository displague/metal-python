# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import metal
from metal.paths.projects_id_ips import post  # noqa: E501
from metal import configuration, schemas, api_client

from .. import ApiTestMixin


class TestProjectsIdIps(ApiTestMixin, unittest.TestCase):
    """
    ProjectsIdIps unit test stubs
        Requesting IP reservations  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201






if __name__ == '__main__':
    unittest.main()
