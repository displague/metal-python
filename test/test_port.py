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
from metal.types.port import Port  # noqa: E501
from metal.rest import ApiException

class TestPort(unittest.TestCase):
    """Port unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Port
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.port.Port()  # noqa: E501
        if include_optional :
            return Port(
                id = '', 
                type = '', 
                name = '', 
                data = None, 
                disbond_operation_supported = True, 
                hardware = metal.models.href.Href(
                    href = '', ), 
                virtual_networks = [
                    metal.models.href.Href(
                        href = '', )
                    ], 
                connected_port = metal.models.href.Href(
                    href = '', ), 
                href = ''
            )
        else :
            return Port(
        )

    def testPort(self):
        """Test Port"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
