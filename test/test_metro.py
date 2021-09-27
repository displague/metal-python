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
import datetime

import metal
from metal.types.metro import Metro  # noqa: E501
from metal.rest import ApiException

class TestMetro(unittest.TestCase):
    """Metro unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Metro
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.metro.Metro()  # noqa: E501
        if include_optional :
            return Metro(
                id = '', 
                name = '', 
                code = '', 
                country = ''
            )
        else :
            return Metro(
        )

    def testMetro(self):
        """Test Metro"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()