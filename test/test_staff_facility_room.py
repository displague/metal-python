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
from metal.types.staff_facility_room import StaffFacilityRoom  # noqa: E501
from metal.rest import ApiException

class TestStaffFacilityRoom(unittest.TestCase):
    """StaffFacilityRoom unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StaffFacilityRoom
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.staff_facility_room.StaffFacilityRoom()  # noqa: E501
        if include_optional :
            return StaffFacilityRoom(
                id = '', 
                name = '', 
                code = '', 
                max_racks = 56, 
                facility = metal.models.staff::facility_little.Staff::FacilityLittle(
                    id = '', 
                    name = '', 
                    code = '', 
                    metro = metal.models.staff::metro_little.Staff::MetroLittle(
                        id = '', 
                        name = '', 
                        code = '', 
                        features = [
                            ''
                            ], ), ), 
                cages = [
                    metal.models.staff::cage.Staff::Cage(
                        id = '', 
                        name = '', 
                        code = '', 
                        facility_room = metal.models.staff::facility_room.Staff::FacilityRoom(
                            id = '', 
                            name = '', 
                            code = '', 
                            max_racks = 56, 
                            facility = metal.models.staff::facility_little.Staff::FacilityLittle(
                                id = '', 
                                name = '', 
                                code = '', 
                                metro = metal.models.staff::metro_little.Staff::MetroLittle(
                                    id = '', 
                                    name = '', 
                                    code = '', 
                                    features = [
                                        ''
                                        ], ), ), ), 
                        rows = [
                            metal.models.staff::row.Staff::Row(
                                id = '', 
                                name = '', 
                                code = '', 
                                cage = metal.models.staff::cage.Staff::Cage(
                                    id = '', 
                                    name = '', 
                                    code = '', ), 
                                server_racks = [
                                    metal.models.staff::server_rack.Staff::ServerRack(
                                        id = '', 
                                        slot_number = 56, 
                                        server_rack = metal.models.staff::server_rack.Staff::ServerRack(
                                            id = '', 
                                            slot_number = 56, 
                                            hardware = None, ), 
                                        hardware = None, )
                                    ], )
                            ], )
                    ]
            )
        else :
            return StaffFacilityRoom(
        )

    def testStaffFacilityRoom(self):
        """Test StaffFacilityRoom"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
