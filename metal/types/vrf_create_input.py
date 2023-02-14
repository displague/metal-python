# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal import util


class VrfCreateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, ip_ranges: List[str]=None, local_asn: int=None, metro: str=None, name: str=None):
        """VrfCreateInput - a model defined in OpenAPI

        :param description: The description of this VrfCreateInput.
        :param ip_ranges: The ip_ranges of this VrfCreateInput.
        :param local_asn: The local_asn of this VrfCreateInput.
        :param metro: The metro of this VrfCreateInput.
        :param name: The name of this VrfCreateInput.
        """
        self.openapi_types = {
            'description': str,
            'ip_ranges': List[str],
            'local_asn': int,
            'metro': str,
            'name': str
        }

        self.attribute_map = {
            'description': 'description',
            'ip_ranges': 'ip_ranges',
            'local_asn': 'local_asn',
            'metro': 'metro',
            'name': 'name'
        }

        self._description = description
        self._ip_ranges = ip_ranges
        self._local_asn = local_asn
        self._metro = metro
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VrfCreateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VrfCreateInput of this VrfCreateInput.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this VrfCreateInput.


        :return: The description of this VrfCreateInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VrfCreateInput.


        :param description: The description of this VrfCreateInput.
        :type description: str
        """

        self._description = description

    @property
    def ip_ranges(self):
        """Gets the ip_ranges of this VrfCreateInput.

        A list of CIDR network addresses. Like [\"10.0.0.0/16\", \"2001:d78::/56\"]. IPv4 blocks must be between /8 and /29 in size. IPv6 blocks must be between /56 and /64. A VRF\\'s IP ranges must be defined in order to create VRF IP Reservations, which can then be used for Metal Gateways or Virtual Circuits.

        :return: The ip_ranges of this VrfCreateInput.
        :rtype: List[str]
        """
        return self._ip_ranges

    @ip_ranges.setter
    def ip_ranges(self, ip_ranges):
        """Sets the ip_ranges of this VrfCreateInput.

        A list of CIDR network addresses. Like [\"10.0.0.0/16\", \"2001:d78::/56\"]. IPv4 blocks must be between /8 and /29 in size. IPv6 blocks must be between /56 and /64. A VRF\\'s IP ranges must be defined in order to create VRF IP Reservations, which can then be used for Metal Gateways or Virtual Circuits.

        :param ip_ranges: The ip_ranges of this VrfCreateInput.
        :type ip_ranges: List[str]
        """

        self._ip_ranges = ip_ranges

    @property
    def local_asn(self):
        """Gets the local_asn of this VrfCreateInput.


        :return: The local_asn of this VrfCreateInput.
        :rtype: int
        """
        return self._local_asn

    @local_asn.setter
    def local_asn(self, local_asn):
        """Sets the local_asn of this VrfCreateInput.


        :param local_asn: The local_asn of this VrfCreateInput.
        :type local_asn: int
        """

        self._local_asn = local_asn

    @property
    def metro(self):
        """Gets the metro of this VrfCreateInput.

        The UUID (or metro code) for the Metro in which to create this VRF.

        :return: The metro of this VrfCreateInput.
        :rtype: str
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this VrfCreateInput.

        The UUID (or metro code) for the Metro in which to create this VRF.

        :param metro: The metro of this VrfCreateInput.
        :type metro: str
        """
        if metro is None:
            raise ValueError("Invalid value for `metro`, must not be `None`")

        self._metro = metro

    @property
    def name(self):
        """Gets the name of this VrfCreateInput.


        :return: The name of this VrfCreateInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VrfCreateInput.


        :param name: The name of this VrfCreateInput.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
