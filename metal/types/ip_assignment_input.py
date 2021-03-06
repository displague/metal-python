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


class IPAssignmentInput(object):
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
        'address': 'str',
        'manageable': 'bool',
        'customdata': 'object'
    }

    attribute_map = {
        'address': 'address',
        'manageable': 'manageable',
        'customdata': 'customdata'
    }

    def __init__(self, address=None, manageable=None, customdata=None, local_vars_configuration=None):  # noqa: E501
        """IPAssignmentInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._manageable = None
        self._customdata = None
        self.discriminator = None

        self.address = address
        if manageable is not None:
            self.manageable = manageable
        if customdata is not None:
            self.customdata = customdata

    @property
    def address(self):
        """Gets the address of this IPAssignmentInput.  # noqa: E501


        :return: The address of this IPAssignmentInput.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IPAssignmentInput.


        :param address: The address of this IPAssignmentInput.  # noqa: E501
        :type address: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def manageable(self):
        """Gets the manageable of this IPAssignmentInput.  # noqa: E501


        :return: The manageable of this IPAssignmentInput.  # noqa: E501
        :rtype: bool
        """
        return self._manageable

    @manageable.setter
    def manageable(self, manageable):
        """Sets the manageable of this IPAssignmentInput.


        :param manageable: The manageable of this IPAssignmentInput.  # noqa: E501
        :type manageable: bool
        """

        self._manageable = manageable

    @property
    def customdata(self):
        """Gets the customdata of this IPAssignmentInput.  # noqa: E501


        :return: The customdata of this IPAssignmentInput.  # noqa: E501
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this IPAssignmentInput.


        :param customdata: The customdata of this IPAssignmentInput.  # noqa: E501
        :type customdata: object
        """

        self._customdata = customdata

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
        if not isinstance(other, IPAssignmentInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IPAssignmentInput):
            return True

        return self.to_dict() != other.to_dict()
