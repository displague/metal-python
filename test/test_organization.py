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
from metal.types.organization import Organization  # noqa: E501
from metal.rest import ApiException

class TestOrganization(unittest.TestCase):
    """Organization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Organization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.organization.Organization()  # noqa: E501
        if include_optional :
            return Organization(
                id = '', 
                name = '', 
                description = '', 
                website = '', 
                twitter = '', 
                logo = bytes(b'blah'), 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                projects = [
                    metal.models.href.Href(
                        href = '', )
                    ], 
                members = [
                    metal.models.href.Href(
                        href = '', )
                    ], 
                memberships = [
                    metal.models.href.Href(
                        href = '', )
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
                        longitude = '', ), ), 
                billing_address = metal.models.address.Address(
                    address = '', 
                    address2 = '', 
                    city = '', 
                    state = '', 
                    zip_code = '', 
                    country = '', 
                    coordinates = metal.models.coordinates.Coordinates(
                        latitude = '', 
                        longitude = '', ), ), 
                entitlement = metal.models.entitlement.Entitlement(
                    id = '', 
                    description = '', 
                    slug = '', 
                    name = '', 
                    weight = 56, 
                    instance_quota = metal.models.instance_quota.instance_quota(), 
                    project_quota = 56, 
                    volume_quota = metal.models.volume_quota.volume_quota(), 
                    ip_quota = metal.models.ip_quota.ip_quota(), 
                    feature_access = metal.models.feature_access.feature_access(), 
                    href = '', 
                    volume_limits = metal.models.volume_limits.volume_limits(), ), 
                terms = 56, 
                credit_amount = 1.337, 
                customdata = None, 
                enforce_2fa_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return Organization(
        )

    def testOrganization(self):
        """Test Organization"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
