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
from metal.types.ip_assignment import IPAssignment  # noqa: E501
from metal.rest import ApiException

class TestIPAssignment(unittest.TestCase):
    """IPAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IPAssignment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.ip_assignment.IPAssignment()  # noqa: E501
        if include_optional :
            return IPAssignment(
                id = '', 
                address_family = 56, 
                netmask = '', 
                public = True, 
                enabled = True, 
                cidr = 56, 
                management = True, 
                manageable = True, 
                global_ip = True, 
                assigned_to = metal.models.href.Href(
                    href = '', ), 
                network = '', 
                address = '', 
                gateway = '', 
                href = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                metro = metal.models.ip_assignment_metro.IPAssignment_metro(), 
                parent_block = metal.models.parent_block.ParentBlock(
                    network = '', 
                    netmask = '', 
                    cidr = 56, 
                    href = '', )
            )
        else :
            return IPAssignment(
        )

    def testIPAssignment(self):
        """Test IPAssignment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
