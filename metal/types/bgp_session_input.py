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


class BGPSessionInput(object):
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
        'address_family': 'str',
        'default_route': 'bool'
    }

    attribute_map = {
        'address_family': 'address_family',
        'default_route': 'default_route'
    }

    def __init__(self, address_family=None, default_route=None, local_vars_configuration=None):  # noqa: E501
        """BGPSessionInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._address_family = None
        self._default_route = None
        self.discriminator = None

        if address_family is not None:
            self.address_family = address_family
        if default_route is not None:
            self.default_route = default_route

    @property
    def address_family(self):
        """Gets the address_family of this BGPSessionInput.  # noqa: E501


        :return: The address_family of this BGPSessionInput.  # noqa: E501
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this BGPSessionInput.


        :param address_family: The address_family of this BGPSessionInput.  # noqa: E501
        :type address_family: str
        """

        self._address_family = address_family

    @property
    def default_route(self):
        """Gets the default_route of this BGPSessionInput.  # noqa: E501


        :return: The default_route of this BGPSessionInput.  # noqa: E501
        :rtype: bool
        """
        return self._default_route

    @default_route.setter
    def default_route(self, default_route):
        """Sets the default_route of this BGPSessionInput.


        :param default_route: The default_route of this BGPSessionInput.  # noqa: E501
        :type default_route: bool
        """

        self._default_route = default_route

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
        if not isinstance(other, BGPSessionInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BGPSessionInput):
            return True

        return self.to_dict() != other.to_dict()