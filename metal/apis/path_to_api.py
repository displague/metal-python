import typing_extensions

from metal.paths import PathValues
from metal.apis.paths.api_keys_id import ApiKeysId
from metal.apis.paths.batches_id import BatchesId
from metal.apis.paths.bgp_sessions_id import BgpSessionsId
from metal.apis.paths.capacity import Capacity
from metal.apis.paths.capacity_metros import CapacityMetros
from metal.apis.paths.connections_connection_id import ConnectionsConnectionId
from metal.apis.paths.connections_connection_id_events import ConnectionsConnectionIdEvents
from metal.apis.paths.connections_connection_id_ports import ConnectionsConnectionIdPorts
from metal.apis.paths.connections_connection_id_virtual_circuits import ConnectionsConnectionIdVirtualCircuits
from metal.apis.paths.connections_connection_id_ports_id import ConnectionsConnectionIdPortsId
from metal.apis.paths.connections_connection_id_ports_id_events import ConnectionsConnectionIdPortsIdEvents
from metal.apis.paths.connections_connection_id_ports_port_id_virtual_circuits import ConnectionsConnectionIdPortsPortIdVirtualCircuits
from metal.apis.paths.devices_id import DevicesId
from metal.apis.paths.devices_id_actions import DevicesIdActions
from metal.apis.paths.devices_id_bandwidth import DevicesIdBandwidth
from metal.apis.paths.devices_id_bgp_neighbors import DevicesIdBgpNeighbors
from metal.apis.paths.devices_id_bgp_sessions import DevicesIdBgpSessions
from metal.apis.paths.devices_id_customdata import DevicesIdCustomdata
from metal.apis.paths.devices_id_events import DevicesIdEvents
from metal.apis.paths.devices_id_ips import DevicesIdIps
from metal.apis.paths.devices_id_metadata import DevicesIdMetadata
from metal.apis.paths.devices_id_ssh_keys import DevicesIdSshKeys
from metal.apis.paths.devices_id_traffic import DevicesIdTraffic
from metal.apis.paths.devices_id_usages import DevicesIdUsages
from metal.apis.paths.devices_id_userdata import DevicesIdUserdata
from metal.apis.paths.devices_instance_id_ips_id_customdata import DevicesInstanceIdIpsIdCustomdata
from metal.apis.paths.emails import Emails
from metal.apis.paths.emails_id import EmailsId
from metal.apis.paths.events import Events
from metal.apis.paths.events_id import EventsId
from metal.apis.paths.facilities import Facilities
from metal.apis.paths.hardware_reservations_id import HardwareReservationsId
from metal.apis.paths.hardware_reservations_id_activate import HardwareReservationsIdActivate
from metal.apis.paths.hardware_reservations_id_move import HardwareReservationsIdMove
from metal.apis.paths.incidents import Incidents
from metal.apis.paths.invitations import Invitations
from metal.apis.paths.invitations_id import InvitationsId
from metal.apis.paths.ips_id import IpsId
from metal.apis.paths.ips_id_available import IpsIdAvailable
from metal.apis.paths.ips_id_customdata import IpsIdCustomdata
from metal.apis.paths.licenses_id import LicensesId
from metal.apis.paths.locations_metros import LocationsMetros
from metal.apis.paths.locations_metros_id import LocationsMetrosId
from metal.apis.paths.market_spot_prices import MarketSpotPrices
from metal.apis.paths.market_spot_prices_history import MarketSpotPricesHistory
from metal.apis.paths.market_spot_prices_metros import MarketSpotPricesMetros
from metal.apis.paths.memberships_id import MembershipsId
from metal.apis.paths.metal_gateways_id import MetalGatewaysId
from metal.apis.paths.operating_system_versions import OperatingSystemVersions
from metal.apis.paths.operating_systems import OperatingSystems
from metal.apis.paths.organizations import Organizations
from metal.apis.paths.organizations_id import OrganizationsId
from metal.apis.paths.organizations_id_capacity import OrganizationsIdCapacity
from metal.apis.paths.organizations_id_capacity_metros import OrganizationsIdCapacityMetros
from metal.apis.paths.organizations_id_customdata import OrganizationsIdCustomdata
from metal.apis.paths.organizations_id_devices import OrganizationsIdDevices
from metal.apis.paths.organizations_id_events import OrganizationsIdEvents
from metal.apis.paths.organizations_id_facilities import OrganizationsIdFacilities
from metal.apis.paths.organizations_id_invitations import OrganizationsIdInvitations
from metal.apis.paths.organizations_id_operating_systems import OrganizationsIdOperatingSystems
from metal.apis.paths.organizations_id_payment_methods import OrganizationsIdPaymentMethods
from metal.apis.paths.organizations_id_plans import OrganizationsIdPlans
from metal.apis.paths.organizations_id_projects import OrganizationsIdProjects
from metal.apis.paths.organizations_id_transfers import OrganizationsIdTransfers
from metal.apis.paths.organizations_organization_id_connections import OrganizationsOrganizationIdConnections
from metal.apis.paths.payment_methods_id import PaymentMethodsId
from metal.apis.paths.plans import Plans
from metal.apis.paths.ports_id import PortsId
from metal.apis.paths.ports_id_assign import PortsIdAssign
from metal.apis.paths.ports_id_bond import PortsIdBond
from metal.apis.paths.ports_id_convert_layer_2 import PortsIdConvertLayer2
from metal.apis.paths.ports_id_convert_layer_3 import PortsIdConvertLayer3
from metal.apis.paths.ports_id_disbond import PortsIdDisbond
from metal.apis.paths.ports_id_native_vlan import PortsIdNativeVlan
from metal.apis.paths.ports_id_unassign import PortsIdUnassign
from metal.apis.paths.ports_id_vlan_assignments import PortsIdVlanAssignments
from metal.apis.paths.ports_id_vlan_assignments_assignment_id import PortsIdVlanAssignmentsAssignmentId
from metal.apis.paths.ports_id_vlan_assignments_batches import PortsIdVlanAssignmentsBatches
from metal.apis.paths.ports_id_vlan_assignments_batches_batch_id import PortsIdVlanAssignmentsBatchesBatchId
from metal.apis.paths.projects import Projects
from metal.apis.paths.projects_id import ProjectsId
from metal.apis.paths.projects_id_api_keys import ProjectsIdApiKeys
from metal.apis.paths.projects_id_batches import ProjectsIdBatches
from metal.apis.paths.projects_id_bgp_config import ProjectsIdBgpConfig
from metal.apis.paths.projects_id_bgp_configs import ProjectsIdBgpConfigs
from metal.apis.paths.projects_id_bgp_sessions import ProjectsIdBgpSessions
from metal.apis.paths.projects_id_customdata import ProjectsIdCustomdata
from metal.apis.paths.projects_id_devices import ProjectsIdDevices
from metal.apis.paths.projects_id_devices_batch import ProjectsIdDevicesBatch
from metal.apis.paths.projects_id_events import ProjectsIdEvents
from metal.apis.paths.projects_id_facilities import ProjectsIdFacilities
from metal.apis.paths.projects_id_global_bgp_ranges import ProjectsIdGlobalBgpRanges
from metal.apis.paths.projects_id_hardware_reservations import ProjectsIdHardwareReservations
from metal.apis.paths.projects_id_ips import ProjectsIdIps
from metal.apis.paths.projects_id_licenses import ProjectsIdLicenses
from metal.apis.paths.projects_id_plans import ProjectsIdPlans
from metal.apis.paths.projects_id_spot_market_requests import ProjectsIdSpotMarketRequests
from metal.apis.paths.projects_id_ssh_keys import ProjectsIdSshKeys
from metal.apis.paths.projects_id_transfers import ProjectsIdTransfers
from metal.apis.paths.projects_id_usages import ProjectsIdUsages
from metal.apis.paths.projects_id_virtual_networks import ProjectsIdVirtualNetworks
from metal.apis.paths.projects_id_vrfs import ProjectsIdVrfs
from metal.apis.paths.projects_project_id_connections import ProjectsProjectIdConnections
from metal.apis.paths.projects_project_id_invitations import ProjectsProjectIdInvitations
from metal.apis.paths.projects_project_id_ips_id_customdata import ProjectsProjectIdIpsIdCustomdata
from metal.apis.paths.projects_project_id_memberships import ProjectsProjectIdMemberships
from metal.apis.paths.projects_project_id_metal_gateways import ProjectsProjectIdMetalGateways
from metal.apis.paths.projects_project_id_self_service_reservations import ProjectsProjectIdSelfServiceReservations
from metal.apis.paths.projects_project_id_self_service_reservations_id import ProjectsProjectIdSelfServiceReservationsId
from metal.apis.paths.reset_password import ResetPassword
from metal.apis.paths.routes_id import RoutesId
from metal.apis.paths.spot_market_requests_id import SpotMarketRequestsId
from metal.apis.paths.ssh_keys import SshKeys
from metal.apis.paths.ssh_keys_id import SshKeysId
from metal.apis.paths.support_requests import SupportRequests
from metal.apis.paths.transfers_id import TransfersId
from metal.apis.paths.user import User
from metal.apis.paths.user_api_keys import UserApiKeys
from metal.apis.paths.user_api_keys_id import UserApiKeysId
from metal.apis.paths.user_otp_app import UserOtpApp
from metal.apis.paths.user_otp_recovery_codes import UserOtpRecoveryCodes
from metal.apis.paths.user_otp_sms import UserOtpSms
from metal.apis.paths.user_otp_sms_receive import UserOtpSmsReceive
from metal.apis.paths.user_otp_verify_otp import UserOtpVerifyOtp
from metal.apis.paths.userdata_validate import UserdataValidate
from metal.apis.paths.users import Users
from metal.apis.paths.users_id import UsersId
from metal.apis.paths.users_id_customdata import UsersIdCustomdata
from metal.apis.paths.verify_email import VerifyEmail
from metal.apis.paths.virtual_circuits_id_events import VirtualCircuitsIdEvents
from metal.apis.paths.virtual_circuits_id import VirtualCircuitsId
from metal.apis.paths.virtual_networks_id import VirtualNetworksId
from metal.apis.paths.vrfs_id import VrfsId
from metal.apis.paths.vrfs_id_ips import VrfsIdIps
from metal.apis.paths.vrfs_vrf_id_ips_id import VrfsVrfIdIpsId
from metal.apis.paths.vrfs_id_routes import VrfsIdRoutes

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.APIKEYS_ID: ApiKeysId,
        PathValues.BATCHES_ID: BatchesId,
        PathValues.BGP_SESSIONS_ID: BgpSessionsId,
        PathValues.CAPACITY: Capacity,
        PathValues.CAPACITY_METROS: CapacityMetros,
        PathValues.CONNECTIONS_CONNECTION_ID: ConnectionsConnectionId,
        PathValues.CONNECTIONS_CONNECTION_ID_EVENTS: ConnectionsConnectionIdEvents,
        PathValues.CONNECTIONS_CONNECTION_ID_PORTS: ConnectionsConnectionIdPorts,
        PathValues.CONNECTIONS_CONNECTION_ID_VIRTUALCIRCUITS: ConnectionsConnectionIdVirtualCircuits,
        PathValues.CONNECTIONS_CONNECTION_ID_PORTS_ID: ConnectionsConnectionIdPortsId,
        PathValues.CONNECTIONS_CONNECTION_ID_PORTS_ID_EVENTS: ConnectionsConnectionIdPortsIdEvents,
        PathValues.CONNECTIONS_CONNECTION_ID_PORTS_PORT_ID_VIRTUALCIRCUITS: ConnectionsConnectionIdPortsPortIdVirtualCircuits,
        PathValues.DEVICES_ID: DevicesId,
        PathValues.DEVICES_ID_ACTIONS: DevicesIdActions,
        PathValues.DEVICES_ID_BANDWIDTH: DevicesIdBandwidth,
        PathValues.DEVICES_ID_BGP_NEIGHBORS: DevicesIdBgpNeighbors,
        PathValues.DEVICES_ID_BGP_SESSIONS: DevicesIdBgpSessions,
        PathValues.DEVICES_ID_CUSTOMDATA: DevicesIdCustomdata,
        PathValues.DEVICES_ID_EVENTS: DevicesIdEvents,
        PathValues.DEVICES_ID_IPS: DevicesIdIps,
        PathValues.DEVICES_ID_METADATA: DevicesIdMetadata,
        PathValues.DEVICES_ID_SSHKEYS: DevicesIdSshKeys,
        PathValues.DEVICES_ID_TRAFFIC: DevicesIdTraffic,
        PathValues.DEVICES_ID_USAGES: DevicesIdUsages,
        PathValues.DEVICES_ID_USERDATA: DevicesIdUserdata,
        PathValues.DEVICES_INSTANCE_ID_IPS_ID_CUSTOMDATA: DevicesInstanceIdIpsIdCustomdata,
        PathValues.EMAILS: Emails,
        PathValues.EMAILS_ID: EmailsId,
        PathValues.EVENTS: Events,
        PathValues.EVENTS_ID: EventsId,
        PathValues.FACILITIES: Facilities,
        PathValues.HARDWARERESERVATIONS_ID: HardwareReservationsId,
        PathValues.HARDWARERESERVATIONS_ID_ACTIVATE: HardwareReservationsIdActivate,
        PathValues.HARDWARERESERVATIONS_ID_MOVE: HardwareReservationsIdMove,
        PathValues.INCIDENTS: Incidents,
        PathValues.INVITATIONS: Invitations,
        PathValues.INVITATIONS_ID: InvitationsId,
        PathValues.IPS_ID: IpsId,
        PathValues.IPS_ID_AVAILABLE: IpsIdAvailable,
        PathValues.IPS_ID_CUSTOMDATA: IpsIdCustomdata,
        PathValues.LICENSES_ID: LicensesId,
        PathValues.LOCATIONS_METROS: LocationsMetros,
        PathValues.LOCATIONS_METROS_ID: LocationsMetrosId,
        PathValues.MARKET_SPOT_PRICES: MarketSpotPrices,
        PathValues.MARKET_SPOT_PRICES_HISTORY: MarketSpotPricesHistory,
        PathValues.MARKET_SPOT_PRICES_METROS: MarketSpotPricesMetros,
        PathValues.MEMBERSHIPS_ID: MembershipsId,
        PathValues.METALGATEWAYS_ID: MetalGatewaysId,
        PathValues.OPERATINGSYSTEMVERSIONS: OperatingSystemVersions,
        PathValues.OPERATINGSYSTEMS: OperatingSystems,
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.ORGANIZATIONS_ID: OrganizationsId,
        PathValues.ORGANIZATIONS_ID_CAPACITY: OrganizationsIdCapacity,
        PathValues.ORGANIZATIONS_ID_CAPACITY_METROS: OrganizationsIdCapacityMetros,
        PathValues.ORGANIZATIONS_ID_CUSTOMDATA: OrganizationsIdCustomdata,
        PathValues.ORGANIZATIONS_ID_DEVICES: OrganizationsIdDevices,
        PathValues.ORGANIZATIONS_ID_EVENTS: OrganizationsIdEvents,
        PathValues.ORGANIZATIONS_ID_FACILITIES: OrganizationsIdFacilities,
        PathValues.ORGANIZATIONS_ID_INVITATIONS: OrganizationsIdInvitations,
        PathValues.ORGANIZATIONS_ID_OPERATINGSYSTEMS: OrganizationsIdOperatingSystems,
        PathValues.ORGANIZATIONS_ID_PAYMENTMETHODS: OrganizationsIdPaymentMethods,
        PathValues.ORGANIZATIONS_ID_PLANS: OrganizationsIdPlans,
        PathValues.ORGANIZATIONS_ID_PROJECTS: OrganizationsIdProjects,
        PathValues.ORGANIZATIONS_ID_TRANSFERS: OrganizationsIdTransfers,
        PathValues.ORGANIZATIONS_ORGANIZATION_ID_CONNECTIONS: OrganizationsOrganizationIdConnections,
        PathValues.PAYMENTMETHODS_ID: PaymentMethodsId,
        PathValues.PLANS: Plans,
        PathValues.PORTS_ID: PortsId,
        PathValues.PORTS_ID_ASSIGN: PortsIdAssign,
        PathValues.PORTS_ID_BOND: PortsIdBond,
        PathValues.PORTS_ID_CONVERT_LAYER2: PortsIdConvertLayer2,
        PathValues.PORTS_ID_CONVERT_LAYER3: PortsIdConvertLayer3,
        PathValues.PORTS_ID_DISBOND: PortsIdDisbond,
        PathValues.PORTS_ID_NATIVEVLAN: PortsIdNativeVlan,
        PathValues.PORTS_ID_UNASSIGN: PortsIdUnassign,
        PathValues.PORTS_ID_VLANASSIGNMENTS: PortsIdVlanAssignments,
        PathValues.PORTS_ID_VLANASSIGNMENTS_ASSIGNMENT_ID: PortsIdVlanAssignmentsAssignmentId,
        PathValues.PORTS_ID_VLANASSIGNMENTS_BATCHES: PortsIdVlanAssignmentsBatches,
        PathValues.PORTS_ID_VLANASSIGNMENTS_BATCHES_BATCH_ID: PortsIdVlanAssignmentsBatchesBatchId,
        PathValues.PROJECTS: Projects,
        PathValues.PROJECTS_ID: ProjectsId,
        PathValues.PROJECTS_ID_APIKEYS: ProjectsIdApiKeys,
        PathValues.PROJECTS_ID_BATCHES: ProjectsIdBatches,
        PathValues.PROJECTS_ID_BGPCONFIG: ProjectsIdBgpConfig,
        PathValues.PROJECTS_ID_BGPCONFIGS: ProjectsIdBgpConfigs,
        PathValues.PROJECTS_ID_BGP_SESSIONS: ProjectsIdBgpSessions,
        PathValues.PROJECTS_ID_CUSTOMDATA: ProjectsIdCustomdata,
        PathValues.PROJECTS_ID_DEVICES: ProjectsIdDevices,
        PathValues.PROJECTS_ID_DEVICES_BATCH: ProjectsIdDevicesBatch,
        PathValues.PROJECTS_ID_EVENTS: ProjectsIdEvents,
        PathValues.PROJECTS_ID_FACILITIES: ProjectsIdFacilities,
        PathValues.PROJECTS_ID_GLOBALBGPRANGES: ProjectsIdGlobalBgpRanges,
        PathValues.PROJECTS_ID_HARDWARERESERVATIONS: ProjectsIdHardwareReservations,
        PathValues.PROJECTS_ID_IPS: ProjectsIdIps,
        PathValues.PROJECTS_ID_LICENSES: ProjectsIdLicenses,
        PathValues.PROJECTS_ID_PLANS: ProjectsIdPlans,
        PathValues.PROJECTS_ID_SPOTMARKETREQUESTS: ProjectsIdSpotMarketRequests,
        PathValues.PROJECTS_ID_SSHKEYS: ProjectsIdSshKeys,
        PathValues.PROJECTS_ID_TRANSFERS: ProjectsIdTransfers,
        PathValues.PROJECTS_ID_USAGES: ProjectsIdUsages,
        PathValues.PROJECTS_ID_VIRTUALNETWORKS: ProjectsIdVirtualNetworks,
        PathValues.PROJECTS_ID_VRFS: ProjectsIdVrfs,
        PathValues.PROJECTS_PROJECT_ID_CONNECTIONS: ProjectsProjectIdConnections,
        PathValues.PROJECTS_PROJECT_ID_INVITATIONS: ProjectsProjectIdInvitations,
        PathValues.PROJECTS_PROJECT_ID_IPS_ID_CUSTOMDATA: ProjectsProjectIdIpsIdCustomdata,
        PathValues.PROJECTS_PROJECT_ID_MEMBERSHIPS: ProjectsProjectIdMemberships,
        PathValues.PROJECTS_PROJECT_ID_METALGATEWAYS: ProjectsProjectIdMetalGateways,
        PathValues.PROJECTS_PROJECT_ID_SELFSERVICE_RESERVATIONS: ProjectsProjectIdSelfServiceReservations,
        PathValues.PROJECTS_PROJECT_ID_SELFSERVICE_RESERVATIONS_ID: ProjectsProjectIdSelfServiceReservationsId,
        PathValues.RESETPASSWORD: ResetPassword,
        PathValues.ROUTES_ID: RoutesId,
        PathValues.SPOTMARKETREQUESTS_ID: SpotMarketRequestsId,
        PathValues.SSHKEYS: SshKeys,
        PathValues.SSHKEYS_ID: SshKeysId,
        PathValues.SUPPORTREQUESTS: SupportRequests,
        PathValues.TRANSFERS_ID: TransfersId,
        PathValues.USER: User,
        PathValues.USER_APIKEYS: UserApiKeys,
        PathValues.USER_APIKEYS_ID: UserApiKeysId,
        PathValues.USER_OTP_APP: UserOtpApp,
        PathValues.USER_OTP_RECOVERYCODES: UserOtpRecoveryCodes,
        PathValues.USER_OTP_SMS: UserOtpSms,
        PathValues.USER_OTP_SMS_RECEIVE: UserOtpSmsReceive,
        PathValues.USER_OTP_VERIFY_OTP: UserOtpVerifyOtp,
        PathValues.USERDATA_VALIDATE: UserdataValidate,
        PathValues.USERS: Users,
        PathValues.USERS_ID: UsersId,
        PathValues.USERS_ID_CUSTOMDATA: UsersIdCustomdata,
        PathValues.VERIFYEMAIL: VerifyEmail,
        PathValues.VIRTUALCIRCUITS_ID_EVENTS: VirtualCircuitsIdEvents,
        PathValues.VIRTUALCIRCUITS_ID: VirtualCircuitsId,
        PathValues.VIRTUALNETWORKS_ID: VirtualNetworksId,
        PathValues.VRFS_ID: VrfsId,
        PathValues.VRFS_ID_IPS: VrfsIdIps,
        PathValues.VRFS_VRF_ID_IPS_ID: VrfsVrfIdIpsId,
        PathValues.VRFS_ID_ROUTES: VrfsIdRoutes,
    }
)

path_to_api = PathToApi(
    {
        PathValues.APIKEYS_ID: ApiKeysId,
        PathValues.BATCHES_ID: BatchesId,
        PathValues.BGP_SESSIONS_ID: BgpSessionsId,
        PathValues.CAPACITY: Capacity,
        PathValues.CAPACITY_METROS: CapacityMetros,
        PathValues.CONNECTIONS_CONNECTION_ID: ConnectionsConnectionId,
        PathValues.CONNECTIONS_CONNECTION_ID_EVENTS: ConnectionsConnectionIdEvents,
        PathValues.CONNECTIONS_CONNECTION_ID_PORTS: ConnectionsConnectionIdPorts,
        PathValues.CONNECTIONS_CONNECTION_ID_VIRTUALCIRCUITS: ConnectionsConnectionIdVirtualCircuits,
        PathValues.CONNECTIONS_CONNECTION_ID_PORTS_ID: ConnectionsConnectionIdPortsId,
        PathValues.CONNECTIONS_CONNECTION_ID_PORTS_ID_EVENTS: ConnectionsConnectionIdPortsIdEvents,
        PathValues.CONNECTIONS_CONNECTION_ID_PORTS_PORT_ID_VIRTUALCIRCUITS: ConnectionsConnectionIdPortsPortIdVirtualCircuits,
        PathValues.DEVICES_ID: DevicesId,
        PathValues.DEVICES_ID_ACTIONS: DevicesIdActions,
        PathValues.DEVICES_ID_BANDWIDTH: DevicesIdBandwidth,
        PathValues.DEVICES_ID_BGP_NEIGHBORS: DevicesIdBgpNeighbors,
        PathValues.DEVICES_ID_BGP_SESSIONS: DevicesIdBgpSessions,
        PathValues.DEVICES_ID_CUSTOMDATA: DevicesIdCustomdata,
        PathValues.DEVICES_ID_EVENTS: DevicesIdEvents,
        PathValues.DEVICES_ID_IPS: DevicesIdIps,
        PathValues.DEVICES_ID_METADATA: DevicesIdMetadata,
        PathValues.DEVICES_ID_SSHKEYS: DevicesIdSshKeys,
        PathValues.DEVICES_ID_TRAFFIC: DevicesIdTraffic,
        PathValues.DEVICES_ID_USAGES: DevicesIdUsages,
        PathValues.DEVICES_ID_USERDATA: DevicesIdUserdata,
        PathValues.DEVICES_INSTANCE_ID_IPS_ID_CUSTOMDATA: DevicesInstanceIdIpsIdCustomdata,
        PathValues.EMAILS: Emails,
        PathValues.EMAILS_ID: EmailsId,
        PathValues.EVENTS: Events,
        PathValues.EVENTS_ID: EventsId,
        PathValues.FACILITIES: Facilities,
        PathValues.HARDWARERESERVATIONS_ID: HardwareReservationsId,
        PathValues.HARDWARERESERVATIONS_ID_ACTIVATE: HardwareReservationsIdActivate,
        PathValues.HARDWARERESERVATIONS_ID_MOVE: HardwareReservationsIdMove,
        PathValues.INCIDENTS: Incidents,
        PathValues.INVITATIONS: Invitations,
        PathValues.INVITATIONS_ID: InvitationsId,
        PathValues.IPS_ID: IpsId,
        PathValues.IPS_ID_AVAILABLE: IpsIdAvailable,
        PathValues.IPS_ID_CUSTOMDATA: IpsIdCustomdata,
        PathValues.LICENSES_ID: LicensesId,
        PathValues.LOCATIONS_METROS: LocationsMetros,
        PathValues.LOCATIONS_METROS_ID: LocationsMetrosId,
        PathValues.MARKET_SPOT_PRICES: MarketSpotPrices,
        PathValues.MARKET_SPOT_PRICES_HISTORY: MarketSpotPricesHistory,
        PathValues.MARKET_SPOT_PRICES_METROS: MarketSpotPricesMetros,
        PathValues.MEMBERSHIPS_ID: MembershipsId,
        PathValues.METALGATEWAYS_ID: MetalGatewaysId,
        PathValues.OPERATINGSYSTEMVERSIONS: OperatingSystemVersions,
        PathValues.OPERATINGSYSTEMS: OperatingSystems,
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.ORGANIZATIONS_ID: OrganizationsId,
        PathValues.ORGANIZATIONS_ID_CAPACITY: OrganizationsIdCapacity,
        PathValues.ORGANIZATIONS_ID_CAPACITY_METROS: OrganizationsIdCapacityMetros,
        PathValues.ORGANIZATIONS_ID_CUSTOMDATA: OrganizationsIdCustomdata,
        PathValues.ORGANIZATIONS_ID_DEVICES: OrganizationsIdDevices,
        PathValues.ORGANIZATIONS_ID_EVENTS: OrganizationsIdEvents,
        PathValues.ORGANIZATIONS_ID_FACILITIES: OrganizationsIdFacilities,
        PathValues.ORGANIZATIONS_ID_INVITATIONS: OrganizationsIdInvitations,
        PathValues.ORGANIZATIONS_ID_OPERATINGSYSTEMS: OrganizationsIdOperatingSystems,
        PathValues.ORGANIZATIONS_ID_PAYMENTMETHODS: OrganizationsIdPaymentMethods,
        PathValues.ORGANIZATIONS_ID_PLANS: OrganizationsIdPlans,
        PathValues.ORGANIZATIONS_ID_PROJECTS: OrganizationsIdProjects,
        PathValues.ORGANIZATIONS_ID_TRANSFERS: OrganizationsIdTransfers,
        PathValues.ORGANIZATIONS_ORGANIZATION_ID_CONNECTIONS: OrganizationsOrganizationIdConnections,
        PathValues.PAYMENTMETHODS_ID: PaymentMethodsId,
        PathValues.PLANS: Plans,
        PathValues.PORTS_ID: PortsId,
        PathValues.PORTS_ID_ASSIGN: PortsIdAssign,
        PathValues.PORTS_ID_BOND: PortsIdBond,
        PathValues.PORTS_ID_CONVERT_LAYER2: PortsIdConvertLayer2,
        PathValues.PORTS_ID_CONVERT_LAYER3: PortsIdConvertLayer3,
        PathValues.PORTS_ID_DISBOND: PortsIdDisbond,
        PathValues.PORTS_ID_NATIVEVLAN: PortsIdNativeVlan,
        PathValues.PORTS_ID_UNASSIGN: PortsIdUnassign,
        PathValues.PORTS_ID_VLANASSIGNMENTS: PortsIdVlanAssignments,
        PathValues.PORTS_ID_VLANASSIGNMENTS_ASSIGNMENT_ID: PortsIdVlanAssignmentsAssignmentId,
        PathValues.PORTS_ID_VLANASSIGNMENTS_BATCHES: PortsIdVlanAssignmentsBatches,
        PathValues.PORTS_ID_VLANASSIGNMENTS_BATCHES_BATCH_ID: PortsIdVlanAssignmentsBatchesBatchId,
        PathValues.PROJECTS: Projects,
        PathValues.PROJECTS_ID: ProjectsId,
        PathValues.PROJECTS_ID_APIKEYS: ProjectsIdApiKeys,
        PathValues.PROJECTS_ID_BATCHES: ProjectsIdBatches,
        PathValues.PROJECTS_ID_BGPCONFIG: ProjectsIdBgpConfig,
        PathValues.PROJECTS_ID_BGPCONFIGS: ProjectsIdBgpConfigs,
        PathValues.PROJECTS_ID_BGP_SESSIONS: ProjectsIdBgpSessions,
        PathValues.PROJECTS_ID_CUSTOMDATA: ProjectsIdCustomdata,
        PathValues.PROJECTS_ID_DEVICES: ProjectsIdDevices,
        PathValues.PROJECTS_ID_DEVICES_BATCH: ProjectsIdDevicesBatch,
        PathValues.PROJECTS_ID_EVENTS: ProjectsIdEvents,
        PathValues.PROJECTS_ID_FACILITIES: ProjectsIdFacilities,
        PathValues.PROJECTS_ID_GLOBALBGPRANGES: ProjectsIdGlobalBgpRanges,
        PathValues.PROJECTS_ID_HARDWARERESERVATIONS: ProjectsIdHardwareReservations,
        PathValues.PROJECTS_ID_IPS: ProjectsIdIps,
        PathValues.PROJECTS_ID_LICENSES: ProjectsIdLicenses,
        PathValues.PROJECTS_ID_PLANS: ProjectsIdPlans,
        PathValues.PROJECTS_ID_SPOTMARKETREQUESTS: ProjectsIdSpotMarketRequests,
        PathValues.PROJECTS_ID_SSHKEYS: ProjectsIdSshKeys,
        PathValues.PROJECTS_ID_TRANSFERS: ProjectsIdTransfers,
        PathValues.PROJECTS_ID_USAGES: ProjectsIdUsages,
        PathValues.PROJECTS_ID_VIRTUALNETWORKS: ProjectsIdVirtualNetworks,
        PathValues.PROJECTS_ID_VRFS: ProjectsIdVrfs,
        PathValues.PROJECTS_PROJECT_ID_CONNECTIONS: ProjectsProjectIdConnections,
        PathValues.PROJECTS_PROJECT_ID_INVITATIONS: ProjectsProjectIdInvitations,
        PathValues.PROJECTS_PROJECT_ID_IPS_ID_CUSTOMDATA: ProjectsProjectIdIpsIdCustomdata,
        PathValues.PROJECTS_PROJECT_ID_MEMBERSHIPS: ProjectsProjectIdMemberships,
        PathValues.PROJECTS_PROJECT_ID_METALGATEWAYS: ProjectsProjectIdMetalGateways,
        PathValues.PROJECTS_PROJECT_ID_SELFSERVICE_RESERVATIONS: ProjectsProjectIdSelfServiceReservations,
        PathValues.PROJECTS_PROJECT_ID_SELFSERVICE_RESERVATIONS_ID: ProjectsProjectIdSelfServiceReservationsId,
        PathValues.RESETPASSWORD: ResetPassword,
        PathValues.ROUTES_ID: RoutesId,
        PathValues.SPOTMARKETREQUESTS_ID: SpotMarketRequestsId,
        PathValues.SSHKEYS: SshKeys,
        PathValues.SSHKEYS_ID: SshKeysId,
        PathValues.SUPPORTREQUESTS: SupportRequests,
        PathValues.TRANSFERS_ID: TransfersId,
        PathValues.USER: User,
        PathValues.USER_APIKEYS: UserApiKeys,
        PathValues.USER_APIKEYS_ID: UserApiKeysId,
        PathValues.USER_OTP_APP: UserOtpApp,
        PathValues.USER_OTP_RECOVERYCODES: UserOtpRecoveryCodes,
        PathValues.USER_OTP_SMS: UserOtpSms,
        PathValues.USER_OTP_SMS_RECEIVE: UserOtpSmsReceive,
        PathValues.USER_OTP_VERIFY_OTP: UserOtpVerifyOtp,
        PathValues.USERDATA_VALIDATE: UserdataValidate,
        PathValues.USERS: Users,
        PathValues.USERS_ID: UsersId,
        PathValues.USERS_ID_CUSTOMDATA: UsersIdCustomdata,
        PathValues.VERIFYEMAIL: VerifyEmail,
        PathValues.VIRTUALCIRCUITS_ID_EVENTS: VirtualCircuitsIdEvents,
        PathValues.VIRTUALCIRCUITS_ID: VirtualCircuitsId,
        PathValues.VIRTUALNETWORKS_ID: VirtualNetworksId,
        PathValues.VRFS_ID: VrfsId,
        PathValues.VRFS_ID_IPS: VrfsIdIps,
        PathValues.VRFS_VRF_ID_IPS_ID: VrfsVrfIdIpsId,
        PathValues.VRFS_ID_ROUTES: VrfsIdRoutes,
    }
)
