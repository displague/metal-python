# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal import util


class DeviceCreateInputIpAddressesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address_family: float=None, cidr: float=None, ip_reservations: List[str]=None, public: bool=True):
        """DeviceCreateInputIpAddressesInner - a model defined in OpenAPI

        :param address_family: The address_family of this DeviceCreateInputIpAddressesInner.
        :param cidr: The cidr of this DeviceCreateInputIpAddressesInner.
        :param ip_reservations: The ip_reservations of this DeviceCreateInputIpAddressesInner.
        :param public: The public of this DeviceCreateInputIpAddressesInner.
        """
        self.openapi_types = {
            'address_family': float,
            'cidr': float,
            'ip_reservations': List[str],
            'public': bool
        }

        self.attribute_map = {
            'address_family': 'address_family',
            'cidr': 'cidr',
            'ip_reservations': 'ip_reservations',
            'public': 'public'
        }

        self._address_family = address_family
        self._cidr = cidr
        self._ip_reservations = ip_reservations
        self._public = public

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DeviceCreateInputIpAddressesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DeviceCreateInput_ip_addresses_inner of this DeviceCreateInputIpAddressesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address_family(self):
        """Gets the address_family of this DeviceCreateInputIpAddressesInner.

        Address Family for IP Address

        :return: The address_family of this DeviceCreateInputIpAddressesInner.
        :rtype: float
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this DeviceCreateInputIpAddressesInner.

        Address Family for IP Address

        :param address_family: The address_family of this DeviceCreateInputIpAddressesInner.
        :type address_family: float
        """
        allowed_values = [4, 6]  # noqa: E501
        if address_family not in allowed_values:
            raise ValueError(
                "Invalid value for `address_family` ({0}), must be one of {1}"
                .format(address_family, allowed_values)
            )

        self._address_family = address_family

    @property
    def cidr(self):
        """Gets the cidr of this DeviceCreateInputIpAddressesInner.

        Cidr Size for the IP Block created. Valid values depends on the operating system being provisioned. (28..32 for IPv4 addresses, 124..127 for IPv6 addresses)

        :return: The cidr of this DeviceCreateInputIpAddressesInner.
        :rtype: float
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this DeviceCreateInputIpAddressesInner.

        Cidr Size for the IP Block created. Valid values depends on the operating system being provisioned. (28..32 for IPv4 addresses, 124..127 for IPv6 addresses)

        :param cidr: The cidr of this DeviceCreateInputIpAddressesInner.
        :type cidr: float
        """

        self._cidr = cidr

    @property
    def ip_reservations(self):
        """Gets the ip_reservations of this DeviceCreateInputIpAddressesInner.

        UUIDs of any IP reservations to use when assigning IPs

        :return: The ip_reservations of this DeviceCreateInputIpAddressesInner.
        :rtype: List[str]
        """
        return self._ip_reservations

    @ip_reservations.setter
    def ip_reservations(self, ip_reservations):
        """Sets the ip_reservations of this DeviceCreateInputIpAddressesInner.

        UUIDs of any IP reservations to use when assigning IPs

        :param ip_reservations: The ip_reservations of this DeviceCreateInputIpAddressesInner.
        :type ip_reservations: List[str]
        """

        self._ip_reservations = ip_reservations

    @property
    def public(self):
        """Gets the public of this DeviceCreateInputIpAddressesInner.

        Address Type for IP Address

        :return: The public of this DeviceCreateInputIpAddressesInner.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this DeviceCreateInputIpAddressesInner.

        Address Type for IP Address

        :param public: The public of this DeviceCreateInputIpAddressesInner.
        :type public: bool
        """

        self._public = public
