# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://metal.equinix.com/developers/api>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. The fields available for search differ by resource, as does the search strategy.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from metal.configuration import Configuration


class Device(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'always_pxe': 'bool',
        'billing_cycle': 'str',
        'bonding_mode': 'int',
        'created_at': 'datetime',
        'created_by': 'DeviceCreatedBy',
        'customdata': 'dict[str, object]',
        'description': 'str',
        'facility': 'Facility',
        'hardware_reservation': 'Href',
        'hostname': 'str',
        'href': 'str',
        'id': 'str',
        'image_url': 'str',
        'ip_addresses': 'list[IPAssignment]',
        'ipxe_script_url': 'str',
        'iqn': 'str',
        'locked': 'bool',
        'metro': 'DeviceMetro',
        'network_ports': 'list[Port]',
        'operating_system': 'OperatingSystem',
        'actions': 'list[DeviceActionsInner]',
        'plan': 'Plan',
        'project': 'DeviceProject',
        'project_lite': 'DeviceProjectLite',
        'provisioning_events': 'list[Event]',
        'provisioning_percentage': 'float',
        'root_password': 'str',
        'short_id': 'str',
        'spot_instance': 'bool',
        'spot_price_max': 'float',
        'ssh_keys': 'list[Href]',
        'state': 'str',
        'switch_uuid': 'str',
        'tags': 'list[str]',
        'termination_time': 'datetime',
        'updated_at': 'datetime',
        'user': 'str',
        'userdata': 'str',
        'volumes': 'list[Href]'
    }

    attribute_map = {
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

    def __init__(self, always_pxe=None, billing_cycle=None, bonding_mode=None, created_at=None, created_by=None, customdata=None, description=None, facility=None, hardware_reservation=None, hostname=None, href=None, id=None, image_url=None, ip_addresses=None, ipxe_script_url=None, iqn=None, locked=None, metro=None, network_ports=None, operating_system=None, actions=None, plan=None, project=None, project_lite=None, provisioning_events=None, provisioning_percentage=None, root_password=None, short_id=None, spot_instance=None, spot_price_max=None, ssh_keys=None, state=None, switch_uuid=None, tags=None, termination_time=None, updated_at=None, user=None, userdata=None, volumes=None, local_vars_configuration=None):  # noqa: E501
        """Device - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._always_pxe = None
        self._billing_cycle = None
        self._bonding_mode = None
        self._created_at = None
        self._created_by = None
        self._customdata = None
        self._description = None
        self._facility = None
        self._hardware_reservation = None
        self._hostname = None
        self._href = None
        self._id = None
        self._image_url = None
        self._ip_addresses = None
        self._ipxe_script_url = None
        self._iqn = None
        self._locked = None
        self._metro = None
        self._network_ports = None
        self._operating_system = None
        self._actions = None
        self._plan = None
        self._project = None
        self._project_lite = None
        self._provisioning_events = None
        self._provisioning_percentage = None
        self._root_password = None
        self._short_id = None
        self._spot_instance = None
        self._spot_price_max = None
        self._ssh_keys = None
        self._state = None
        self._switch_uuid = None
        self._tags = None
        self._termination_time = None
        self._updated_at = None
        self._user = None
        self._userdata = None
        self._volumes = None
        self.discriminator = None

        if always_pxe is not None:
            self.always_pxe = always_pxe
        if billing_cycle is not None:
            self.billing_cycle = billing_cycle
        if bonding_mode is not None:
            self.bonding_mode = bonding_mode
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if customdata is not None:
            self.customdata = customdata
        if description is not None:
            self.description = description
        if facility is not None:
            self.facility = facility
        if hardware_reservation is not None:
            self.hardware_reservation = hardware_reservation
        if hostname is not None:
            self.hostname = hostname
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if image_url is not None:
            self.image_url = image_url
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if ipxe_script_url is not None:
            self.ipxe_script_url = ipxe_script_url
        if iqn is not None:
            self.iqn = iqn
        if locked is not None:
            self.locked = locked
        if metro is not None:
            self.metro = metro
        if network_ports is not None:
            self.network_ports = network_ports
        if operating_system is not None:
            self.operating_system = operating_system
        if actions is not None:
            self.actions = actions
        if plan is not None:
            self.plan = plan
        if project is not None:
            self.project = project
        if project_lite is not None:
            self.project_lite = project_lite
        if provisioning_events is not None:
            self.provisioning_events = provisioning_events
        if provisioning_percentage is not None:
            self.provisioning_percentage = provisioning_percentage
        if root_password is not None:
            self.root_password = root_password
        if short_id is not None:
            self.short_id = short_id
        if spot_instance is not None:
            self.spot_instance = spot_instance
        if spot_price_max is not None:
            self.spot_price_max = spot_price_max
        if ssh_keys is not None:
            self.ssh_keys = ssh_keys
        if state is not None:
            self.state = state
        if switch_uuid is not None:
            self.switch_uuid = switch_uuid
        if tags is not None:
            self.tags = tags
        if termination_time is not None:
            self.termination_time = termination_time
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user
        if userdata is not None:
            self.userdata = userdata
        if volumes is not None:
            self.volumes = volumes

    @property
    def always_pxe(self):
        """Gets the always_pxe of this Device.  # noqa: E501


        :return: The always_pxe of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._always_pxe

    @always_pxe.setter
    def always_pxe(self, always_pxe):
        """Sets the always_pxe of this Device.


        :param always_pxe: The always_pxe of this Device.  # noqa: E501
        :type always_pxe: bool
        """

        self._always_pxe = always_pxe

    @property
    def billing_cycle(self):
        """Gets the billing_cycle of this Device.  # noqa: E501


        :return: The billing_cycle of this Device.  # noqa: E501
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        """Sets the billing_cycle of this Device.


        :param billing_cycle: The billing_cycle of this Device.  # noqa: E501
        :type billing_cycle: str
        """

        self._billing_cycle = billing_cycle

    @property
    def bonding_mode(self):
        """Gets the bonding_mode of this Device.  # noqa: E501


        :return: The bonding_mode of this Device.  # noqa: E501
        :rtype: int
        """
        return self._bonding_mode

    @bonding_mode.setter
    def bonding_mode(self, bonding_mode):
        """Sets the bonding_mode of this Device.


        :param bonding_mode: The bonding_mode of this Device.  # noqa: E501
        :type bonding_mode: int
        """

        self._bonding_mode = bonding_mode

    @property
    def created_at(self):
        """Gets the created_at of this Device.  # noqa: E501


        :return: The created_at of this Device.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Device.


        :param created_at: The created_at of this Device.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Device.  # noqa: E501


        :return: The created_by of this Device.  # noqa: E501
        :rtype: DeviceCreatedBy
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Device.


        :param created_by: The created_by of this Device.  # noqa: E501
        :type created_by: DeviceCreatedBy
        """

        self._created_by = created_by

    @property
    def customdata(self):
        """Gets the customdata of this Device.  # noqa: E501


        :return: The customdata of this Device.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this Device.


        :param customdata: The customdata of this Device.  # noqa: E501
        :type customdata: dict[str, object]
        """

        self._customdata = customdata

    @property
    def description(self):
        """Gets the description of this Device.  # noqa: E501


        :return: The description of this Device.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Device.


        :param description: The description of this Device.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def facility(self):
        """Gets the facility of this Device.  # noqa: E501


        :return: The facility of this Device.  # noqa: E501
        :rtype: Facility
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this Device.


        :param facility: The facility of this Device.  # noqa: E501
        :type facility: Facility
        """

        self._facility = facility

    @property
    def hardware_reservation(self):
        """Gets the hardware_reservation of this Device.  # noqa: E501


        :return: The hardware_reservation of this Device.  # noqa: E501
        :rtype: Href
        """
        return self._hardware_reservation

    @hardware_reservation.setter
    def hardware_reservation(self, hardware_reservation):
        """Sets the hardware_reservation of this Device.


        :param hardware_reservation: The hardware_reservation of this Device.  # noqa: E501
        :type hardware_reservation: Href
        """

        self._hardware_reservation = hardware_reservation

    @property
    def hostname(self):
        """Gets the hostname of this Device.  # noqa: E501


        :return: The hostname of this Device.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Device.


        :param hostname: The hostname of this Device.  # noqa: E501
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def href(self):
        """Gets the href of this Device.  # noqa: E501


        :return: The href of this Device.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Device.


        :param href: The href of this Device.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Device.  # noqa: E501


        :return: The id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.


        :param id: The id of this Device.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def image_url(self):
        """Gets the image_url of this Device.  # noqa: E501


        :return: The image_url of this Device.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Device.


        :param image_url: The image_url of this Device.  # noqa: E501
        :type image_url: str
        """

        self._image_url = image_url

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this Device.  # noqa: E501


        :return: The ip_addresses of this Device.  # noqa: E501
        :rtype: list[IPAssignment]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this Device.


        :param ip_addresses: The ip_addresses of this Device.  # noqa: E501
        :type ip_addresses: list[IPAssignment]
        """

        self._ip_addresses = ip_addresses

    @property
    def ipxe_script_url(self):
        """Gets the ipxe_script_url of this Device.  # noqa: E501


        :return: The ipxe_script_url of this Device.  # noqa: E501
        :rtype: str
        """
        return self._ipxe_script_url

    @ipxe_script_url.setter
    def ipxe_script_url(self, ipxe_script_url):
        """Sets the ipxe_script_url of this Device.


        :param ipxe_script_url: The ipxe_script_url of this Device.  # noqa: E501
        :type ipxe_script_url: str
        """

        self._ipxe_script_url = ipxe_script_url

    @property
    def iqn(self):
        """Gets the iqn of this Device.  # noqa: E501


        :return: The iqn of this Device.  # noqa: E501
        :rtype: str
        """
        return self._iqn

    @iqn.setter
    def iqn(self, iqn):
        """Sets the iqn of this Device.


        :param iqn: The iqn of this Device.  # noqa: E501
        :type iqn: str
        """

        self._iqn = iqn

    @property
    def locked(self):
        """Gets the locked of this Device.  # noqa: E501


        :return: The locked of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this Device.


        :param locked: The locked of this Device.  # noqa: E501
        :type locked: bool
        """

        self._locked = locked

    @property
    def metro(self):
        """Gets the metro of this Device.  # noqa: E501


        :return: The metro of this Device.  # noqa: E501
        :rtype: DeviceMetro
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this Device.


        :param metro: The metro of this Device.  # noqa: E501
        :type metro: DeviceMetro
        """

        self._metro = metro

    @property
    def network_ports(self):
        """Gets the network_ports of this Device.  # noqa: E501

        By default, servers at Equinix Metal are configured in a “bonded” mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans may have a different number of ports and bonds available.  # noqa: E501

        :return: The network_ports of this Device.  # noqa: E501
        :rtype: list[Port]
        """
        return self._network_ports

    @network_ports.setter
    def network_ports(self, network_ports):
        """Sets the network_ports of this Device.

        By default, servers at Equinix Metal are configured in a “bonded” mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans may have a different number of ports and bonds available.  # noqa: E501

        :param network_ports: The network_ports of this Device.  # noqa: E501
        :type network_ports: list[Port]
        """

        self._network_ports = network_ports

    @property
    def operating_system(self):
        """Gets the operating_system of this Device.  # noqa: E501


        :return: The operating_system of this Device.  # noqa: E501
        :rtype: OperatingSystem
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this Device.


        :param operating_system: The operating_system of this Device.  # noqa: E501
        :type operating_system: OperatingSystem
        """

        self._operating_system = operating_system

    @property
    def actions(self):
        """Gets the actions of this Device.  # noqa: E501

        Actions supported by the device instance.  # noqa: E501

        :return: The actions of this Device.  # noqa: E501
        :rtype: list[DeviceActionsInner]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Device.

        Actions supported by the device instance.  # noqa: E501

        :param actions: The actions of this Device.  # noqa: E501
        :type actions: list[DeviceActionsInner]
        """

        self._actions = actions

    @property
    def plan(self):
        """Gets the plan of this Device.  # noqa: E501


        :return: The plan of this Device.  # noqa: E501
        :rtype: Plan
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this Device.


        :param plan: The plan of this Device.  # noqa: E501
        :type plan: Plan
        """

        self._plan = plan

    @property
    def project(self):
        """Gets the project of this Device.  # noqa: E501


        :return: The project of this Device.  # noqa: E501
        :rtype: DeviceProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Device.


        :param project: The project of this Device.  # noqa: E501
        :type project: DeviceProject
        """

        self._project = project

    @property
    def project_lite(self):
        """Gets the project_lite of this Device.  # noqa: E501


        :return: The project_lite of this Device.  # noqa: E501
        :rtype: DeviceProjectLite
        """
        return self._project_lite

    @project_lite.setter
    def project_lite(self, project_lite):
        """Sets the project_lite of this Device.


        :param project_lite: The project_lite of this Device.  # noqa: E501
        :type project_lite: DeviceProjectLite
        """

        self._project_lite = project_lite

    @property
    def provisioning_events(self):
        """Gets the provisioning_events of this Device.  # noqa: E501


        :return: The provisioning_events of this Device.  # noqa: E501
        :rtype: list[Event]
        """
        return self._provisioning_events

    @provisioning_events.setter
    def provisioning_events(self, provisioning_events):
        """Sets the provisioning_events of this Device.


        :param provisioning_events: The provisioning_events of this Device.  # noqa: E501
        :type provisioning_events: list[Event]
        """

        self._provisioning_events = provisioning_events

    @property
    def provisioning_percentage(self):
        """Gets the provisioning_percentage of this Device.  # noqa: E501

        Only visible while device provisioning  # noqa: E501

        :return: The provisioning_percentage of this Device.  # noqa: E501
        :rtype: float
        """
        return self._provisioning_percentage

    @provisioning_percentage.setter
    def provisioning_percentage(self, provisioning_percentage):
        """Sets the provisioning_percentage of this Device.

        Only visible while device provisioning  # noqa: E501

        :param provisioning_percentage: The provisioning_percentage of this Device.  # noqa: E501
        :type provisioning_percentage: float
        """

        self._provisioning_percentage = provisioning_percentage

    @property
    def root_password(self):
        """Gets the root_password of this Device.  # noqa: E501

        Root password is automatically generated when server is provisioned and it is removed after 24 hours  # noqa: E501

        :return: The root_password of this Device.  # noqa: E501
        :rtype: str
        """
        return self._root_password

    @root_password.setter
    def root_password(self, root_password):
        """Sets the root_password of this Device.

        Root password is automatically generated when server is provisioned and it is removed after 24 hours  # noqa: E501

        :param root_password: The root_password of this Device.  # noqa: E501
        :type root_password: str
        """

        self._root_password = root_password

    @property
    def short_id(self):
        """Gets the short_id of this Device.  # noqa: E501


        :return: The short_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        """Sets the short_id of this Device.


        :param short_id: The short_id of this Device.  # noqa: E501
        :type short_id: str
        """

        self._short_id = short_id

    @property
    def spot_instance(self):
        """Gets the spot_instance of this Device.  # noqa: E501

        Whether or not the device is a spot instance.  # noqa: E501

        :return: The spot_instance of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._spot_instance

    @spot_instance.setter
    def spot_instance(self, spot_instance):
        """Sets the spot_instance of this Device.

        Whether or not the device is a spot instance.  # noqa: E501

        :param spot_instance: The spot_instance of this Device.  # noqa: E501
        :type spot_instance: bool
        """

        self._spot_instance = spot_instance

    @property
    def spot_price_max(self):
        """Gets the spot_price_max of this Device.  # noqa: E501

        The maximum price per hour you are willing to pay to keep this spot instance.  If you are outbid, the termination will be set allowing two minutes before shutdown.  # noqa: E501

        :return: The spot_price_max of this Device.  # noqa: E501
        :rtype: float
        """
        return self._spot_price_max

    @spot_price_max.setter
    def spot_price_max(self, spot_price_max):
        """Sets the spot_price_max of this Device.

        The maximum price per hour you are willing to pay to keep this spot instance.  If you are outbid, the termination will be set allowing two minutes before shutdown.  # noqa: E501

        :param spot_price_max: The spot_price_max of this Device.  # noqa: E501
        :type spot_price_max: float
        """

        self._spot_price_max = spot_price_max

    @property
    def ssh_keys(self):
        """Gets the ssh_keys of this Device.  # noqa: E501


        :return: The ssh_keys of this Device.  # noqa: E501
        :rtype: list[Href]
        """
        return self._ssh_keys

    @ssh_keys.setter
    def ssh_keys(self, ssh_keys):
        """Sets the ssh_keys of this Device.


        :param ssh_keys: The ssh_keys of this Device.  # noqa: E501
        :type ssh_keys: list[Href]
        """

        self._ssh_keys = ssh_keys

    @property
    def state(self):
        """Gets the state of this Device.  # noqa: E501


        :return: The state of this Device.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Device.


        :param state: The state of this Device.  # noqa: E501
        :type state: str
        """
        allowed_values = ["active", "deleted", "deprovisioning", "failed", "inactive", "queued", "reinstalling", "post_provisioning", "powering_on", "powering_off", "provisioning"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def switch_uuid(self):
        """Gets the switch_uuid of this Device.  # noqa: E501

        Switch short id. This can be used to determine if two devices are connected to the same switch, for example.  # noqa: E501

        :return: The switch_uuid of this Device.  # noqa: E501
        :rtype: str
        """
        return self._switch_uuid

    @switch_uuid.setter
    def switch_uuid(self, switch_uuid):
        """Sets the switch_uuid of this Device.

        Switch short id. This can be used to determine if two devices are connected to the same switch, for example.  # noqa: E501

        :param switch_uuid: The switch_uuid of this Device.  # noqa: E501
        :type switch_uuid: str
        """

        self._switch_uuid = switch_uuid

    @property
    def tags(self):
        """Gets the tags of this Device.  # noqa: E501


        :return: The tags of this Device.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Device.


        :param tags: The tags of this Device.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def termination_time(self):
        """Gets the termination_time of this Device.  # noqa: E501

        When the device will be terminated. This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid.  # noqa: E501

        :return: The termination_time of this Device.  # noqa: E501
        :rtype: datetime
        """
        return self._termination_time

    @termination_time.setter
    def termination_time(self, termination_time):
        """Sets the termination_time of this Device.

        When the device will be terminated. This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid.  # noqa: E501

        :param termination_time: The termination_time of this Device.  # noqa: E501
        :type termination_time: datetime
        """

        self._termination_time = termination_time

    @property
    def updated_at(self):
        """Gets the updated_at of this Device.  # noqa: E501


        :return: The updated_at of this Device.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Device.


        :param updated_at: The updated_at of this Device.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this Device.  # noqa: E501


        :return: The user of this Device.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Device.


        :param user: The user of this Device.  # noqa: E501
        :type user: str
        """

        self._user = user

    @property
    def userdata(self):
        """Gets the userdata of this Device.  # noqa: E501


        :return: The userdata of this Device.  # noqa: E501
        :rtype: str
        """
        return self._userdata

    @userdata.setter
    def userdata(self, userdata):
        """Sets the userdata of this Device.


        :param userdata: The userdata of this Device.  # noqa: E501
        :type userdata: str
        """

        self._userdata = userdata

    @property
    def volumes(self):
        """Gets the volumes of this Device.  # noqa: E501


        :return: The volumes of this Device.  # noqa: E501
        :rtype: list[Href]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this Device.


        :param volumes: The volumes of this Device.  # noqa: E501
        :type volumes: list[Href]
        """

        self._volumes = volumes

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Device):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Device):
            return True

        return self.to_dict() != other.to_dict()
