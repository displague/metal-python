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


class PortVlanAssignmentBatchVlanAssignments(object):
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
        'vlan': 'int',
        'state': 'str',
        'native': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'vlan': 'vlan',
        'state': 'state',
        'native': 'native'
    }

    def __init__(self, id=None, vlan=None, state=None, native=None, local_vars_configuration=None):  # noqa: E501
        """PortVlanAssignmentBatchVlanAssignments - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._vlan = None
        self._state = None
        self._native = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vlan is not None:
            self.vlan = vlan
        if state is not None:
            self.state = state
        if native is not None:
            self.native = native

    @property
    def id(self):
        """Gets the id of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501


        :return: The id of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortVlanAssignmentBatchVlanAssignments.


        :param id: The id of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def vlan(self):
        """Gets the vlan of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501


        :return: The vlan of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this PortVlanAssignmentBatchVlanAssignments.


        :param vlan: The vlan of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501
        :type vlan: int
        """

        self._vlan = vlan

    @property
    def state(self):
        """Gets the state of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501


        :return: The state of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PortVlanAssignmentBatchVlanAssignments.


        :param state: The state of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501
        :type state: str
        """
        allowed_values = ["assigned", "unassigned"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def native(self):
        """Gets the native of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501


        :return: The native of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501
        :rtype: bool
        """
        return self._native

    @native.setter
    def native(self, native):
        """Sets the native of this PortVlanAssignmentBatchVlanAssignments.


        :param native: The native of this PortVlanAssignmentBatchVlanAssignments.  # noqa: E501
        :type native: bool
        """

        self._native = native

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
        if not isinstance(other, PortVlanAssignmentBatchVlanAssignments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortVlanAssignmentBatchVlanAssignments):
            return True

        return self.to_dict() != other.to_dict()
