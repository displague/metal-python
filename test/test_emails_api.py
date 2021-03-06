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
from models.emails_api import EmailsApi  # noqa: E501
from metal.rest import ApiException


class TestEmailsApi(unittest.TestCase):
    """EmailsApi unit test stubs"""

    def setUp(self):
        self.api = models.emails_api.EmailsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_email(self):
        """Test case for create_email

        Create an email  # noqa: E501
        """
        pass

    def test_delete_email(self):
        """Test case for delete_email

        Delete the email  # noqa: E501
        """
        pass

    def test_find_email_by_id(self):
        """Test case for find_email_by_id

        Retrieve an email  # noqa: E501
        """
        pass

    def test_update_email(self):
        """Test case for update_email

        Update the email  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
