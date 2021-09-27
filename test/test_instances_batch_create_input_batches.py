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
from metal.types.instances_batch_create_input_batches import InstancesBatchCreateInputBatches  # noqa: E501
from metal.rest import ApiException

class TestInstancesBatchCreateInputBatches(unittest.TestCase):
    """InstancesBatchCreateInputBatches unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InstancesBatchCreateInputBatches
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.instances_batch_create_input_batches.InstancesBatchCreateInputBatches()  # noqa: E501
        if include_optional :
            return InstancesBatchCreateInputBatches(
                plan = '', 
                hostname = '', 
                hostnames = [
                    ''
                    ], 
                facility = [
                    ''
                    ], 
                metro = '', 
                description = '', 
                billing_cycle = '', 
                operating_system = '', 
                always_pxe = True, 
                userdata = '', 
                locked = True, 
                termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                tags = [
                    ''
                    ], 
                project_ssh_keys = [
                    ''
                    ], 
                user_ssh_keys = [
                    ''
                    ], 
                no_ssh_keys = True, 
                features = [
                    ''
                    ], 
                customdata = metal.models.customdata.customdata(), 
                ip_addresses = [
                    metal.models.instances_batch_create_input_ip_addresses.InstancesBatchCreateInput_ip_addresses(
                        address_family = 4.0, 
                        public = False, 
                        cidr = 28.0, 
                        ip_reservations = [
                            ''
                            ], )
                    ]
            )
        else :
            return InstancesBatchCreateInputBatches(
        )

    def testInstancesBatchCreateInputBatches(self):
        """Test InstancesBatchCreateInputBatches"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
