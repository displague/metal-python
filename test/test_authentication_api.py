# coding: utf-8

"""
    Metal API

    This is the API for Equinix Metal. The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account.  The official API docs are hosted at <https://metal.equinix.com/developers/api>.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import metal
from models.authentication_api import AuthenticationApi  # noqa: E501
from metal.rest import ApiException


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = models.authentication_api.AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_api_key(self):
        """Test case for create_api_key

        Create a API key  # noqa: E501
        """
        pass

    def test_create_project_api_key(self):
        """Test case for create_project_api_key

        Create an API key for a project.  # noqa: E501
        """
        pass

    def test_delete_api_key(self):
        """Test case for delete_api_key

        Delete the API key  # noqa: E501
        """
        pass

    def test_delete_user_api_key(self):
        """Test case for delete_user_api_key

        Delete the API key  # noqa: E501
        """
        pass

    def test_find_api_keys(self):
        """Test case for find_api_keys

        Retrieve all user API keys  # noqa: E501
        """
        pass

    def test_find_project_api_keys(self):
        """Test case for find_project_api_keys

        Retrieve all API keys for the project.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
