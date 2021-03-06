# coding: utf-8

"""
    Metal API

    This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import metal
from models.ssh_keys_api import SSHKeysApi  # noqa: E501
from metal.rest import ApiException


class TestSSHKeysApi(unittest.TestCase):
    """SSHKeysApi unit test stubs"""

    def setUp(self):
        self.api = models.ssh_keys_api.SSHKeysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project_ssh_key(self):
        """Test case for create_project_ssh_key

        Create a ssh key for the given project  # noqa: E501
        """
        pass

    def test_create_ssh_key(self):
        """Test case for create_ssh_key

        Create a ssh key for the current user  # noqa: E501
        """
        pass

    def test_delete_ssh_key(self):
        """Test case for delete_ssh_key

        Delete the ssh key  # noqa: E501
        """
        pass

    def test_find_device_ssh_keys(self):
        """Test case for find_device_ssh_keys

        Retrieve a device's ssh keys  # noqa: E501
        """
        pass

    def test_find_project_ssh_keys(self):
        """Test case for find_project_ssh_keys

        Retrieve a project's ssh keys  # noqa: E501
        """
        pass

    def test_find_ssh_key_by_id(self):
        """Test case for find_ssh_key_by_id

        Retrieve a ssh key  # noqa: E501
        """
        pass

    def test_find_ssh_keys(self):
        """Test case for find_ssh_keys

        Retrieve all ssh keys  # noqa: E501
        """
        pass

    def test_update_ssh_key(self):
        """Test case for update_ssh_key

        Update the ssh key  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
