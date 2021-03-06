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
from metal.types.staff_hardware import StaffHardware  # noqa: E501
from metal.rest import ApiException

class TestStaffHardware(unittest.TestCase):
    """StaffHardware unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StaffHardware
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.staff_hardware.StaffHardware()  # noqa: E501
        if include_optional :
            return StaffHardware(
                id = '', 
                arch = '', 
                bios_password = '', 
                data = None, 
                dhcp_group = '', 
                efi_boot = True, 
                hostname = '', 
                leased = True, 
                location = '', 
                maintenance_state = '', 
                management = None, 
                model_number = '', 
                name = '', 
                rack_spaces_labels = '', 
                serial_number = '', 
                services = None, 
                state = '', 
                supported_networking = [
                    ''
                    ], 
                type = '', 
                u_spaces = 56, 
                reserved = True, 
                link_aggregation = '', 
                vrf = '', 
                provisioner = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                bonding_mode = 56, 
                total_provisions = 56, 
                successful_provisions = 56, 
                failed_provisions = 56, 
                last_provision_success = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_provision_failed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_deprovision_success = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_deprovision_failed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                uefi_supports_rfc3021 = True, 
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
                                max_racks = 56, ), 
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
                        ], ), 
                cage = metal.models.staff::cage.Staff::Cage(
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
                                    ], ), ), 
                        cages = [
                            metal.models.staff::cage.Staff::Cage(
                                id = '', 
                                name = '', 
                                code = '', 
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
                            ], ), 
                    rows = [
                        metal.models.staff::row.Staff::Row(
                            id = '', 
                            name = '', 
                            code = '', )
                        ], ), 
                row = metal.models.staff::row.Staff::Row(
                    id = '', 
                    name = '', 
                    code = '', 
                    cage = metal.models.staff::cage.Staff::Cage(
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
                                        ], ), ), 
                            cages = [
                                metal.models.staff::cage.Staff::Cage(
                                    id = '', 
                                    name = '', 
                                    code = '', 
                                    rows = [
                                        metal.models.staff::row.Staff::Row(
                                            id = '', 
                                            name = '', 
                                            code = '', 
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
                                ], ), 
                        rows = [
                            metal.models.staff::row.Staff::Row(
                                id = '', 
                                name = '', 
                                code = '', )
                            ], ), 
                    server_racks = [
                        metal.models.staff::server_rack.Staff::ServerRack(
                            id = '', 
                            slot_number = 56, 
                            hardware = None, )
                        ], ), 
                server_rack = metal.models.staff::server_rack.Staff::ServerRack(
                    id = '', 
                    slot_number = 56, 
                    server_rack = metal.models.staff::server_rack.Staff::ServerRack(
                        id = '', 
                        slot_number = 56, 
                        hardware = None, ), 
                    hardware = None, ), 
                manufacturer = metal.models.staff::manufacturer.Staff::Manufacturer(
                    id = '', 
                    name = '', 
                    slug = '', 
                    type = '', 
                    contact_name = '', 
                    contact_phone = '', 
                    contact_email = '', 
                    website_url = '', 
                    logo_url = '', ), 
                plan_verion = metal.models.staff::plan_version.Staff::PlanVersion(
                    id = '', 
                    name = '', 
                    slug = '', 
                    specs = '', 
                    active = True, 
                    priority = 56, 
                    storage = '', 
                    preinstallable = True, 
                    plan = metal.models.staff::plan.Staff::Plan(
                        id = '', 
                        name = '', 
                        slug = '', 
                        description = '', 
                        line = '', 
                        specs = metal.models.specs.specs(), 
                        legacy = True, 
                        pricing = metal.models.pricing.pricing(), 
                        available_in_codes = [
                            ''
                            ], 
                        default_plan_version_id = '', 
                        original_slug = '', 
                        deployment_types = [
                            ''
                            ], 
                        zoho_item_id = '', 
                        configuration = metal.models.configuration.configuration(), 
                        features = [
                            ''
                            ], 
                        aliases = [
                            ''
                            ], 
                        default_preinstallable_operating_system_id = '', 
                        default_plan_version = metal.models.staff::plan_version.Staff::PlanVersion(
                            id = '', 
                            name = '', 
                            slug = '', 
                            specs = '', 
                            active = True, 
                            priority = 56, 
                            storage = '', 
                            preinstallable = True, 
                            facility = metal.models.staff::facility_little.Staff::FacilityLittle(
                                id = '', 
                                name = '', 
                                code = '', 
                                metro = metal.models.staff::metro_little.Staff::MetroLittle(
                                    id = '', 
                                    name = '', 
                                    code = '', ), ), ), 
                        plan_versions = [
                            metal.models.staff::plan_version.Staff::PlanVersion(
                                id = '', 
                                name = '', 
                                slug = '', 
                                specs = '', 
                                active = True, 
                                priority = 56, 
                                storage = '', 
                                preinstallable = True, )
                            ], ), 
                    facility = metal.models.staff::facility_little.Staff::FacilityLittle(
                        id = '', 
                        name = '', 
                        code = '', ), ), 
                leased_from = metal.models.staff::provider.Staff::Provider(
                    id = '', 
                    name = '', 
                    slug = '', 
                    type = '', 
                    contact_name = '', 
                    contact_phone = '', 
                    contact_email = '', 
                    website_url = '', 
                    logo_url = '', 
                    address = metal.models.staff::address.Staff::Address(
                        id = '', 
                        address2 = '', 
                        city = '', 
                        state = '', 
                        zip_code = '', 
                        country = '', 
                        coordinates = metal.models.coordinates.coordinates(), ), ), 
                plan = metal.models.staff::plan.Staff::Plan(
                    id = '', 
                    name = '', 
                    slug = '', 
                    description = '', 
                    line = '', 
                    specs = metal.models.specs.specs(), 
                    legacy = True, 
                    pricing = metal.models.pricing.pricing(), 
                    available_in_codes = [
                        ''
                        ], 
                    default_plan_version_id = '', 
                    original_slug = '', 
                    deployment_types = [
                        ''
                        ], 
                    zoho_item_id = '', 
                    configuration = metal.models.configuration.configuration(), 
                    features = [
                        ''
                        ], 
                    aliases = [
                        ''
                        ], 
                    default_preinstallable_operating_system_id = '', 
                    default_plan_version = metal.models.staff::plan_version.Staff::PlanVersion(
                        id = '', 
                        name = '', 
                        slug = '', 
                        specs = '', 
                        active = True, 
                        priority = 56, 
                        storage = '', 
                        preinstallable = True, 
                        plan = metal.models.staff::plan.Staff::Plan(
                            id = '', 
                            name = '', 
                            slug = '', 
                            description = '', 
                            line = '', 
                            specs = metal.models.specs.specs(), 
                            legacy = True, 
                            pricing = metal.models.pricing.pricing(), 
                            default_plan_version_id = '', 
                            original_slug = '', 
                            zoho_item_id = '', 
                            configuration = metal.models.configuration.configuration(), 
                            default_preinstallable_operating_system_id = '', 
                            plan_versions = [
                                metal.models.staff::plan_version.Staff::PlanVersion(
                                    id = '', 
                                    name = '', 
                                    slug = '', 
                                    specs = '', 
                                    active = True, 
                                    priority = 56, 
                                    storage = '', 
                                    preinstallable = True, 
                                    facility = metal.models.staff::facility_little.Staff::FacilityLittle(
                                        id = '', 
                                        name = '', 
                                        code = '', 
                                        metro = metal.models.staff::metro_little.Staff::MetroLittle(
                                            id = '', 
                                            name = '', 
                                            code = '', ), ), )
                                ], ), 
                        facility = metal.models.staff::facility_little.Staff::FacilityLittle(
                            id = '', 
                            name = '', 
                            code = '', ), ), 
                    plan_versions = [
                        metal.models.staff::plan_version.Staff::PlanVersion(
                            id = '', 
                            name = '', 
                            slug = '', 
                            specs = '', 
                            active = True, 
                            priority = 56, 
                            storage = '', 
                            preinstallable = True, )
                        ], ), 
                ip_assignments = [
                    metal.models.staff::ip_address.Staff::IpAddress(
                        id = '', 
                        network = '', 
                        address_family = 56, 
                        netmask = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        details = '', 
                        public = True, 
                        management = True, 
                        manageable = True, 
                        enabled = True, 
                        created_by = '', 
                        global_ip = True, 
                        reservation = True, 
                        customdata = metal.models.customdata.customdata(), 
                        bill = True, 
                        tags = [
                            ''
                            ], 
                        address = '', 
                        gateway = '', 
                        cidr = 56, 
                        state = '', 
                        requested_quantity = 56, 
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
                        metro = metal.models.staff::metro_little.Staff::MetroLittle(
                            id = '', 
                            name = '', 
                            code = '', ), 
                        interface = None, )
                    ], 
                notes = [
                    None
                    ], 
                rack_spaces = [
                    None
                    ], 
                ip_blocks = [
                    metal.models.staff::ip_address.Staff::IpAddress(
                        id = '', 
                        network = '', 
                        address_family = 56, 
                        netmask = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        details = '', 
                        public = True, 
                        management = True, 
                        manageable = True, 
                        enabled = True, 
                        created_by = '', 
                        global_ip = True, 
                        reservation = True, 
                        customdata = metal.models.customdata.customdata(), 
                        bill = True, 
                        tags = [
                            ''
                            ], 
                        address = '', 
                        gateway = '', 
                        cidr = 56, 
                        state = '', 
                        requested_quantity = 56, 
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
                        metro = metal.models.staff::metro_little.Staff::MetroLittle(
                            id = '', 
                            name = '', 
                            code = '', ), 
                        interface = None, )
                    ], 
                instance = None, 
                hardware_reservation = None, 
                preinstalled_operating_system_version = None
            )
        else :
            return StaffHardware(
        )

    def testStaffHardware(self):
        """Test StaffHardware"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
