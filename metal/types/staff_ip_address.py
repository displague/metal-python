# coding: utf-8

"""
    Metal API

    This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from metal.configuration import Configuration


class StaffIpAddress(object):
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
        'id': 'str',
        'network': 'str',
        'address_family': 'int',
        'netmask': 'str',
        'created_at': 'datetime',
        'details': 'str',
        'public': 'bool',
        'management': 'bool',
        'manageable': 'bool',
        'enabled': 'bool',
        'created_by': 'str',
        'global_ip': 'bool',
        'reservation': 'bool',
        'customdata': 'object',
        'bill': 'bool',
        'tags': 'list[str]',
        'address': 'str',
        'gateway': 'str',
        'cidr': 'int',
        'state': 'str',
        'requested_quantity': 'int',
        'facility': 'StaffFacilityLittle',
        'metro': 'StaffMetroLittle',
        'interface': 'StaffPort'
    }

    attribute_map = {
        'id': 'id',
        'network': 'network',
        'address_family': 'address_family',
        'netmask': 'netmask',
        'created_at': 'created_at',
        'details': 'details',
        'public': 'public',
        'management': 'management',
        'manageable': 'manageable',
        'enabled': 'enabled',
        'created_by': 'created_by',
        'global_ip': 'global_ip',
        'reservation': 'reservation',
        'customdata': 'customdata',
        'bill': 'bill',
        'tags': 'tags',
        'address': 'address',
        'gateway': 'gateway',
        'cidr': 'cidr',
        'state': 'state',
        'requested_quantity': 'requested_quantity',
        'facility': 'facility',
        'metro': 'metro',
        'interface': 'interface'
    }

    def __init__(self, id=None, network=None, address_family=None, netmask=None, created_at=None, details=None, public=None, management=None, manageable=None, enabled=None, created_by=None, global_ip=None, reservation=None, customdata=None, bill=None, tags=None, address=None, gateway=None, cidr=None, state=None, requested_quantity=None, facility=None, metro=None, interface=None, local_vars_configuration=None):  # noqa: E501
        """StaffIpAddress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._network = None
        self._address_family = None
        self._netmask = None
        self._created_at = None
        self._details = None
        self._public = None
        self._management = None
        self._manageable = None
        self._enabled = None
        self._created_by = None
        self._global_ip = None
        self._reservation = None
        self._customdata = None
        self._bill = None
        self._tags = None
        self._address = None
        self._gateway = None
        self._cidr = None
        self._state = None
        self._requested_quantity = None
        self._facility = None
        self._metro = None
        self._interface = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if network is not None:
            self.network = network
        if address_family is not None:
            self.address_family = address_family
        if netmask is not None:
            self.netmask = netmask
        if created_at is not None:
            self.created_at = created_at
        if details is not None:
            self.details = details
        if public is not None:
            self.public = public
        if management is not None:
            self.management = management
        if manageable is not None:
            self.manageable = manageable
        if enabled is not None:
            self.enabled = enabled
        if created_by is not None:
            self.created_by = created_by
        if global_ip is not None:
            self.global_ip = global_ip
        if reservation is not None:
            self.reservation = reservation
        if customdata is not None:
            self.customdata = customdata
        if bill is not None:
            self.bill = bill
        if tags is not None:
            self.tags = tags
        if address is not None:
            self.address = address
        if gateway is not None:
            self.gateway = gateway
        if cidr is not None:
            self.cidr = cidr
        if state is not None:
            self.state = state
        if requested_quantity is not None:
            self.requested_quantity = requested_quantity
        if facility is not None:
            self.facility = facility
        if metro is not None:
            self.metro = metro
        if interface is not None:
            self.interface = interface

    @property
    def id(self):
        """Gets the id of this StaffIpAddress.  # noqa: E501


        :return: The id of this StaffIpAddress.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StaffIpAddress.


        :param id: The id of this StaffIpAddress.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def network(self):
        """Gets the network of this StaffIpAddress.  # noqa: E501


        :return: The network of this StaffIpAddress.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this StaffIpAddress.


        :param network: The network of this StaffIpAddress.  # noqa: E501
        :type network: str
        """

        self._network = network

    @property
    def address_family(self):
        """Gets the address_family of this StaffIpAddress.  # noqa: E501


        :return: The address_family of this StaffIpAddress.  # noqa: E501
        :rtype: int
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this StaffIpAddress.


        :param address_family: The address_family of this StaffIpAddress.  # noqa: E501
        :type address_family: int
        """

        self._address_family = address_family

    @property
    def netmask(self):
        """Gets the netmask of this StaffIpAddress.  # noqa: E501


        :return: The netmask of this StaffIpAddress.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this StaffIpAddress.


        :param netmask: The netmask of this StaffIpAddress.  # noqa: E501
        :type netmask: str
        """

        self._netmask = netmask

    @property
    def created_at(self):
        """Gets the created_at of this StaffIpAddress.  # noqa: E501


        :return: The created_at of this StaffIpAddress.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this StaffIpAddress.


        :param created_at: The created_at of this StaffIpAddress.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def details(self):
        """Gets the details of this StaffIpAddress.  # noqa: E501


        :return: The details of this StaffIpAddress.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this StaffIpAddress.


        :param details: The details of this StaffIpAddress.  # noqa: E501
        :type details: str
        """

        self._details = details

    @property
    def public(self):
        """Gets the public of this StaffIpAddress.  # noqa: E501


        :return: The public of this StaffIpAddress.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this StaffIpAddress.


        :param public: The public of this StaffIpAddress.  # noqa: E501
        :type public: bool
        """

        self._public = public

    @property
    def management(self):
        """Gets the management of this StaffIpAddress.  # noqa: E501


        :return: The management of this StaffIpAddress.  # noqa: E501
        :rtype: bool
        """
        return self._management

    @management.setter
    def management(self, management):
        """Sets the management of this StaffIpAddress.


        :param management: The management of this StaffIpAddress.  # noqa: E501
        :type management: bool
        """

        self._management = management

    @property
    def manageable(self):
        """Gets the manageable of this StaffIpAddress.  # noqa: E501


        :return: The manageable of this StaffIpAddress.  # noqa: E501
        :rtype: bool
        """
        return self._manageable

    @manageable.setter
    def manageable(self, manageable):
        """Sets the manageable of this StaffIpAddress.


        :param manageable: The manageable of this StaffIpAddress.  # noqa: E501
        :type manageable: bool
        """

        self._manageable = manageable

    @property
    def enabled(self):
        """Gets the enabled of this StaffIpAddress.  # noqa: E501


        :return: The enabled of this StaffIpAddress.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this StaffIpAddress.


        :param enabled: The enabled of this StaffIpAddress.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def created_by(self):
        """Gets the created_by of this StaffIpAddress.  # noqa: E501


        :return: The created_by of this StaffIpAddress.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this StaffIpAddress.


        :param created_by: The created_by of this StaffIpAddress.  # noqa: E501
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def global_ip(self):
        """Gets the global_ip of this StaffIpAddress.  # noqa: E501


        :return: The global_ip of this StaffIpAddress.  # noqa: E501
        :rtype: bool
        """
        return self._global_ip

    @global_ip.setter
    def global_ip(self, global_ip):
        """Sets the global_ip of this StaffIpAddress.


        :param global_ip: The global_ip of this StaffIpAddress.  # noqa: E501
        :type global_ip: bool
        """

        self._global_ip = global_ip

    @property
    def reservation(self):
        """Gets the reservation of this StaffIpAddress.  # noqa: E501


        :return: The reservation of this StaffIpAddress.  # noqa: E501
        :rtype: bool
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation):
        """Sets the reservation of this StaffIpAddress.


        :param reservation: The reservation of this StaffIpAddress.  # noqa: E501
        :type reservation: bool
        """

        self._reservation = reservation

    @property
    def customdata(self):
        """Gets the customdata of this StaffIpAddress.  # noqa: E501


        :return: The customdata of this StaffIpAddress.  # noqa: E501
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this StaffIpAddress.


        :param customdata: The customdata of this StaffIpAddress.  # noqa: E501
        :type customdata: object
        """

        self._customdata = customdata

    @property
    def bill(self):
        """Gets the bill of this StaffIpAddress.  # noqa: E501


        :return: The bill of this StaffIpAddress.  # noqa: E501
        :rtype: bool
        """
        return self._bill

    @bill.setter
    def bill(self, bill):
        """Sets the bill of this StaffIpAddress.


        :param bill: The bill of this StaffIpAddress.  # noqa: E501
        :type bill: bool
        """

        self._bill = bill

    @property
    def tags(self):
        """Gets the tags of this StaffIpAddress.  # noqa: E501


        :return: The tags of this StaffIpAddress.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this StaffIpAddress.


        :param tags: The tags of this StaffIpAddress.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def address(self):
        """Gets the address of this StaffIpAddress.  # noqa: E501


        :return: The address of this StaffIpAddress.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this StaffIpAddress.


        :param address: The address of this StaffIpAddress.  # noqa: E501
        :type address: str
        """

        self._address = address

    @property
    def gateway(self):
        """Gets the gateway of this StaffIpAddress.  # noqa: E501


        :return: The gateway of this StaffIpAddress.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this StaffIpAddress.


        :param gateway: The gateway of this StaffIpAddress.  # noqa: E501
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def cidr(self):
        """Gets the cidr of this StaffIpAddress.  # noqa: E501


        :return: The cidr of this StaffIpAddress.  # noqa: E501
        :rtype: int
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this StaffIpAddress.


        :param cidr: The cidr of this StaffIpAddress.  # noqa: E501
        :type cidr: int
        """

        self._cidr = cidr

    @property
    def state(self):
        """Gets the state of this StaffIpAddress.  # noqa: E501


        :return: The state of this StaffIpAddress.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this StaffIpAddress.


        :param state: The state of this StaffIpAddress.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def requested_quantity(self):
        """Gets the requested_quantity of this StaffIpAddress.  # noqa: E501


        :return: The requested_quantity of this StaffIpAddress.  # noqa: E501
        :rtype: int
        """
        return self._requested_quantity

    @requested_quantity.setter
    def requested_quantity(self, requested_quantity):
        """Sets the requested_quantity of this StaffIpAddress.


        :param requested_quantity: The requested_quantity of this StaffIpAddress.  # noqa: E501
        :type requested_quantity: int
        """

        self._requested_quantity = requested_quantity

    @property
    def facility(self):
        """Gets the facility of this StaffIpAddress.  # noqa: E501


        :return: The facility of this StaffIpAddress.  # noqa: E501
        :rtype: StaffFacilityLittle
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this StaffIpAddress.


        :param facility: The facility of this StaffIpAddress.  # noqa: E501
        :type facility: StaffFacilityLittle
        """

        self._facility = facility

    @property
    def metro(self):
        """Gets the metro of this StaffIpAddress.  # noqa: E501


        :return: The metro of this StaffIpAddress.  # noqa: E501
        :rtype: StaffMetroLittle
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this StaffIpAddress.


        :param metro: The metro of this StaffIpAddress.  # noqa: E501
        :type metro: StaffMetroLittle
        """

        self._metro = metro

    @property
    def interface(self):
        """Gets the interface of this StaffIpAddress.  # noqa: E501


        :return: The interface of this StaffIpAddress.  # noqa: E501
        :rtype: StaffPort
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this StaffIpAddress.


        :param interface: The interface of this StaffIpAddress.  # noqa: E501
        :type interface: StaffPort
        """

        self._interface = interface

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
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
        if not isinstance(other, StaffIpAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StaffIpAddress):
            return True

        return self.to_dict() != other.to_dict()