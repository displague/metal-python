# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import metal
from metal.paths.reset_password import post  # noqa: E501
from metal import configuration, schemas, api_client

from .. import ApiTestMixin


class TestResetPassword(ApiTestMixin, unittest.TestCase):
    """
    ResetPassword unit test stubs
        Create a password reset token  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201
    response_body = ''


if __name__ == '__main__':
    unittest.main()