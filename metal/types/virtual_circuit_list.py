# coding: utf-8

"""
    Metal API

    This is the API for Equinix Metal. The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account.  The official API docs are hosted at <https://metal.equinix.com/developers/api>.   # noqa: E501

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


class VirtualCircuitList(object):
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
        'virtual_circuits': 'list[VirtualCircuit]'
    }

    attribute_map = {
        'virtual_circuits': 'virtual_circuits'
    }

    def __init__(self, virtual_circuits=None, local_vars_configuration=None):  # noqa: E501
        """VirtualCircuitList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._virtual_circuits = None
        self.discriminator = None

        if virtual_circuits is not None:
            self.virtual_circuits = virtual_circuits

    @property
    def virtual_circuits(self):
        """Gets the virtual_circuits of this VirtualCircuitList.  # noqa: E501


        :return: The virtual_circuits of this VirtualCircuitList.  # noqa: E501
        :rtype: list[VirtualCircuit]
        """
        return self._virtual_circuits

    @virtual_circuits.setter
    def virtual_circuits(self, virtual_circuits):
        """Sets the virtual_circuits of this VirtualCircuitList.


        :param virtual_circuits: The virtual_circuits of this VirtualCircuitList.  # noqa: E501
        :type virtual_circuits: list[VirtualCircuit]
        """

        self._virtual_circuits = virtual_circuits

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
        if not isinstance(other, VirtualCircuitList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualCircuitList):
            return True

        return self.to_dict() != other.to_dict()
