# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import metal
from metal.paths.organizations_organization_id_connections import post  # noqa: E501
from metal import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOrganizationsOrganizationIdConnections(ApiTestMixin, unittest.TestCase):
    """
    OrganizationsOrganizationIdConnections unit test stubs
        Request a new interconnection for the organization  # noqa: E501
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
