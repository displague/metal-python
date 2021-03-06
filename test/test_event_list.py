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
from metal.types.event_list import EventList  # noqa: E501
from metal.rest import ApiException

class TestEventList(unittest.TestCase):
    """EventList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EventList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.event_list.EventList()  # noqa: E501
        if include_optional :
            return EventList(
                events = [
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
                    ], 
                meta = metal.models.meta.Meta(
                    first = metal.models.href.Href(
                        href = '', ), 
                    previous = metal.models.href.Href(
                        href = '', ), 
                    self = metal.models.href.Href(
                        href = '', ), 
                    next = metal.models.href.Href(
                        href = '', ), 
                    last = metal.models.href.Href(
                        href = '', ), 
                    total = 56, )
            )
        else :
            return EventList(
        )

    def testEventList(self):
        """Test EventList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
