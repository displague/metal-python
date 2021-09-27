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
from metal.types.port_vlan_assignment_list import PortVlanAssignmentList  # noqa: E501
from metal.rest import ApiException

class TestPortVlanAssignmentList(unittest.TestCase):
    """PortVlanAssignmentList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PortVlanAssignmentList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.port_vlan_assignment_list.PortVlanAssignmentList()  # noqa: E501
        if include_optional :
            return PortVlanAssignmentList(
                vlan_assignments = [
                    metal.models.port_vlan_assignment.PortVlanAssignment(
                        id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        native = True, 
                        state = 'assigned', 
                        vlan = 56, 
                        port = metal.models.href.Href(
                            href = '', ), 
                        virtual_network = metal.models.href.Href(
                            href = '', ), )
                    ]
            )
        else :
            return PortVlanAssignmentList(
        )

    def testPortVlanAssignmentList(self):
        """Test PortVlanAssignmentList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()