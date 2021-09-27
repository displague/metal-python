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
from models.self_service_reservations_api import SelfServiceReservationsApi  # noqa: E501
from metal.rest import ApiException


class TestSelfServiceReservationsApi(unittest.TestCase):
    """SelfServiceReservationsApi unit test stubs"""

    def setUp(self):
        self.api = models.self_service_reservations_api.SelfServiceReservationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_self_service_reservation(self):
        """Test case for create_self_service_reservation

        Create a reservation  # noqa: E501
        """
        pass

    def test_find_self_service_reservation(self):
        """Test case for find_self_service_reservation

        Retrieve a reservation  # noqa: E501
        """
        pass

    def test_find_self_service_reservations(self):
        """Test case for find_self_service_reservations

        Retrieve all reservations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()