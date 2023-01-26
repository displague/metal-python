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


class IPReservation(object):
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
        'addon': 'bool',
        'address': 'str',
        'address_family': 'int',
        'assignments': 'list[IPAssignment]',
        'available': 'str',
        'bill': 'bool',
        'cidr': 'int',
        'created_at': 'datetime',
        'customdata': 'object',
        'enabled': 'bool',
        'details': 'str',
        'facility': 'IPReservationFacility',
        'gateway': 'str',
        'global_ip': 'bool',
        'href': 'str',
        'id': 'str',
        'manageable': 'bool',
        'management': 'bool',
        'metal_gateway': 'MetalGatewayLite',
        'metro': 'IPReservationMetro',
        'netmask': 'str',
        'network': 'str',
        'project': 'Project',
        'project_lite': 'Href',
        'requested_by': 'Href',
        'public': 'bool',
        'state': 'str',
        'tags': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'addon': 'addon',
        'address': 'address',
        'address_family': 'address_family',
        'assignments': 'assignments',
        'available': 'available',
        'bill': 'bill',
        'cidr': 'cidr',
        'created_at': 'created_at',
        'customdata': 'customdata',
        'enabled': 'enabled',
        'details': 'details',
        'facility': 'facility',
        'gateway': 'gateway',
        'global_ip': 'global_ip',
        'href': 'href',
        'id': 'id',
        'manageable': 'manageable',
        'management': 'management',
        'metal_gateway': 'metal_gateway',
        'metro': 'metro',
        'netmask': 'netmask',
        'network': 'network',
        'project': 'project',
        'project_lite': 'project_lite',
        'requested_by': 'requested_by',
        'public': 'public',
        'state': 'state',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, addon=None, address=None, address_family=None, assignments=None, available=None, bill=None, cidr=None, created_at=None, customdata=None, enabled=None, details=None, facility=None, gateway=None, global_ip=None, href=None, id=None, manageable=None, management=None, metal_gateway=None, metro=None, netmask=None, network=None, project=None, project_lite=None, requested_by=None, public=None, state=None, tags=None, type=None, local_vars_configuration=None):  # noqa: E501
        """IPReservation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._addon = None
        self._address = None
        self._address_family = None
        self._assignments = None
        self._available = None
        self._bill = None
        self._cidr = None
        self._created_at = None
        self._customdata = None
        self._enabled = None
        self._details = None
        self._facility = None
        self._gateway = None
        self._global_ip = None
        self._href = None
        self._id = None
        self._manageable = None
        self._management = None
        self._metal_gateway = None
        self._metro = None
        self._netmask = None
        self._network = None
        self._project = None
        self._project_lite = None
        self._requested_by = None
        self._public = None
        self._state = None
        self._tags = None
        self._type = None
        self.discriminator = None

        if addon is not None:
            self.addon = addon
        if address is not None:
            self.address = address
        if address_family is not None:
            self.address_family = address_family
        if assignments is not None:
            self.assignments = assignments
        if available is not None:
            self.available = available
        if bill is not None:
            self.bill = bill
        if cidr is not None:
            self.cidr = cidr
        if created_at is not None:
            self.created_at = created_at
        if customdata is not None:
            self.customdata = customdata
        if enabled is not None:
            self.enabled = enabled
        if details is not None:
            self.details = details
        if facility is not None:
            self.facility = facility
        if gateway is not None:
            self.gateway = gateway
        if global_ip is not None:
            self.global_ip = global_ip
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if manageable is not None:
            self.manageable = manageable
        if management is not None:
            self.management = management
        if metal_gateway is not None:
            self.metal_gateway = metal_gateway
        if metro is not None:
            self.metro = metro
        if netmask is not None:
            self.netmask = netmask
        if network is not None:
            self.network = network
        if project is not None:
            self.project = project
        if project_lite is not None:
            self.project_lite = project_lite
        if requested_by is not None:
            self.requested_by = requested_by
        if public is not None:
            self.public = public
        if state is not None:
            self.state = state
        if tags is not None:
            self.tags = tags
        self.type = type

    @property
    def addon(self):
        """Gets the addon of this IPReservation.  # noqa: E501


        :return: The addon of this IPReservation.  # noqa: E501
        :rtype: bool
        """
        return self._addon

    @addon.setter
    def addon(self, addon):
        """Sets the addon of this IPReservation.


        :param addon: The addon of this IPReservation.  # noqa: E501
        :type addon: bool
        """

        self._addon = addon

    @property
    def address(self):
        """Gets the address of this IPReservation.  # noqa: E501


        :return: The address of this IPReservation.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IPReservation.


        :param address: The address of this IPReservation.  # noqa: E501
        :type address: str
        """

        self._address = address

    @property
    def address_family(self):
        """Gets the address_family of this IPReservation.  # noqa: E501


        :return: The address_family of this IPReservation.  # noqa: E501
        :rtype: int
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this IPReservation.


        :param address_family: The address_family of this IPReservation.  # noqa: E501
        :type address_family: int
        """

        self._address_family = address_family

    @property
    def assignments(self):
        """Gets the assignments of this IPReservation.  # noqa: E501


        :return: The assignments of this IPReservation.  # noqa: E501
        :rtype: list[IPAssignment]
        """
        return self._assignments

    @assignments.setter
    def assignments(self, assignments):
        """Sets the assignments of this IPReservation.


        :param assignments: The assignments of this IPReservation.  # noqa: E501
        :type assignments: list[IPAssignment]
        """

        self._assignments = assignments

    @property
    def available(self):
        """Gets the available of this IPReservation.  # noqa: E501


        :return: The available of this IPReservation.  # noqa: E501
        :rtype: str
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this IPReservation.


        :param available: The available of this IPReservation.  # noqa: E501
        :type available: str
        """

        self._available = available

    @property
    def bill(self):
        """Gets the bill of this IPReservation.  # noqa: E501


        :return: The bill of this IPReservation.  # noqa: E501
        :rtype: bool
        """
        return self._bill

    @bill.setter
    def bill(self, bill):
        """Sets the bill of this IPReservation.


        :param bill: The bill of this IPReservation.  # noqa: E501
        :type bill: bool
        """

        self._bill = bill

    @property
    def cidr(self):
        """Gets the cidr of this IPReservation.  # noqa: E501


        :return: The cidr of this IPReservation.  # noqa: E501
        :rtype: int
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this IPReservation.


        :param cidr: The cidr of this IPReservation.  # noqa: E501
        :type cidr: int
        """

        self._cidr = cidr

    @property
    def created_at(self):
        """Gets the created_at of this IPReservation.  # noqa: E501


        :return: The created_at of this IPReservation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IPReservation.


        :param created_at: The created_at of this IPReservation.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def customdata(self):
        """Gets the customdata of this IPReservation.  # noqa: E501


        :return: The customdata of this IPReservation.  # noqa: E501
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this IPReservation.


        :param customdata: The customdata of this IPReservation.  # noqa: E501
        :type customdata: object
        """

        self._customdata = customdata

    @property
    def enabled(self):
        """Gets the enabled of this IPReservation.  # noqa: E501


        :return: The enabled of this IPReservation.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IPReservation.


        :param enabled: The enabled of this IPReservation.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def details(self):
        """Gets the details of this IPReservation.  # noqa: E501


        :return: The details of this IPReservation.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this IPReservation.


        :param details: The details of this IPReservation.  # noqa: E501
        :type details: str
        """

        self._details = details

    @property
    def facility(self):
        """Gets the facility of this IPReservation.  # noqa: E501


        :return: The facility of this IPReservation.  # noqa: E501
        :rtype: IPReservationFacility
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this IPReservation.


        :param facility: The facility of this IPReservation.  # noqa: E501
        :type facility: IPReservationFacility
        """

        self._facility = facility

    @property
    def gateway(self):
        """Gets the gateway of this IPReservation.  # noqa: E501


        :return: The gateway of this IPReservation.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this IPReservation.


        :param gateway: The gateway of this IPReservation.  # noqa: E501
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def global_ip(self):
        """Gets the global_ip of this IPReservation.  # noqa: E501


        :return: The global_ip of this IPReservation.  # noqa: E501
        :rtype: bool
        """
        return self._global_ip

    @global_ip.setter
    def global_ip(self, global_ip):
        """Sets the global_ip of this IPReservation.


        :param global_ip: The global_ip of this IPReservation.  # noqa: E501
        :type global_ip: bool
        """

        self._global_ip = global_ip

    @property
    def href(self):
        """Gets the href of this IPReservation.  # noqa: E501


        :return: The href of this IPReservation.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this IPReservation.


        :param href: The href of this IPReservation.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this IPReservation.  # noqa: E501


        :return: The id of this IPReservation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IPReservation.


        :param id: The id of this IPReservation.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def manageable(self):
        """Gets the manageable of this IPReservation.  # noqa: E501


        :return: The manageable of this IPReservation.  # noqa: E501
        :rtype: bool
        """
        return self._manageable

    @manageable.setter
    def manageable(self, manageable):
        """Sets the manageable of this IPReservation.


        :param manageable: The manageable of this IPReservation.  # noqa: E501
        :type manageable: bool
        """

        self._manageable = manageable

    @property
    def management(self):
        """Gets the management of this IPReservation.  # noqa: E501


        :return: The management of this IPReservation.  # noqa: E501
        :rtype: bool
        """
        return self._management

    @management.setter
    def management(self, management):
        """Sets the management of this IPReservation.


        :param management: The management of this IPReservation.  # noqa: E501
        :type management: bool
        """

        self._management = management

    @property
    def metal_gateway(self):
        """Gets the metal_gateway of this IPReservation.  # noqa: E501


        :return: The metal_gateway of this IPReservation.  # noqa: E501
        :rtype: MetalGatewayLite
        """
        return self._metal_gateway

    @metal_gateway.setter
    def metal_gateway(self, metal_gateway):
        """Sets the metal_gateway of this IPReservation.


        :param metal_gateway: The metal_gateway of this IPReservation.  # noqa: E501
        :type metal_gateway: MetalGatewayLite
        """

        self._metal_gateway = metal_gateway

    @property
    def metro(self):
        """Gets the metro of this IPReservation.  # noqa: E501


        :return: The metro of this IPReservation.  # noqa: E501
        :rtype: IPReservationMetro
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this IPReservation.


        :param metro: The metro of this IPReservation.  # noqa: E501
        :type metro: IPReservationMetro
        """

        self._metro = metro

    @property
    def netmask(self):
        """Gets the netmask of this IPReservation.  # noqa: E501


        :return: The netmask of this IPReservation.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this IPReservation.


        :param netmask: The netmask of this IPReservation.  # noqa: E501
        :type netmask: str
        """

        self._netmask = netmask

    @property
    def network(self):
        """Gets the network of this IPReservation.  # noqa: E501


        :return: The network of this IPReservation.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this IPReservation.


        :param network: The network of this IPReservation.  # noqa: E501
        :type network: str
        """

        self._network = network

    @property
    def project(self):
        """Gets the project of this IPReservation.  # noqa: E501


        :return: The project of this IPReservation.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this IPReservation.


        :param project: The project of this IPReservation.  # noqa: E501
        :type project: Project
        """

        self._project = project

    @property
    def project_lite(self):
        """Gets the project_lite of this IPReservation.  # noqa: E501


        :return: The project_lite of this IPReservation.  # noqa: E501
        :rtype: Href
        """
        return self._project_lite

    @project_lite.setter
    def project_lite(self, project_lite):
        """Sets the project_lite of this IPReservation.


        :param project_lite: The project_lite of this IPReservation.  # noqa: E501
        :type project_lite: Href
        """

        self._project_lite = project_lite

    @property
    def requested_by(self):
        """Gets the requested_by of this IPReservation.  # noqa: E501


        :return: The requested_by of this IPReservation.  # noqa: E501
        :rtype: Href
        """
        return self._requested_by

    @requested_by.setter
    def requested_by(self, requested_by):
        """Sets the requested_by of this IPReservation.


        :param requested_by: The requested_by of this IPReservation.  # noqa: E501
        :type requested_by: Href
        """

        self._requested_by = requested_by

    @property
    def public(self):
        """Gets the public of this IPReservation.  # noqa: E501


        :return: The public of this IPReservation.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this IPReservation.


        :param public: The public of this IPReservation.  # noqa: E501
        :type public: bool
        """

        self._public = public

    @property
    def state(self):
        """Gets the state of this IPReservation.  # noqa: E501


        :return: The state of this IPReservation.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this IPReservation.


        :param state: The state of this IPReservation.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def tags(self):
        """Gets the tags of this IPReservation.  # noqa: E501


        :return: The tags of this IPReservation.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this IPReservation.


        :param tags: The tags of this IPReservation.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this IPReservation.  # noqa: E501


        :return: The type of this IPReservation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IPReservation.


        :param type: The type of this IPReservation.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["global_ipv4", "public_ipv4", "private_ipv4", "public_ipv6"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, IPReservation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IPReservation):
            return True

        return self.to_dict() != other.to_dict()
