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
from metal.types.hardware_reservation import HardwareReservation  # noqa: E501
from metal.rest import ApiException

class TestHardwareReservation(unittest.TestCase):
    """HardwareReservation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HardwareReservation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.hardware_reservation.HardwareReservation()  # noqa: E501
        if include_optional :
            return HardwareReservation(
                id = '', 
                short_id = '', 
                facility = metal.models.facility.Facility(
                    id = '', 
                    name = '', 
                    code = '', 
                    features = [
                        ''
                        ], 
                    address = metal.models.address.Address(
                        address = '', 
                        address2 = '', 
                        city = '', 
                        state = '', 
                        zip_code = '', 
                        country = '', 
                        coordinates = metal.models.coordinates.Coordinates(
                            latitude = '', 
                            longitude = '', ), ), ), 
                plan = metal.models.plan.Plan(
                    id = '', 
                    slug = '', 
                    name = '', 
                    description = '', 
                    line = '', 
                    specs = metal.models.specs.specs(), 
                    pricing = metal.models.pricing.pricing(), 
                    legacy = True, 
                    class = '', 
                    available_in = [
                        metal.models.href.Href(
                            href = '', )
                        ], ), 
                href = '', 
                project = metal.models.project.Project(
                    id = '', 
                    name = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    max_devices = metal.models.max_devices.max_devices(), 
                    members = [
                        metal.models.href.Href(
                            href = '', )
                        ], 
                    memberships = [
                        metal.models.href.Href(
                            href = '', )
                        ], 
                    network_status = metal.models.network_status.network_status(), 
                    invitations = [
                        metal.models.href.Href(
                            href = '', )
                        ], 
                    payment_method = metal.models.href.Href(
                        href = '', ), 
                    devices = [
                        metal.models.href.Href(
                            href = '', )
                        ], 
                    ssh_keys = [
                        metal.models.href.Href(
                            href = '', )
                        ], 
                    volumes = [
                        metal.models.href.Href(
                            href = '', )
                        ], 
                    bgp_config = metal.models.href.Href(
                        href = '', ), 
                    customdata = metal.models.customdata.customdata(), ), 
                device = metal.models.device.Device(
                    id = '', 
                    short_id = '', 
                    hostname = '', 
                    description = '', 
                    state = '', 
                    tags = [
                        ''
                        ], 
                    image_url = '', 
                    billing_cycle = '', 
                    user = '', 
                    iqn = '', 
                    locked = True, 
                    bonding_mode = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    spot_instance = True, 
                    spot_price_max = 1.337, 
                    termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    customdata = metal.models.customdata.customdata(), 
                    provisioning_percentage = 1.337, 
                    operating_system = metal.models.operating_system.OperatingSystem(
                        id = '', 
                        slug = '', 
                        name = '', 
                        distro = '', 
                        version = '', 
                        provisionable_on = [
                            ''
                            ], ), 
                    always_pxe = True, 
                    ipxe_script_url = '', 
                    location = metal.models.hardware_location.HardwareLocation(
                        cage = '', 
                        facility = '', 
                        rack = '', 
                        row = '', 
                        switch = '', ), 
                    facility = metal.models.facility.Facility(
                        id = '', 
                        name = '', 
                        code = '', 
                        features = [
                            ''
                            ], 
                        address = metal.models.address.Address(
                            address = '', 
                            address2 = '', 
                            city = '', 
                            state = '', 
                            zip_code = '', 
                            country = '', 
                            coordinates = metal.models.coordinates.Coordinates(
                                latitude = '', 
                                longitude = '', ), ), ), 
                    plan = metal.models.plan.Plan(
                        id = '', 
                        slug = '', 
                        name = '', 
                        description = '', 
                        line = '', 
                        specs = metal.models.specs.specs(), 
                        pricing = metal.models.pricing.pricing(), 
                        legacy = True, 
                        class = '', 
                        available_in = [
                            metal.models.href.Href(
                                href = '', )
                            ], ), 
                    userdata = '', 
                    root_password = '', 
                    href = '', 
                    project = metal.models.href.Href(
                        href = '', ), 
                    project_lite = metal.models.href.Href(
                        href = '', ), 
                    volumes = [
                        metal.models.href.Href(
                            href = '', )
                        ], 
                    hardware_reservation = metal.models.href.Href(
                        href = '', ), 
                    ssh_keys = [
                        metal.models.href.Href(
                            href = '', )
                        ], 
                    ip_addresses = [
                        metal.models.ip_assignment.IPAssignment(
                            id = '', 
                            address_family = 56, 
                            netmask = '', 
                            public = True, 
                            enabled = True, 
                            cidr = 56, 
                            management = True, 
                            manageable = True, 
                            assigned_to = metal.models.href.Href(
                                href = '', ), 
                            network = '', 
                            gateway = '', 
                            href = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            parent_block = metal.models.parent_block.ParentBlock(
                                network = '', 
                                netmask = '', 
                                cidr = 56, 
                                href = '', ), )
                        ], 
                    provisioning_events = [
                        metal.models.event.Event(
                            id = '', 
                            state = '', 
                            type = '', 
                            body = '', 
                            relationships = [
                                metal.models.href.Href(
                                    href = '', )
                                ], 
                            interpolated = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            href = '', )
                        ], ), 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                remove_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return HardwareReservation(
        )

    def testHardwareReservation(self):
        """Test HardwareReservation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()