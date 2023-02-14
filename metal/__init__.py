# coding: utf-8

# flake8: noqa

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://metal.equinix.com/developers/api>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. The fields available for search differ by resource, as does the search strategy.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from models.authentication_api import AuthenticationApi
from models.bgp_api import BGPApi
from models.batches_api import BatchesApi
from models.capacity_api import CapacityApi
from models.devices_api import DevicesApi
from models.emails_api import EmailsApi
from models.events_api import EventsApi
from models.facilities_api import FacilitiesApi
from models.hardware_reservations_api import HardwareReservationsApi
from models.ip_addresses_api import IPAddressesApi
from models.incidents_api import IncidentsApi
from models.interconnections_api import InterconnectionsApi
from models.invitations_api import InvitationsApi
from models.licenses_api import LicensesApi
from models.memberships_api import MembershipsApi
from models.metal_gateways_api import MetalGatewaysApi
from models.metros_api import MetrosApi
from models.otps_api import OTPsApi
from models.operating_systems_api import OperatingSystemsApi
from models.organizations_api import OrganizationsApi
from models.password_reset_tokens_api import PasswordResetTokensApi
from models.payment_methods_api import PaymentMethodsApi
from models.plans_api import PlansApi
from models.ports_api import PortsApi
from models.projects_api import ProjectsApi
from models.ssh_keys_api import SSHKeysApi
from models.self_service_reservations_api import SelfServiceReservationsApi
from models.spot_market_api import SpotMarketApi
from models.support_request_api import SupportRequestApi
from models.transfer_requests_api import TransferRequestsApi
from models.two_factor_auth_api import TwoFactorAuthApi
from models.usages_api import UsagesApi
from models.user_verification_tokens_api import UserVerificationTokensApi
from models.userdata_api import UserdataApi
from models.users_api import UsersApi
from models.vlans_api import VLANsApi
from models.vrfs_api import VRFsApi

# import ApiClient
from metal.api_client import ApiClient
from metal.configuration import Configuration
from metal.exceptions import OpenApiException
from metal.exceptions import ApiTypeError
from metal.exceptions import ApiValueError
from metal.exceptions import ApiKeyError
from metal.exceptions import ApiAttributeError
from metal.exceptions import ApiException
# import models into sdk package
from metal.types.activate_hardware_reservation_request import ActivateHardwareReservationRequest
from metal.types.address import Address
from metal.types.auth_token import AuthToken
from metal.types.auth_token_input import AuthTokenInput
from metal.types.auth_token_list import AuthTokenList
from metal.types.auth_token_project import AuthTokenProject
from metal.types.auth_token_user import AuthTokenUser
from metal.types.bgp_session_input import BGPSessionInput
from metal.types.batch import Batch
from metal.types.batches_list import BatchesList
from metal.types.bgp_config import BgpConfig
from metal.types.bgp_config_request_input import BgpConfigRequestInput
from metal.types.bgp_neighbor_data import BgpNeighborData
from metal.types.bgp_route import BgpRoute
from metal.types.bgp_session import BgpSession
from metal.types.bgp_session_list import BgpSessionList
from metal.types.bgp_session_neighbors import BgpSessionNeighbors
from metal.types.bond_port_data import BondPortData
from metal.types.capacity_check_per_facility_info import CapacityCheckPerFacilityInfo
from metal.types.capacity_check_per_facility_list import CapacityCheckPerFacilityList
from metal.types.capacity_check_per_metro_info import CapacityCheckPerMetroInfo
from metal.types.capacity_check_per_metro_list import CapacityCheckPerMetroList
from metal.types.capacity_input import CapacityInput
from metal.types.capacity_level_per_baremetal import CapacityLevelPerBaremetal
from metal.types.capacity_list import CapacityList
from metal.types.capacity_per_facility import CapacityPerFacility
from metal.types.capacity_per_metro_input import CapacityPerMetroInput
from metal.types.capacity_per_new_facility import CapacityPerNewFacility
from metal.types.capacity_report import CapacityReport
from metal.types.coordinates import Coordinates
from metal.types.create_device_request import CreateDeviceRequest
from metal.types.create_email_input import CreateEmailInput
from metal.types.create_interconnection_port_virtual_circuit201_response import CreateInterconnectionPortVirtualCircuit201Response
from metal.types.create_interconnection_port_virtual_circuit_request import CreateInterconnectionPortVirtualCircuitRequest
from metal.types.create_metal_gateway_request import CreateMetalGatewayRequest
from metal.types.create_self_service_reservation_request import CreateSelfServiceReservationRequest
from metal.types.create_self_service_reservation_request_period import CreateSelfServiceReservationRequestPeriod
from metal.types.device import Device
from metal.types.device_action_input import DeviceActionInput
from metal.types.device_actions_inner import DeviceActionsInner
from metal.types.device_create_in_facility_input import DeviceCreateInFacilityInput
from metal.types.device_create_in_metro_input import DeviceCreateInMetroInput
from metal.types.device_create_input import DeviceCreateInput
from metal.types.device_create_input_ip_addresses_inner import DeviceCreateInputIpAddressesInner
from metal.types.device_created_by import DeviceCreatedBy
from metal.types.device_list import DeviceList
from metal.types.device_metro import DeviceMetro
from metal.types.device_project import DeviceProject
from metal.types.device_project_lite import DeviceProjectLite
from metal.types.device_update_input import DeviceUpdateInput
from metal.types.device_usage import DeviceUsage
from metal.types.device_usage_list import DeviceUsageList
from metal.types.email import Email
from metal.types.email_input import EmailInput
from metal.types.entitlement import Entitlement
from metal.types.error import Error
from metal.types.event import Event
from metal.types.event_list import EventList
from metal.types.fabric_service_token import FabricServiceToken
from metal.types.facility import Facility
from metal.types.facility_input import FacilityInput
from metal.types.facility_input_facility import FacilityInputFacility
from metal.types.facility_list import FacilityList
from metal.types.find_ip_address_by_id200_response import FindIPAddressById200Response
from metal.types.find_metal_gateway_by_id200_response import FindMetalGatewayById200Response
from metal.types.find_traffic_timeframe_parameter import FindTrafficTimeframeParameter
from metal.types.global_bgp_range import GlobalBgpRange
from metal.types.global_bgp_range_list import GlobalBgpRangeList
from metal.types.hardware_reservation import HardwareReservation
from metal.types.hardware_reservation_list import HardwareReservationList
from metal.types.href import Href
from metal.types.ip_assignment import IPAssignment
from metal.types.ip_assignment_input import IPAssignmentInput
from metal.types.ip_assignment_list import IPAssignmentList
from metal.types.ip_assignment_metro import IPAssignmentMetro
from metal.types.ip_assignment_update_input import IPAssignmentUpdateInput
from metal.types.ip_availabilities_list import IPAvailabilitiesList
from metal.types.ip_reservation import IPReservation
from metal.types.ip_reservation_facility import IPReservationFacility
from metal.types.ip_reservation_list import IPReservationList
from metal.types.ip_reservation_list_ip_addresses_inner import IPReservationListIpAddressesInner
from metal.types.ip_reservation_metro import IPReservationMetro
from metal.types.ip_reservation_request_input import IPReservationRequestInput
from metal.types.instances_batch_create_input import InstancesBatchCreateInput
from metal.types.instances_batch_create_input_batches_inner import InstancesBatchCreateInputBatchesInner
from metal.types.instances_batch_create_input_batches_inner_all_of import InstancesBatchCreateInputBatchesInnerAllOf
from metal.types.interconnection import Interconnection
from metal.types.interconnection_create_input import InterconnectionCreateInput
from metal.types.interconnection_list import InterconnectionList
from metal.types.interconnection_metro import InterconnectionMetro
from metal.types.interconnection_port import InterconnectionPort
from metal.types.interconnection_port_list import InterconnectionPortList
from metal.types.interconnection_update_input import InterconnectionUpdateInput
from metal.types.invitation import Invitation
from metal.types.invitation_input import InvitationInput
from metal.types.invitation_list import InvitationList
from metal.types.license import License
from metal.types.license_create_input import LicenseCreateInput
from metal.types.license_list import LicenseList
from metal.types.license_update_input import LicenseUpdateInput
from metal.types.membership import Membership
from metal.types.membership_input import MembershipInput
from metal.types.membership_list import MembershipList
from metal.types.meta import Meta
from metal.types.metadata import Metadata
from metal.types.metadata_network import MetadataNetwork
from metal.types.metadata_network_network import MetadataNetworkNetwork
from metal.types.metadata_network_network_bonding import MetadataNetworkNetworkBonding
from metal.types.metal_gateway import MetalGateway
from metal.types.metal_gateway_create_input import MetalGatewayCreateInput
from metal.types.metal_gateway_list import MetalGatewayList
from metal.types.metal_gateway_list_metal_gateways_inner import MetalGatewayListMetalGatewaysInner
from metal.types.metal_gateway_lite import MetalGatewayLite
from metal.types.metro import Metro
from metal.types.metro_capacity_list import MetroCapacityList
from metal.types.metro_capacity_report import MetroCapacityReport
from metal.types.metro_input import MetroInput
from metal.types.metro_list import MetroList
from metal.types.metro_server_info import MetroServerInfo
from metal.types.move_hardware_reservation_request import MoveHardwareReservationRequest
from metal.types.new_password import NewPassword
from metal.types.operating_system import OperatingSystem
from metal.types.operating_system_list import OperatingSystemList
from metal.types.organization import Organization
from metal.types.organization_input import OrganizationInput
from metal.types.organization_list import OrganizationList
from metal.types.parent_block import ParentBlock
from metal.types.payment_method import PaymentMethod
from metal.types.payment_method_billing_address import PaymentMethodBillingAddress
from metal.types.payment_method_create_input import PaymentMethodCreateInput
from metal.types.payment_method_list import PaymentMethodList
from metal.types.payment_method_update_input import PaymentMethodUpdateInput
from metal.types.plan import Plan
from metal.types.plan_available_in_inner import PlanAvailableInInner
from metal.types.plan_available_in_inner_price import PlanAvailableInInnerPrice
from metal.types.plan_available_in_metros_inner import PlanAvailableInMetrosInner
from metal.types.plan_list import PlanList
from metal.types.plan_specs import PlanSpecs
from metal.types.plan_specs_cpus_inner import PlanSpecsCpusInner
from metal.types.plan_specs_drives_inner import PlanSpecsDrivesInner
from metal.types.plan_specs_features import PlanSpecsFeatures
from metal.types.plan_specs_nics_inner import PlanSpecsNicsInner
from metal.types.port import Port
from metal.types.port_assign_input import PortAssignInput
from metal.types.port_convert_layer3_input import PortConvertLayer3Input
from metal.types.port_convert_layer3_input_request_ips_inner import PortConvertLayer3InputRequestIpsInner
from metal.types.port_data import PortData
from metal.types.port_vlan_assignment import PortVlanAssignment
from metal.types.port_vlan_assignment_batch import PortVlanAssignmentBatch
from metal.types.port_vlan_assignment_batch_create_input import PortVlanAssignmentBatchCreateInput
from metal.types.port_vlan_assignment_batch_create_input_vlan_assignments_inner import PortVlanAssignmentBatchCreateInputVlanAssignmentsInner
from metal.types.port_vlan_assignment_batch_list import PortVlanAssignmentBatchList
from metal.types.port_vlan_assignment_batch_vlan_assignments_inner import PortVlanAssignmentBatchVlanAssignmentsInner
from metal.types.port_vlan_assignment_list import PortVlanAssignmentList
from metal.types.project import Project
from metal.types.project_create_from_root_input import ProjectCreateFromRootInput
from metal.types.project_create_input import ProjectCreateInput
from metal.types.project_list import ProjectList
from metal.types.project_update_input import ProjectUpdateInput
from metal.types.project_usage import ProjectUsage
from metal.types.project_usage_list import ProjectUsageList
from metal.types.recovery_code_list import RecoveryCodeList
from metal.types.request_ip_reservation201_response import RequestIPReservation201Response
from metal.types.request_ip_reservation_request import RequestIPReservationRequest
from metal.types.ssh_key import SSHKey
from metal.types.ssh_key_create_input import SSHKeyCreateInput
from metal.types.ssh_key_input import SSHKeyInput
from metal.types.ssh_key_list import SSHKeyList
from metal.types.self_service_reservation_item_request import SelfServiceReservationItemRequest
from metal.types.self_service_reservation_item_response import SelfServiceReservationItemResponse
from metal.types.self_service_reservation_list import SelfServiceReservationList
from metal.types.self_service_reservation_response import SelfServiceReservationResponse
from metal.types.server_info import ServerInfo
from metal.types.spot_market_prices_list import SpotMarketPricesList
from metal.types.spot_market_prices_per_metro_list import SpotMarketPricesPerMetroList
from metal.types.spot_market_prices_per_metro_report import SpotMarketPricesPerMetroReport
from metal.types.spot_market_request import SpotMarketRequest
from metal.types.spot_market_request_create_input import SpotMarketRequestCreateInput
from metal.types.spot_market_request_create_input_instance_attributes import SpotMarketRequestCreateInputInstanceAttributes
from metal.types.spot_market_request_list import SpotMarketRequestList
from metal.types.spot_market_request_metro import SpotMarketRequestMetro
from metal.types.spot_prices_datapoints import SpotPricesDatapoints
from metal.types.spot_prices_history_report import SpotPricesHistoryReport
from metal.types.spot_prices_per_baremetal import SpotPricesPerBaremetal
from metal.types.spot_prices_per_facility import SpotPricesPerFacility
from metal.types.spot_prices_per_new_facility import SpotPricesPerNewFacility
from metal.types.spot_prices_report import SpotPricesReport
from metal.types.support_request_input import SupportRequestInput
from metal.types.transfer_request import TransferRequest
from metal.types.transfer_request_input import TransferRequestInput
from metal.types.transfer_request_list import TransferRequestList
from metal.types.update_email_input import UpdateEmailInput
from metal.types.update_virtual_circuit_request import UpdateVirtualCircuitRequest
from metal.types.user import User
from metal.types.user_create_input import UserCreateInput
from metal.types.user_list import UserList
from metal.types.user_lite import UserLite
from metal.types.user_update_input import UserUpdateInput
from metal.types.userdata import Userdata
from metal.types.verify_email import VerifyEmail
from metal.types.virtual_circuit import VirtualCircuit
from metal.types.virtual_circuit_create_input import VirtualCircuitCreateInput
from metal.types.virtual_circuit_list import VirtualCircuitList
from metal.types.virtual_circuit_list_virtual_circuits_inner import VirtualCircuitListVirtualCircuitsInner
from metal.types.virtual_circuit_update_input import VirtualCircuitUpdateInput
from metal.types.virtual_network import VirtualNetwork
from metal.types.virtual_network_create_input import VirtualNetworkCreateInput
from metal.types.virtual_network_list import VirtualNetworkList
from metal.types.vrf import Vrf
from metal.types.vrf_create_input import VrfCreateInput
from metal.types.vrf_ip_reservation import VrfIpReservation
from metal.types.vrf_ip_reservation_create_input import VrfIpReservationCreateInput
from metal.types.vrf_ip_reservation_list import VrfIpReservationList
from metal.types.vrf_list import VrfList
from metal.types.vrf_metal_gateway import VrfMetalGateway
from metal.types.vrf_metal_gateway_create_input import VrfMetalGatewayCreateInput
from metal.types.vrf_route import VrfRoute
from metal.types.vrf_route_create_input import VrfRouteCreateInput
from metal.types.vrf_route_list import VrfRouteList
from metal.types.vrf_route_metal_gateway import VrfRouteMetalGateway
from metal.types.vrf_route_virtual_network import VrfRouteVirtualNetwork
from metal.types.vrf_route_vrf import VrfRouteVrf
from metal.types.vrf_update_input import VrfUpdateInput
from metal.types.vrf_virtual_circuit import VrfVirtualCircuit
from metal.types.vrf_virtual_circuit_create_input import VrfVirtualCircuitCreateInput
from metal.types.vrf_virtual_circuit_update_input import VrfVirtualCircuitUpdateInput

