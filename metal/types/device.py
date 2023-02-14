# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal.types.device_actions_inner import DeviceActionsInner
from metal.types.device_created_by import DeviceCreatedBy
from metal.types.device_metro import DeviceMetro
from metal.types.device_project import DeviceProject
from metal.types.device_project_lite import DeviceProjectLite
from metal.types.event import Event
from metal.types.facility import Facility
from metal.types.href import Href
from metal.types.ip_assignment import IPAssignment
from metal.types.operating_system import OperatingSystem
from metal.types.plan import Plan
from metal.types.port import Port
from metal import util


class Device(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, always_pxe: bool=None, billing_cycle: str=None, bonding_mode: int=None, created_at: datetime=None, created_by: DeviceCreatedBy=None, customdata: Dict[str, object]=None, description: str=None, facility: Facility=None, hardware_reservation: Href=None, hostname: str=None, href: str=None, id: str=None, image_url: str=None, ip_addresses: List[IPAssignment]=None, ipxe_script_url: str=None, iqn: str=None, locked: bool=None, metro: DeviceMetro=None, network_ports: List[Port]=None, operating_system: OperatingSystem=None, actions: List[DeviceActionsInner]=None, plan: Plan=None, project: DeviceProject=None, project_lite: DeviceProjectLite=None, provisioning_events: List[Event]=None, provisioning_percentage: float=None, root_password: str=None, short_id: str=None, spot_instance: bool=None, spot_price_max: float=None, ssh_keys: List[Href]=None, state: str=None, switch_uuid: str=None, tags: List[str]=None, termination_time: datetime=None, updated_at: datetime=None, user: str=None, userdata: str=None, volumes: List[Href]=None):
        """Device - a model defined in OpenAPI

        :param always_pxe: The always_pxe of this Device.
        :param billing_cycle: The billing_cycle of this Device.
        :param bonding_mode: The bonding_mode of this Device.
        :param created_at: The created_at of this Device.
        :param created_by: The created_by of this Device.
        :param customdata: The customdata of this Device.
        :param description: The description of this Device.
        :param facility: The facility of this Device.
        :param hardware_reservation: The hardware_reservation of this Device.
        :param hostname: The hostname of this Device.
        :param href: The href of this Device.
        :param id: The id of this Device.
        :param image_url: The image_url of this Device.
        :param ip_addresses: The ip_addresses of this Device.
        :param ipxe_script_url: The ipxe_script_url of this Device.
        :param iqn: The iqn of this Device.
        :param locked: The locked of this Device.
        :param metro: The metro of this Device.
        :param network_ports: The network_ports of this Device.
        :param operating_system: The operating_system of this Device.
        :param actions: The actions of this Device.
        :param plan: The plan of this Device.
        :param project: The project of this Device.
        :param project_lite: The project_lite of this Device.
        :param provisioning_events: The provisioning_events of this Device.
        :param provisioning_percentage: The provisioning_percentage of this Device.
        :param root_password: The root_password of this Device.
        :param short_id: The short_id of this Device.
        :param spot_instance: The spot_instance of this Device.
        :param spot_price_max: The spot_price_max of this Device.
        :param ssh_keys: The ssh_keys of this Device.
        :param state: The state of this Device.
        :param switch_uuid: The switch_uuid of this Device.
        :param tags: The tags of this Device.
        :param termination_time: The termination_time of this Device.
        :param updated_at: The updated_at of this Device.
        :param user: The user of this Device.
        :param userdata: The userdata of this Device.
        :param volumes: The volumes of this Device.
        """
        self.openapi_types = {
            'always_pxe': bool,
            'billing_cycle': str,
            'bonding_mode': int,
            'created_at': datetime,
            'created_by': DeviceCreatedBy,
            'customdata': Dict[str, object],
            'description': str,
            'facility': Facility,
            'hardware_reservation': Href,
            'hostname': str,
            'href': str,
            'id': str,
            'image_url': str,
            'ip_addresses': List[IPAssignment],
            'ipxe_script_url': str,
            'iqn': str,
            'locked': bool,
            'metro': DeviceMetro,
            'network_ports': List[Port],
            'operating_system': OperatingSystem,
            'actions': List[DeviceActionsInner],
            'plan': Plan,
            'project': DeviceProject,
            'project_lite': DeviceProjectLite,
            'provisioning_events': List[Event],
            'provisioning_percentage': float,
            'root_password': str,
            'short_id': str,
            'spot_instance': bool,
            'spot_price_max': float,
            'ssh_keys': List[Href],
            'state': str,
            'switch_uuid': str,
            'tags': List[str],
            'termination_time': datetime,
            'updated_at': datetime,
            'user': str,
            'userdata': str,
            'volumes': List[Href]
        }

        self.attribute_map = {
            'always_pxe': 'always_pxe',
            'billing_cycle': 'billing_cycle',
            'bonding_mode': 'bonding_mode',
            'created_at': 'created_at',
            'created_by': 'created_by',
            'customdata': 'customdata',
            'description': 'description',
            'facility': 'facility',
            'hardware_reservation': 'hardware_reservation',
            'hostname': 'hostname',
            'href': 'href',
            'id': 'id',
            'image_url': 'image_url',
            'ip_addresses': 'ip_addresses',
            'ipxe_script_url': 'ipxe_script_url',
            'iqn': 'iqn',
            'locked': 'locked',
            'metro': 'metro',
            'network_ports': 'network_ports',
            'operating_system': 'operating_system',
            'actions': 'actions',
            'plan': 'plan',
            'project': 'project',
            'project_lite': 'project_lite',
            'provisioning_events': 'provisioning_events',
            'provisioning_percentage': 'provisioning_percentage',
            'root_password': 'root_password',
            'short_id': 'short_id',
            'spot_instance': 'spot_instance',
            'spot_price_max': 'spot_price_max',
            'ssh_keys': 'ssh_keys',
            'state': 'state',
            'switch_uuid': 'switch_uuid',
            'tags': 'tags',
            'termination_time': 'termination_time',
            'updated_at': 'updated_at',
            'user': 'user',
            'userdata': 'userdata',
            'volumes': 'volumes'
        }

        self._always_pxe = always_pxe
        self._billing_cycle = billing_cycle
        self._bonding_mode = bonding_mode
        self._created_at = created_at
        self._created_by = created_by
        self._customdata = customdata
        self._description = description
        self._facility = facility
        self._hardware_reservation = hardware_reservation
        self._hostname = hostname
        self._href = href
        self._id = id
        self._image_url = image_url
        self._ip_addresses = ip_addresses
        self._ipxe_script_url = ipxe_script_url
        self._iqn = iqn
        self._locked = locked
        self._metro = metro
        self._network_ports = network_ports
        self._operating_system = operating_system
        self._actions = actions
        self._plan = plan
        self._project = project
        self._project_lite = project_lite
        self._provisioning_events = provisioning_events
        self._provisioning_percentage = provisioning_percentage
        self._root_password = root_password
        self._short_id = short_id
        self._spot_instance = spot_instance
        self._spot_price_max = spot_price_max
        self._ssh_keys = ssh_keys
        self._state = state
        self._switch_uuid = switch_uuid
        self._tags = tags
        self._termination_time = termination_time
        self._updated_at = updated_at
        self._user = user
        self._userdata = userdata
        self._volumes = volumes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Device':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Device of this Device.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def always_pxe(self):
        """Gets the always_pxe of this Device.


        :return: The always_pxe of this Device.
        :rtype: bool
        """
        return self._always_pxe

    @always_pxe.setter
    def always_pxe(self, always_pxe):
        """Sets the always_pxe of this Device.


        :param always_pxe: The always_pxe of this Device.
        :type always_pxe: bool
        """

        self._always_pxe = always_pxe

    @property
    def billing_cycle(self):
        """Gets the billing_cycle of this Device.


        :return: The billing_cycle of this Device.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        """Sets the billing_cycle of this Device.


        :param billing_cycle: The billing_cycle of this Device.
        :type billing_cycle: str
        """

        self._billing_cycle = billing_cycle

    @property
    def bonding_mode(self):
        """Gets the bonding_mode of this Device.


        :return: The bonding_mode of this Device.
        :rtype: int
        """
        return self._bonding_mode

    @bonding_mode.setter
    def bonding_mode(self, bonding_mode):
        """Sets the bonding_mode of this Device.


        :param bonding_mode: The bonding_mode of this Device.
        :type bonding_mode: int
        """

        self._bonding_mode = bonding_mode

    @property
    def created_at(self):
        """Gets the created_at of this Device.


        :return: The created_at of this Device.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Device.


        :param created_at: The created_at of this Device.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Device.


        :return: The created_by of this Device.
        :rtype: DeviceCreatedBy
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Device.


        :param created_by: The created_by of this Device.
        :type created_by: DeviceCreatedBy
        """

        self._created_by = created_by

    @property
    def customdata(self):
        """Gets the customdata of this Device.


        :return: The customdata of this Device.
        :rtype: Dict[str, object]
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this Device.


        :param customdata: The customdata of this Device.
        :type customdata: Dict[str, object]
        """

        self._customdata = customdata

    @property
    def description(self):
        """Gets the description of this Device.


        :return: The description of this Device.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Device.


        :param description: The description of this Device.
        :type description: str
        """

        self._description = description

    @property
    def facility(self):
        """Gets the facility of this Device.


        :return: The facility of this Device.
        :rtype: Facility
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this Device.


        :param facility: The facility of this Device.
        :type facility: Facility
        """

        self._facility = facility

    @property
    def hardware_reservation(self):
        """Gets the hardware_reservation of this Device.


        :return: The hardware_reservation of this Device.
        :rtype: Href
        """
        return self._hardware_reservation

    @hardware_reservation.setter
    def hardware_reservation(self, hardware_reservation):
        """Sets the hardware_reservation of this Device.


        :param hardware_reservation: The hardware_reservation of this Device.
        :type hardware_reservation: Href
        """

        self._hardware_reservation = hardware_reservation

    @property
    def hostname(self):
        """Gets the hostname of this Device.


        :return: The hostname of this Device.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Device.


        :param hostname: The hostname of this Device.
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def href(self):
        """Gets the href of this Device.


        :return: The href of this Device.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Device.


        :param href: The href of this Device.
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Device.


        :return: The id of this Device.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.


        :param id: The id of this Device.
        :type id: str
        """

        self._id = id

    @property
    def image_url(self):
        """Gets the image_url of this Device.


        :return: The image_url of this Device.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Device.


        :param image_url: The image_url of this Device.
        :type image_url: str
        """

        self._image_url = image_url

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this Device.


        :return: The ip_addresses of this Device.
        :rtype: List[IPAssignment]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this Device.


        :param ip_addresses: The ip_addresses of this Device.
        :type ip_addresses: List[IPAssignment]
        """

        self._ip_addresses = ip_addresses

    @property
    def ipxe_script_url(self):
        """Gets the ipxe_script_url of this Device.


        :return: The ipxe_script_url of this Device.
        :rtype: str
        """
        return self._ipxe_script_url

    @ipxe_script_url.setter
    def ipxe_script_url(self, ipxe_script_url):
        """Sets the ipxe_script_url of this Device.


        :param ipxe_script_url: The ipxe_script_url of this Device.
        :type ipxe_script_url: str
        """

        self._ipxe_script_url = ipxe_script_url

    @property
    def iqn(self):
        """Gets the iqn of this Device.


        :return: The iqn of this Device.
        :rtype: str
        """
        return self._iqn

    @iqn.setter
    def iqn(self, iqn):
        """Sets the iqn of this Device.


        :param iqn: The iqn of this Device.
        :type iqn: str
        """

        self._iqn = iqn

    @property
    def locked(self):
        """Gets the locked of this Device.


        :return: The locked of this Device.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this Device.


        :param locked: The locked of this Device.
        :type locked: bool
        """

        self._locked = locked

    @property
    def metro(self):
        """Gets the metro of this Device.


        :return: The metro of this Device.
        :rtype: DeviceMetro
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this Device.


        :param metro: The metro of this Device.
        :type metro: DeviceMetro
        """

        self._metro = metro

    @property
    def network_ports(self):
        """Gets the network_ports of this Device.

        By default, servers at Equinix Metal are configured in a “bonded” mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans may have a different number of ports and bonds available.

        :return: The network_ports of this Device.
        :rtype: List[Port]
        """
        return self._network_ports

    @network_ports.setter
    def network_ports(self, network_ports):
        """Sets the network_ports of this Device.

        By default, servers at Equinix Metal are configured in a “bonded” mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans may have a different number of ports and bonds available.

        :param network_ports: The network_ports of this Device.
        :type network_ports: List[Port]
        """

        self._network_ports = network_ports

    @property
    def operating_system(self):
        """Gets the operating_system of this Device.


        :return: The operating_system of this Device.
        :rtype: OperatingSystem
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this Device.


        :param operating_system: The operating_system of this Device.
        :type operating_system: OperatingSystem
        """

        self._operating_system = operating_system

    @property
    def actions(self):
        """Gets the actions of this Device.

        Actions supported by the device instance.

        :return: The actions of this Device.
        :rtype: List[DeviceActionsInner]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Device.

        Actions supported by the device instance.

        :param actions: The actions of this Device.
        :type actions: List[DeviceActionsInner]
        """

        self._actions = actions

    @property
    def plan(self):
        """Gets the plan of this Device.


        :return: The plan of this Device.
        :rtype: Plan
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this Device.


        :param plan: The plan of this Device.
        :type plan: Plan
        """

        self._plan = plan

    @property
    def project(self):
        """Gets the project of this Device.


        :return: The project of this Device.
        :rtype: DeviceProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Device.


        :param project: The project of this Device.
        :type project: DeviceProject
        """

        self._project = project

    @property
    def project_lite(self):
        """Gets the project_lite of this Device.


        :return: The project_lite of this Device.
        :rtype: DeviceProjectLite
        """
        return self._project_lite

    @project_lite.setter
    def project_lite(self, project_lite):
        """Sets the project_lite of this Device.


        :param project_lite: The project_lite of this Device.
        :type project_lite: DeviceProjectLite
        """

        self._project_lite = project_lite

    @property
    def provisioning_events(self):
        """Gets the provisioning_events of this Device.


        :return: The provisioning_events of this Device.
        :rtype: List[Event]
        """
        return self._provisioning_events

    @provisioning_events.setter
    def provisioning_events(self, provisioning_events):
        """Sets the provisioning_events of this Device.


        :param provisioning_events: The provisioning_events of this Device.
        :type provisioning_events: List[Event]
        """

        self._provisioning_events = provisioning_events

    @property
    def provisioning_percentage(self):
        """Gets the provisioning_percentage of this Device.

        Only visible while device provisioning

        :return: The provisioning_percentage of this Device.
        :rtype: float
        """
        return self._provisioning_percentage

    @provisioning_percentage.setter
    def provisioning_percentage(self, provisioning_percentage):
        """Sets the provisioning_percentage of this Device.

        Only visible while device provisioning

        :param provisioning_percentage: The provisioning_percentage of this Device.
        :type provisioning_percentage: float
        """

        self._provisioning_percentage = provisioning_percentage

    @property
    def root_password(self):
        """Gets the root_password of this Device.

        Root password is automatically generated when server is provisioned and it is removed after 24 hours

        :return: The root_password of this Device.
        :rtype: str
        """
        return self._root_password

    @root_password.setter
    def root_password(self, root_password):
        """Sets the root_password of this Device.

        Root password is automatically generated when server is provisioned and it is removed after 24 hours

        :param root_password: The root_password of this Device.
        :type root_password: str
        """

        self._root_password = root_password

    @property
    def short_id(self):
        """Gets the short_id of this Device.


        :return: The short_id of this Device.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        """Sets the short_id of this Device.


        :param short_id: The short_id of this Device.
        :type short_id: str
        """

        self._short_id = short_id

    @property
    def spot_instance(self):
        """Gets the spot_instance of this Device.

        Whether or not the device is a spot instance.

        :return: The spot_instance of this Device.
        :rtype: bool
        """
        return self._spot_instance

    @spot_instance.setter
    def spot_instance(self, spot_instance):
        """Sets the spot_instance of this Device.

        Whether or not the device is a spot instance.

        :param spot_instance: The spot_instance of this Device.
        :type spot_instance: bool
        """

        self._spot_instance = spot_instance

    @property
    def spot_price_max(self):
        """Gets the spot_price_max of this Device.

        The maximum price per hour you are willing to pay to keep this spot instance.  If you are outbid, the termination will be set allowing two minutes before shutdown.

        :return: The spot_price_max of this Device.
        :rtype: float
        """
        return self._spot_price_max

    @spot_price_max.setter
    def spot_price_max(self, spot_price_max):
        """Sets the spot_price_max of this Device.

        The maximum price per hour you are willing to pay to keep this spot instance.  If you are outbid, the termination will be set allowing two minutes before shutdown.

        :param spot_price_max: The spot_price_max of this Device.
        :type spot_price_max: float
        """

        self._spot_price_max = spot_price_max

    @property
    def ssh_keys(self):
        """Gets the ssh_keys of this Device.


        :return: The ssh_keys of this Device.
        :rtype: List[Href]
        """
        return self._ssh_keys

    @ssh_keys.setter
    def ssh_keys(self, ssh_keys):
        """Sets the ssh_keys of this Device.


        :param ssh_keys: The ssh_keys of this Device.
        :type ssh_keys: List[Href]
        """

        self._ssh_keys = ssh_keys

    @property
    def state(self):
        """Gets the state of this Device.


        :return: The state of this Device.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Device.


        :param state: The state of this Device.
        :type state: str
        """
        allowed_values = ["active", "deleted", "deprovisioning", "failed", "inactive", "queued", "reinstalling", "post_provisioning", "powering_on", "powering_off", "provisioning"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def switch_uuid(self):
        """Gets the switch_uuid of this Device.

        Switch short id. This can be used to determine if two devices are connected to the same switch, for example.

        :return: The switch_uuid of this Device.
        :rtype: str
        """
        return self._switch_uuid

    @switch_uuid.setter
    def switch_uuid(self, switch_uuid):
        """Sets the switch_uuid of this Device.

        Switch short id. This can be used to determine if two devices are connected to the same switch, for example.

        :param switch_uuid: The switch_uuid of this Device.
        :type switch_uuid: str
        """

        self._switch_uuid = switch_uuid

    @property
    def tags(self):
        """Gets the tags of this Device.


        :return: The tags of this Device.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Device.


        :param tags: The tags of this Device.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def termination_time(self):
        """Gets the termination_time of this Device.

        When the device will be terminated. This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid.

        :return: The termination_time of this Device.
        :rtype: datetime
        """
        return self._termination_time

    @termination_time.setter
    def termination_time(self, termination_time):
        """Sets the termination_time of this Device.

        When the device will be terminated. This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid.

        :param termination_time: The termination_time of this Device.
        :type termination_time: datetime
        """

        self._termination_time = termination_time

    @property
    def updated_at(self):
        """Gets the updated_at of this Device.


        :return: The updated_at of this Device.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Device.


        :param updated_at: The updated_at of this Device.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this Device.


        :return: The user of this Device.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Device.


        :param user: The user of this Device.
        :type user: str
        """

        self._user = user

    @property
    def userdata(self):
        """Gets the userdata of this Device.


        :return: The userdata of this Device.
        :rtype: str
        """
        return self._userdata

    @userdata.setter
    def userdata(self, userdata):
        """Sets the userdata of this Device.


        :param userdata: The userdata of this Device.
        :type userdata: str
        """

        self._userdata = userdata

    @property
    def volumes(self):
        """Gets the volumes of this Device.


        :return: The volumes of this Device.
        :rtype: List[Href]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this Device.


        :param volumes: The volumes of this Device.
        :type volumes: List[Href]
        """

        self._volumes = volumes
