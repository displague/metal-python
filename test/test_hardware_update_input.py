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
from metal.types.hardware_update_input import HardwareUpdateInput  # noqa: E501
from metal.rest import ApiException

class TestHardwareUpdateInput(unittest.TestCase):
    """HardwareUpdateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HardwareUpdateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.hardware_update_input.HardwareUpdateInput()  # noqa: E501
        if include_optional :
            return HardwareUpdateInput(
                state = '', 
                u_spaces = 56, 
                model_number = '', 
                serial_number = '', 
                server_rack_id = '', 
                leased = True, 
                lease_number = '', 
                lease_expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                arch = '', 
                dhcp_group = '', 
                efi_boot = True, 
                bios_password = '', 
                maintenance_state = '', 
                name = '', 
                static_name = '', 
                uefi_supports_rfc3021 = True, 
                preinstalled_operating_system_version_id = '', 
                link_aggregation = '', 
                provisioner = '', 
                supported_networking = [
                    ''
                    ], 
                services = None, 
                management = None, 
                data = None, 
                role = '', 
                vlan_id = 56, 
                tpm = True, 
                switch_short_id = '', 
                is_primary = True, 
                loopback_ip = '', 
                vrf = '', 
                exclude_from_narwhal = True
            )
        else :
            return HardwareUpdateInput(
        )

    def testHardwareUpdateInput(self):
        """Test HardwareUpdateInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
