import typing_extensions

from metal.apis.tags import TagValues
from metal.apis.tags.authentication_api import AuthenticationApi
from metal.apis.tags.errors_api import ErrorsApi
from metal.apis.tags.batches_api import BatchesApi
from metal.apis.tags.bgp_api import BGPApi
from metal.apis.tags.capacity_api import CapacityApi
from metal.apis.tags.interconnections_api import InterconnectionsApi
from metal.apis.tags.devices_api import DevicesApi
from metal.apis.tags.emails_api import EmailsApi
from metal.apis.tags.events_api import EventsApi
from metal.apis.tags.facilities_api import FacilitiesApi
from metal.apis.tags.global_bgp_ranges_api import GlobalBgpRangesApi
from metal.apis.tags.hardware_reservations_api import HardwareReservationsApi
from metal.apis.tags.incidents_api import IncidentsApi
from metal.apis.tags.invitations_api import InvitationsApi
from metal.apis.tags.ip_addresses_api import IPAddressesApi
from metal.apis.tags.licenses_api import LicensesApi
from metal.apis.tags.memberships_api import MembershipsApi
from metal.apis.tags.metadata_api import MetadataApi
from metal.apis.tags.metal_gateways_api import MetalGatewaysApi
from metal.apis.tags.metros_api import MetrosApi
from metal.apis.tags.operating_systems_api import OperatingSystemsApi
from metal.apis.tags.organizations_api import OrganizationsApi
from metal.apis.tags.otps_api import OTPsApi
from metal.apis.tags.password_reset_tokens_api import PasswordResetTokensApi
from metal.apis.tags.payment_methods_api import PaymentMethodsApi
from metal.apis.tags.plans_api import PlansApi
from metal.apis.tags.ports_api import PortsApi
from metal.apis.tags.projects_api import ProjectsApi
from metal.apis.tags.self_service_reservations_api import SelfServiceReservationsApi
from metal.apis.tags.spot_market_api import SpotMarketApi
from metal.apis.tags.ssh_keys_api import SSHKeysApi
from metal.apis.tags.support_request_api import SupportRequestApi
from metal.apis.tags.transfer_requests_api import TransferRequestsApi
from metal.apis.tags.two_factor_auth_api import TwoFactorAuthApi
from metal.apis.tags.usages_api import UsagesApi
from metal.apis.tags.userdata_api import UserdataApi
from metal.apis.tags.users_api import UsersApi
from metal.apis.tags.user_verification_tokens_api import UserVerificationTokensApi
from metal.apis.tags.vlans_api import VLANsApi
from metal.apis.tags.volumes_api import VolumesApi
from metal.apis.tags.vrfs_api import VRFsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.ERRORS: ErrorsApi,
        TagValues.BATCHES: BatchesApi,
        TagValues.BGP: BGPApi,
        TagValues.CAPACITY: CapacityApi,
        TagValues.INTERCONNECTIONS: InterconnectionsApi,
        TagValues.DEVICES: DevicesApi,
        TagValues.EMAILS: EmailsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FACILITIES: FacilitiesApi,
        TagValues.GLOBAL_BGP_RANGES: GlobalBgpRangesApi,
        TagValues.HARDWARE_RESERVATIONS: HardwareReservationsApi,
        TagValues.INCIDENTS: IncidentsApi,
        TagValues.INVITATIONS: InvitationsApi,
        TagValues.IPADDRESSES: IPAddressesApi,
        TagValues.LICENSES: LicensesApi,
        TagValues.MEMBERSHIPS: MembershipsApi,
        TagValues.METADATA: MetadataApi,
        TagValues.METAL_GATEWAYS: MetalGatewaysApi,
        TagValues.METROS: MetrosApi,
        TagValues.OPERATING_SYSTEMS: OperatingSystemsApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.OTPS: OTPsApi,
        TagValues.PASSWORD_RESET_TOKENS: PasswordResetTokensApi,
        TagValues.PAYMENT_METHODS: PaymentMethodsApi,
        TagValues.PLANS: PlansApi,
        TagValues.PORTS: PortsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.SELF_SERVICE_RESERVATIONS: SelfServiceReservationsApi,
        TagValues.SPOT_MARKET: SpotMarketApi,
        TagValues.SSHKEYS: SSHKeysApi,
        TagValues.SUPPORT_REQUEST: SupportRequestApi,
        TagValues.TRANSFER_REQUESTS: TransferRequestsApi,
        TagValues.TWO_FACTOR_AUTH: TwoFactorAuthApi,
        TagValues.USAGES: UsagesApi,
        TagValues.USERDATA: UserdataApi,
        TagValues.USERS: UsersApi,
        TagValues.USER_VERIFICATION_TOKENS: UserVerificationTokensApi,
        TagValues.VLANS: VLANsApi,
        TagValues.VOLUMES: VolumesApi,
        TagValues.VRFS: VRFsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.ERRORS: ErrorsApi,
        TagValues.BATCHES: BatchesApi,
        TagValues.BGP: BGPApi,
        TagValues.CAPACITY: CapacityApi,
        TagValues.INTERCONNECTIONS: InterconnectionsApi,
        TagValues.DEVICES: DevicesApi,
        TagValues.EMAILS: EmailsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FACILITIES: FacilitiesApi,
        TagValues.GLOBAL_BGP_RANGES: GlobalBgpRangesApi,
        TagValues.HARDWARE_RESERVATIONS: HardwareReservationsApi,
        TagValues.INCIDENTS: IncidentsApi,
        TagValues.INVITATIONS: InvitationsApi,
        TagValues.IPADDRESSES: IPAddressesApi,
        TagValues.LICENSES: LicensesApi,
        TagValues.MEMBERSHIPS: MembershipsApi,
        TagValues.METADATA: MetadataApi,
        TagValues.METAL_GATEWAYS: MetalGatewaysApi,
        TagValues.METROS: MetrosApi,
        TagValues.OPERATING_SYSTEMS: OperatingSystemsApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.OTPS: OTPsApi,
        TagValues.PASSWORD_RESET_TOKENS: PasswordResetTokensApi,
        TagValues.PAYMENT_METHODS: PaymentMethodsApi,
        TagValues.PLANS: PlansApi,
        TagValues.PORTS: PortsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.SELF_SERVICE_RESERVATIONS: SelfServiceReservationsApi,
        TagValues.SPOT_MARKET: SpotMarketApi,
        TagValues.SSHKEYS: SSHKeysApi,
        TagValues.SUPPORT_REQUEST: SupportRequestApi,
        TagValues.TRANSFER_REQUESTS: TransferRequestsApi,
        TagValues.TWO_FACTOR_AUTH: TwoFactorAuthApi,
        TagValues.USAGES: UsagesApi,
        TagValues.USERDATA: UserdataApi,
        TagValues.USERS: UsersApi,
        TagValues.USER_VERIFICATION_TOKENS: UserVerificationTokensApi,
        TagValues.VLANS: VLANsApi,
        TagValues.VOLUMES: VolumesApi,
        TagValues.VRFS: VRFsApi,
    }
)
