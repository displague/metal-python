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
import datetime

import metal
from metal.types.payment_method_billing_address import PaymentMethodBillingAddress  # noqa: E501
from metal.rest import ApiException

class TestPaymentMethodBillingAddress(unittest.TestCase):
    """PaymentMethodBillingAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentMethodBillingAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.payment_method_billing_address.PaymentMethodBillingAddress()  # noqa: E501
        if include_optional :
            return PaymentMethodBillingAddress(
                street_address = '', 
                postal_code = '', 
                country_code_alpha2 = ''
            )
        else :
            return PaymentMethodBillingAddress(
        )

    def testPaymentMethodBillingAddress(self):
        """Test PaymentMethodBillingAddress"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
