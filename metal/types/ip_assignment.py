# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal.types.href import Href
from metal.types.ip_assignment_metro import IPAssignmentMetro
from metal.types.parent_block import ParentBlock
from metal import util


class IPAssignment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: str=None, address_family: int=None, assigned_to: Href=None, cidr: int=None, created_at: datetime=None, enabled: bool=None, gateway: str=None, global_ip: bool=None, href: str=None, id: str=None, manageable: bool=None, management: bool=None, metro: IPAssignmentMetro=None, netmask: str=None, network: str=None, parent_block: ParentBlock=None, public: bool=None):
        """IPAssignment - a model defined in OpenAPI

        :param address: The address of this IPAssignment.
        :param address_family: The address_family of this IPAssignment.
        :param assigned_to: The assigned_to of this IPAssignment.
        :param cidr: The cidr of this IPAssignment.
        :param created_at: The created_at of this IPAssignment.
        :param enabled: The enabled of this IPAssignment.
        :param gateway: The gateway of this IPAssignment.
        :param global_ip: The global_ip of this IPAssignment.
        :param href: The href of this IPAssignment.
        :param id: The id of this IPAssignment.
        :param manageable: The manageable of this IPAssignment.
        :param management: The management of this IPAssignment.
        :param metro: The metro of this IPAssignment.
        :param netmask: The netmask of this IPAssignment.
        :param network: The network of this IPAssignment.
        :param parent_block: The parent_block of this IPAssignment.
        :param public: The public of this IPAssignment.
        """
        self.openapi_types = {
            'address': str,
            'address_family': int,
            'assigned_to': Href,
            'cidr': int,
            'created_at': datetime,
            'enabled': bool,
            'gateway': str,
            'global_ip': bool,
            'href': str,
            'id': str,
            'manageable': bool,
            'management': bool,
            'metro': IPAssignmentMetro,
            'netmask': str,
            'network': str,
            'parent_block': ParentBlock,
            'public': bool
        }

        self.attribute_map = {
            'address': 'address',
            'address_family': 'address_family',
            'assigned_to': 'assigned_to',
            'cidr': 'cidr',
            'created_at': 'created_at',
            'enabled': 'enabled',
            'gateway': 'gateway',
            'global_ip': 'global_ip',
            'href': 'href',
            'id': 'id',
            'manageable': 'manageable',
            'management': 'management',
            'metro': 'metro',
            'netmask': 'netmask',
            'network': 'network',
            'parent_block': 'parent_block',
            'public': 'public'
        }

        self._address = address
        self._address_family = address_family
        self._assigned_to = assigned_to
        self._cidr = cidr
        self._created_at = created_at
        self._enabled = enabled
        self._gateway = gateway
        self._global_ip = global_ip
        self._href = href
        self._id = id
        self._manageable = manageable
        self._management = management
        self._metro = metro
        self._netmask = netmask
        self._network = network
        self._parent_block = parent_block
        self._public = public

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IPAssignment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IPAssignment of this IPAssignment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this IPAssignment.


        :return: The address of this IPAssignment.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IPAssignment.


        :param address: The address of this IPAssignment.
        :type address: str
        """

        self._address = address

    @property
    def address_family(self):
        """Gets the address_family of this IPAssignment.


        :return: The address_family of this IPAssignment.
        :rtype: int
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this IPAssignment.


        :param address_family: The address_family of this IPAssignment.
        :type address_family: int
        """

        self._address_family = address_family

    @property
    def assigned_to(self):
        """Gets the assigned_to of this IPAssignment.


        :return: The assigned_to of this IPAssignment.
        :rtype: Href
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this IPAssignment.


        :param assigned_to: The assigned_to of this IPAssignment.
        :type assigned_to: Href
        """

        self._assigned_to = assigned_to

    @property
    def cidr(self):
        """Gets the cidr of this IPAssignment.


        :return: The cidr of this IPAssignment.
        :rtype: int
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this IPAssignment.


        :param cidr: The cidr of this IPAssignment.
        :type cidr: int
        """

        self._cidr = cidr

    @property
    def created_at(self):
        """Gets the created_at of this IPAssignment.


        :return: The created_at of this IPAssignment.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IPAssignment.


        :param created_at: The created_at of this IPAssignment.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def enabled(self):
        """Gets the enabled of this IPAssignment.


        :return: The enabled of this IPAssignment.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IPAssignment.


        :param enabled: The enabled of this IPAssignment.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def gateway(self):
        """Gets the gateway of this IPAssignment.


        :return: The gateway of this IPAssignment.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this IPAssignment.


        :param gateway: The gateway of this IPAssignment.
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def global_ip(self):
        """Gets the global_ip of this IPAssignment.


        :return: The global_ip of this IPAssignment.
        :rtype: bool
        """
        return self._global_ip

    @global_ip.setter
    def global_ip(self, global_ip):
        """Sets the global_ip of this IPAssignment.


        :param global_ip: The global_ip of this IPAssignment.
        :type global_ip: bool
        """

        self._global_ip = global_ip

    @property
    def href(self):
        """Gets the href of this IPAssignment.


        :return: The href of this IPAssignment.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this IPAssignment.


        :param href: The href of this IPAssignment.
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this IPAssignment.


        :return: The id of this IPAssignment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IPAssignment.


        :param id: The id of this IPAssignment.
        :type id: str
        """

        self._id = id

    @property
    def manageable(self):
        """Gets the manageable of this IPAssignment.


        :return: The manageable of this IPAssignment.
        :rtype: bool
        """
        return self._manageable

    @manageable.setter
    def manageable(self, manageable):
        """Sets the manageable of this IPAssignment.


        :param manageable: The manageable of this IPAssignment.
        :type manageable: bool
        """

        self._manageable = manageable

    @property
    def management(self):
        """Gets the management of this IPAssignment.


        :return: The management of this IPAssignment.
        :rtype: bool
        """
        return self._management

    @management.setter
    def management(self, management):
        """Sets the management of this IPAssignment.


        :param management: The management of this IPAssignment.
        :type management: bool
        """

        self._management = management

    @property
    def metro(self):
        """Gets the metro of this IPAssignment.


        :return: The metro of this IPAssignment.
        :rtype: IPAssignmentMetro
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this IPAssignment.


        :param metro: The metro of this IPAssignment.
        :type metro: IPAssignmentMetro
        """

        self._metro = metro

    @property
    def netmask(self):
        """Gets the netmask of this IPAssignment.


        :return: The netmask of this IPAssignment.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this IPAssignment.


        :param netmask: The netmask of this IPAssignment.
        :type netmask: str
        """

        self._netmask = netmask

    @property
    def network(self):
        """Gets the network of this IPAssignment.


        :return: The network of this IPAssignment.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this IPAssignment.


        :param network: The network of this IPAssignment.
        :type network: str
        """

        self._network = network

    @property
    def parent_block(self):
        """Gets the parent_block of this IPAssignment.


        :return: The parent_block of this IPAssignment.
        :rtype: ParentBlock
        """
        return self._parent_block

    @parent_block.setter
    def parent_block(self, parent_block):
        """Sets the parent_block of this IPAssignment.


        :param parent_block: The parent_block of this IPAssignment.
        :type parent_block: ParentBlock
        """

        self._parent_block = parent_block

    @property
    def public(self):
        """Gets the public of this IPAssignment.


        :return: The public of this IPAssignment.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this IPAssignment.


        :param public: The public of this IPAssignment.
        :type public: bool
        """

        self._public = public
