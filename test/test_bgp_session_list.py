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
from metal.types.bgp_session_list import BgpSessionList  # noqa: E501
from metal.rest import ApiException

class TestBgpSessionList(unittest.TestCase):
    """BgpSessionList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BgpSessionList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.bgp_session_list.BgpSessionList()  # noqa: E501
        if include_optional :
            return BgpSessionList(
                bgp_sessions = [
                    metal.models.bgp_session.BgpSession(
                        id = '', 
                        status = 'unknown', 
                        learned_routes = [
                            '10.32.16.0/31'
                            ], 
                        address_family = 'ipv4', 
                        device = metal.models.href.Href(
                            href = '', ), 
                        href = '', 
                        default_route = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else :
            return BgpSessionList(
        )

    def testBgpSessionList(self):
        """Test BgpSessionList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
