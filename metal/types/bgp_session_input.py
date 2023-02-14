# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal import util


class BGPSessionInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address_family: str=None, default_route: bool=False):
        """BGPSessionInput - a model defined in OpenAPI

        :param address_family: The address_family of this BGPSessionInput.
        :param default_route: The default_route of this BGPSessionInput.
        """
        self.openapi_types = {
            'address_family': str,
            'default_route': bool
        }

        self.attribute_map = {
            'address_family': 'address_family',
            'default_route': 'default_route'
        }

        self._address_family = address_family
        self._default_route = default_route

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BGPSessionInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BGPSessionInput of this BGPSessionInput.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address_family(self):
        """Gets the address_family of this BGPSessionInput.

        Address family for BGP session.

        :return: The address_family of this BGPSessionInput.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this BGPSessionInput.

        Address family for BGP session.

        :param address_family: The address_family of this BGPSessionInput.
        :type address_family: str
        """
        allowed_values = ["ipv4", "ipv6"]  # noqa: E501
        if address_family not in allowed_values:
            raise ValueError(
                "Invalid value for `address_family` ({0}), must be one of {1}"
                .format(address_family, allowed_values)
            )

        self._address_family = address_family

    @property
    def default_route(self):
        """Gets the default_route of this BGPSessionInput.

        Set the default route policy.

        :return: The default_route of this BGPSessionInput.
        :rtype: bool
        """
        return self._default_route

    @default_route.setter
    def default_route(self, default_route):
        """Sets the default_route of this BGPSessionInput.

        Set the default route policy.

        :param default_route: The default_route of this BGPSessionInput.
        :type default_route: bool
        """

        self._default_route = default_route
