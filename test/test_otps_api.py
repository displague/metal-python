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
from models.otps_api import OtpsApi  # noqa: E501
from metal.rest import ApiException


class TestOtpsApi(unittest.TestCase):
    """OtpsApi unit test stubs"""

    def setUp(self):
        self.api = models.otps_api.OtpsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_ensure_otp(self):
        """Test case for find_ensure_otp

        Verify user by providing an OTP  # noqa: E501
        """
        pass

    def test_find_recovery_codes(self):
        """Test case for find_recovery_codes

        Retrieve my recovery codes  # noqa: E501
        """
        pass

    def test_receive_codes(self):
        """Test case for receive_codes

        Receive an OTP per sms  # noqa: E501
        """
        pass

    def test_regenerate_codes(self):
        """Test case for regenerate_codes

        Generate new recovery codes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
