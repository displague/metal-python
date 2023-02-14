# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal.types.href import Href
from metal.types.ip_assignment import IPAssignment
from metal.types.ip_reservation_facility import IPReservationFacility
from metal.types.ip_reservation_metro import IPReservationMetro
from metal.types.metal_gateway_lite import MetalGatewayLite
from metal.types.project import Project
from metal import util


class IPReservation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, addon: bool=None, address: str=None, address_family: int=None, assignments: List[IPAssignment]=None, available: str=None, bill: bool=None, cidr: int=None, created_at: datetime=None, customdata: object=None, enabled: bool=None, details: str=None, facility: IPReservationFacility=None, gateway: str=None, global_ip: bool=None, href: str=None, id: str=None, manageable: bool=None, management: bool=None, metal_gateway: MetalGatewayLite=None, metro: IPReservationMetro=None, netmask: str=None, network: str=None, project: Project=None, project_lite: Href=None, requested_by: Href=None, public: bool=None, state: str=None, tags: List[str]=None, type: str=None):
        """IPReservation - a model defined in OpenAPI

        :param addon: The addon of this IPReservation.
        :param address: The address of this IPReservation.
        :param address_family: The address_family of this IPReservation.
        :param assignments: The assignments of this IPReservation.
        :param available: The available of this IPReservation.
        :param bill: The bill of this IPReservation.
        :param cidr: The cidr of this IPReservation.
        :param created_at: The created_at of this IPReservation.
        :param customdata: The customdata of this IPReservation.
        :param enabled: The enabled of this IPReservation.
        :param details: The details of this IPReservation.
        :param facility: The facility of this IPReservation.
        :param gateway: The gateway of this IPReservation.
        :param global_ip: The global_ip of this IPReservation.
        :param href: The href of this IPReservation.
        :param id: The id of this IPReservation.
        :param manageable: The manageable of this IPReservation.
        :param management: The management of this IPReservation.
        :param metal_gateway: The metal_gateway of this IPReservation.
        :param metro: The metro of this IPReservation.
        :param netmask: The netmask of this IPReservation.
        :param network: The network of this IPReservation.
        :param project: The project of this IPReservation.
        :param project_lite: The project_lite of this IPReservation.
        :param requested_by: The requested_by of this IPReservation.
        :param public: The public of this IPReservation.
        :param state: The state of this IPReservation.
        :param tags: The tags of this IPReservation.
        :param type: The type of this IPReservation.
        """
        self.openapi_types = {
            'addon': bool,
            'address': str,
            'address_family': int,
            'assignments': List[IPAssignment],
            'available': str,
            'bill': bool,
            'cidr': int,
            'created_at': datetime,
            'customdata': object,
            'enabled': bool,
            'details': str,
            'facility': IPReservationFacility,
            'gateway': str,
            'global_ip': bool,
            'href': str,
            'id': str,
            'manageable': bool,
            'management': bool,
            'metal_gateway': MetalGatewayLite,
            'metro': IPReservationMetro,
            'netmask': str,
            'network': str,
            'project': Project,
            'project_lite': Href,
            'requested_by': Href,
            'public': bool,
            'state': str,
            'tags': List[str],
            'type': str
        }

        self.attribute_map = {
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

        self._addon = addon
        self._address = address
        self._address_family = address_family
        self._assignments = assignments
        self._available = available
        self._bill = bill
        self._cidr = cidr
        self._created_at = created_at
        self._customdata = customdata
        self._enabled = enabled
        self._details = details
        self._facility = facility
        self._gateway = gateway
        self._global_ip = global_ip
        self._href = href
        self._id = id
        self._manageable = manageable
        self._management = management
        self._metal_gateway = metal_gateway
        self._metro = metro
        self._netmask = netmask
        self._network = network
        self._project = project
        self._project_lite = project_lite
        self._requested_by = requested_by
        self._public = public
        self._state = state
        self._tags = tags
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IPReservation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IPReservation of this IPReservation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def addon(self):
        """Gets the addon of this IPReservation.


        :return: The addon of this IPReservation.
        :rtype: bool
        """
        return self._addon

    @addon.setter
    def addon(self, addon):
        """Sets the addon of this IPReservation.


        :param addon: The addon of this IPReservation.
        :type addon: bool
        """

        self._addon = addon

    @property
    def address(self):
        """Gets the address of this IPReservation.


        :return: The address of this IPReservation.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IPReservation.


        :param address: The address of this IPReservation.
        :type address: str
        """

        self._address = address

    @property
    def address_family(self):
        """Gets the address_family of this IPReservation.


        :return: The address_family of this IPReservation.
        :rtype: int
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this IPReservation.


        :param address_family: The address_family of this IPReservation.
        :type address_family: int
        """

        self._address_family = address_family

    @property
    def assignments(self):
        """Gets the assignments of this IPReservation.


        :return: The assignments of this IPReservation.
        :rtype: List[IPAssignment]
        """
        return self._assignments

    @assignments.setter
    def assignments(self, assignments):
        """Sets the assignments of this IPReservation.


        :param assignments: The assignments of this IPReservation.
        :type assignments: List[IPAssignment]
        """

        self._assignments = assignments

    @property
    def available(self):
        """Gets the available of this IPReservation.


        :return: The available of this IPReservation.
        :rtype: str
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this IPReservation.


        :param available: The available of this IPReservation.
        :type available: str
        """

        self._available = available

    @property
    def bill(self):
        """Gets the bill of this IPReservation.


        :return: The bill of this IPReservation.
        :rtype: bool
        """
        return self._bill

    @bill.setter
    def bill(self, bill):
        """Sets the bill of this IPReservation.


        :param bill: The bill of this IPReservation.
        :type bill: bool
        """

        self._bill = bill

    @property
    def cidr(self):
        """Gets the cidr of this IPReservation.


        :return: The cidr of this IPReservation.
        :rtype: int
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this IPReservation.


        :param cidr: The cidr of this IPReservation.
        :type cidr: int
        """

        self._cidr = cidr

    @property
    def created_at(self):
        """Gets the created_at of this IPReservation.


        :return: The created_at of this IPReservation.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IPReservation.


        :param created_at: The created_at of this IPReservation.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def customdata(self):
        """Gets the customdata of this IPReservation.


        :return: The customdata of this IPReservation.
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this IPReservation.


        :param customdata: The customdata of this IPReservation.
        :type customdata: object
        """

        self._customdata = customdata

    @property
    def enabled(self):
        """Gets the enabled of this IPReservation.


        :return: The enabled of this IPReservation.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IPReservation.


        :param enabled: The enabled of this IPReservation.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def details(self):
        """Gets the details of this IPReservation.


        :return: The details of this IPReservation.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this IPReservation.


        :param details: The details of this IPReservation.
        :type details: str
        """

        self._details = details

    @property
    def facility(self):
        """Gets the facility of this IPReservation.


        :return: The facility of this IPReservation.
        :rtype: IPReservationFacility
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this IPReservation.


        :param facility: The facility of this IPReservation.
        :type facility: IPReservationFacility
        """

        self._facility = facility

    @property
    def gateway(self):
        """Gets the gateway of this IPReservation.


        :return: The gateway of this IPReservation.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this IPReservation.


        :param gateway: The gateway of this IPReservation.
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def global_ip(self):
        """Gets the global_ip of this IPReservation.


        :return: The global_ip of this IPReservation.
        :rtype: bool
        """
        return self._global_ip

    @global_ip.setter
    def global_ip(self, global_ip):
        """Sets the global_ip of this IPReservation.


        :param global_ip: The global_ip of this IPReservation.
        :type global_ip: bool
        """

        self._global_ip = global_ip

    @property
    def href(self):
        """Gets the href of this IPReservation.


        :return: The href of this IPReservation.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this IPReservation.


        :param href: The href of this IPReservation.
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this IPReservation.


        :return: The id of this IPReservation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IPReservation.


        :param id: The id of this IPReservation.
        :type id: str
        """

        self._id = id

    @property
    def manageable(self):
        """Gets the manageable of this IPReservation.


        :return: The manageable of this IPReservation.
        :rtype: bool
        """
        return self._manageable

    @manageable.setter
    def manageable(self, manageable):
        """Sets the manageable of this IPReservation.


        :param manageable: The manageable of this IPReservation.
        :type manageable: bool
        """

        self._manageable = manageable

    @property
    def management(self):
        """Gets the management of this IPReservation.


        :return: The management of this IPReservation.
        :rtype: bool
        """
        return self._management

    @management.setter
    def management(self, management):
        """Sets the management of this IPReservation.


        :param management: The management of this IPReservation.
        :type management: bool
        """

        self._management = management

    @property
    def metal_gateway(self):
        """Gets the metal_gateway of this IPReservation.


        :return: The metal_gateway of this IPReservation.
        :rtype: MetalGatewayLite
        """
        return self._metal_gateway

    @metal_gateway.setter
    def metal_gateway(self, metal_gateway):
        """Sets the metal_gateway of this IPReservation.


        :param metal_gateway: The metal_gateway of this IPReservation.
        :type metal_gateway: MetalGatewayLite
        """

        self._metal_gateway = metal_gateway

    @property
    def metro(self):
        """Gets the metro of this IPReservation.


        :return: The metro of this IPReservation.
        :rtype: IPReservationMetro
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this IPReservation.


        :param metro: The metro of this IPReservation.
        :type metro: IPReservationMetro
        """

        self._metro = metro

    @property
    def netmask(self):
        """Gets the netmask of this IPReservation.


        :return: The netmask of this IPReservation.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this IPReservation.


        :param netmask: The netmask of this IPReservation.
        :type netmask: str
        """

        self._netmask = netmask

    @property
    def network(self):
        """Gets the network of this IPReservation.


        :return: The network of this IPReservation.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this IPReservation.


        :param network: The network of this IPReservation.
        :type network: str
        """

        self._network = network

    @property
    def project(self):
        """Gets the project of this IPReservation.


        :return: The project of this IPReservation.
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this IPReservation.


        :param project: The project of this IPReservation.
        :type project: Project
        """

        self._project = project

    @property
    def project_lite(self):
        """Gets the project_lite of this IPReservation.


        :return: The project_lite of this IPReservation.
        :rtype: Href
        """
        return self._project_lite

    @project_lite.setter
    def project_lite(self, project_lite):
        """Sets the project_lite of this IPReservation.


        :param project_lite: The project_lite of this IPReservation.
        :type project_lite: Href
        """

        self._project_lite = project_lite

    @property
    def requested_by(self):
        """Gets the requested_by of this IPReservation.


        :return: The requested_by of this IPReservation.
        :rtype: Href
        """
        return self._requested_by

    @requested_by.setter
    def requested_by(self, requested_by):
        """Sets the requested_by of this IPReservation.


        :param requested_by: The requested_by of this IPReservation.
        :type requested_by: Href
        """

        self._requested_by = requested_by

    @property
    def public(self):
        """Gets the public of this IPReservation.


        :return: The public of this IPReservation.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this IPReservation.


        :param public: The public of this IPReservation.
        :type public: bool
        """

        self._public = public

    @property
    def state(self):
        """Gets the state of this IPReservation.


        :return: The state of this IPReservation.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this IPReservation.


        :param state: The state of this IPReservation.
        :type state: str
        """

        self._state = state

    @property
    def tags(self):
        """Gets the tags of this IPReservation.


        :return: The tags of this IPReservation.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this IPReservation.


        :param tags: The tags of this IPReservation.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this IPReservation.


        :return: The type of this IPReservation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IPReservation.


        :param type: The type of this IPReservation.
        :type type: str
        """
        allowed_values = ["global_ipv4", "public_ipv4", "private_ipv4", "public_ipv6"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
