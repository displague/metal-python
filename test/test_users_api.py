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
from models.users_api import UsersApi  # noqa: E501
from metal.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = models.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a user  # noqa: E501
        """
        pass

    def test_find_current_user(self):
        """Test case for find_current_user

        Retrieve the current user  # noqa: E501
        """
        pass

    def test_find_invitations(self):
        """Test case for find_invitations

        Retrieve current user invitations  # noqa: E501
        """
        pass

    def test_find_user_by_id(self):
        """Test case for find_user_by_id

        Retrieve a user  # noqa: E501
        """
        pass

    def test_find_user_customdata(self):
        """Test case for find_user_customdata

        Retrieve the custom metadata of a user  # noqa: E501
        """
        pass

    def test_find_users(self):
        """Test case for find_users

        Retrieve all users  # noqa: E501
        """
        pass

    def test_update_current_user(self):
        """Test case for update_current_user

        Update the current user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
