# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import metal
from metal.paths.projects_id_bgp_sessions import get  # noqa: E501
from metal import configuration, schemas, api_client

from .. import ApiTestMixin


class TestProjectsIdBgpSessions(ApiTestMixin, unittest.TestCase):
    """
    ProjectsIdBgpSessions unit test stubs
        Retrieve all BGP sessions for project  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
