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


class GlobalBgpRange(object):
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
        'address_family': 'int',
        'range': 'str',
        'href': 'str'
    }

    attribute_map = {
        'id': 'id',
        'address_family': 'address_family',
        'range': 'range',
        'href': 'href'
    }

    def __init__(self, id=None, address_family=None, range=None, href=None, local_vars_configuration=None):  # noqa: E501
        """GlobalBgpRange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._address_family = None
        self._range = None
        self._href = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if address_family is not None:
            self.address_family = address_family
        if range is not None:
            self.range = range
        if href is not None:
            self.href = href

    @property
    def id(self):
        """Gets the id of this GlobalBgpRange.  # noqa: E501


        :return: The id of this GlobalBgpRange.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GlobalBgpRange.


        :param id: The id of this GlobalBgpRange.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def address_family(self):
        """Gets the address_family of this GlobalBgpRange.  # noqa: E501


        :return: The address_family of this GlobalBgpRange.  # noqa: E501
        :rtype: int
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this GlobalBgpRange.


        :param address_family: The address_family of this GlobalBgpRange.  # noqa: E501
        :type address_family: int
        """

        self._address_family = address_family

    @property
    def range(self):
        """Gets the range of this GlobalBgpRange.  # noqa: E501


        :return: The range of this GlobalBgpRange.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this GlobalBgpRange.


        :param range: The range of this GlobalBgpRange.  # noqa: E501
        :type range: str
        """

        self._range = range

    @property
    def href(self):
        """Gets the href of this GlobalBgpRange.  # noqa: E501


        :return: The href of this GlobalBgpRange.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this GlobalBgpRange.


        :param href: The href of this GlobalBgpRange.  # noqa: E501
        :type href: str
        """

        self._href = href

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
        if not isinstance(other, GlobalBgpRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlobalBgpRange):
            return True

        return self.to_dict() != other.to_dict()
