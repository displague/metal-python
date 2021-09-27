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
from models.operating_systems_api import OperatingSystemsApi  # noqa: E501
from metal.rest import ApiException


class TestOperatingSystemsApi(unittest.TestCase):
    """OperatingSystemsApi unit test stubs"""

    def setUp(self):
        self.api = models.operating_systems_api.OperatingSystemsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_operating_systems(self):
        """Test case for find_operating_systems

        Retrieve all operating systems  # noqa: E501
        """
        pass

    def test_find_operating_systems_by_organization(self):
        """Test case for find_operating_systems_by_organization

        Retrieve all operating systems visible by the organization  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
