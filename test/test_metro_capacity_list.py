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
from metal.types.metro_capacity_list import MetroCapacityList  # noqa: E501
from metal.rest import ApiException

class TestMetroCapacityList(unittest.TestCase):
    """MetroCapacityList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetroCapacityList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.metro_capacity_list.MetroCapacityList()  # noqa: E501
        if include_optional :
            return MetroCapacityList(
                capacity = metal.models.metro_capacity_report.MetroCapacityReport(
                    ny = metal.models.capacity_per_facility.CapacityPerFacility(
                        baremetal_2a = metal.models.capacity_level_per_baremetal.CapacityLevelPerBaremetal(
                            level = '', ), 
                        baremetal_2a2 = metal.models.capacity_level_per_baremetal.CapacityLevelPerBaremetal(
                            level = '', ), 
                        baremetal_1 = metal.models.capacity_level_per_baremetal.CapacityLevelPerBaremetal(
                            level = '', ), 
                        baremetal_3 = metal.models.capacity_level_per_baremetal.CapacityLevelPerBaremetal(
                            level = '', ), 
                        c2/medium/x86 = metal.models.capacity_level_per_baremetal.CapacityLevelPerBaremetal(
                            level = '', ), 
                        baremetal_2 = metal.models.capacity_level_per_baremetal.CapacityLevelPerBaremetal(
                            level = '', ), 
                        m2/xlarge/x86 = metal.models.capacity_level_per_baremetal.CapacityLevelPerBaremetal(
                            level = '', ), 
                        baremetal_s = metal.models.capacity_level_per_baremetal.CapacityLevelPerBaremetal(
                            level = '', ), 
                        baremetal_0 = metal.models.capacity_level_per_baremetal.CapacityLevelPerBaremetal(
                            level = '', ), ), 
                    sv = metal.models.capacity_per_facility.CapacityPerFacility(), 
                    am = metal.models.capacity_per_facility.CapacityPerFacility(), 
                    ch = metal.models.capacity_per_facility.CapacityPerFacility(), 
                    la = metal.models.capacity_per_facility.CapacityPerFacility(), 
                    sg = metal.models.capacity_per_facility.CapacityPerFacility(), 
                    da = metal.models.capacity_per_facility.CapacityPerFacility(), )
            )
        else :
            return MetroCapacityList(
        )

    def testMetroCapacityList(self):
        """Test MetroCapacityList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
