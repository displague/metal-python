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


class PortVlanAssignment(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'native': 'bool',
        'state': 'str',
        'vlan': 'int',
        'port': 'Href',
        'virtual_network': 'Href'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'native': 'native',
        'state': 'state',
        'vlan': 'vlan',
        'port': 'port',
        'virtual_network': 'virtual_network'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, native=None, state=None, vlan=None, port=None, virtual_network=None, local_vars_configuration=None):  # noqa: E501
        """PortVlanAssignment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_at = None
        self._updated_at = None
        self._native = None
        self._state = None
        self._vlan = None
        self._port = None
        self._virtual_network = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if native is not None:
            self.native = native
        if state is not None:
            self.state = state
        if vlan is not None:
            self.vlan = vlan
        if port is not None:
            self.port = port
        if virtual_network is not None:
            self.virtual_network = virtual_network

    @property
    def id(self):
        """Gets the id of this PortVlanAssignment.  # noqa: E501


        :return: The id of this PortVlanAssignment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortVlanAssignment.


        :param id: The id of this PortVlanAssignment.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this PortVlanAssignment.  # noqa: E501


        :return: The created_at of this PortVlanAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PortVlanAssignment.


        :param created_at: The created_at of this PortVlanAssignment.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PortVlanAssignment.  # noqa: E501


        :return: The updated_at of this PortVlanAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PortVlanAssignment.


        :param updated_at: The updated_at of this PortVlanAssignment.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def native(self):
        """Gets the native of this PortVlanAssignment.  # noqa: E501


        :return: The native of this PortVlanAssignment.  # noqa: E501
        :rtype: bool
        """
        return self._native

    @native.setter
    def native(self, native):
        """Sets the native of this PortVlanAssignment.


        :param native: The native of this PortVlanAssignment.  # noqa: E501
        :type native: bool
        """

        self._native = native

    @property
    def state(self):
        """Gets the state of this PortVlanAssignment.  # noqa: E501


        :return: The state of this PortVlanAssignment.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PortVlanAssignment.


        :param state: The state of this PortVlanAssignment.  # noqa: E501
        :type state: str
        """
        allowed_values = ["assigned", "unassigning"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def vlan(self):
        """Gets the vlan of this PortVlanAssignment.  # noqa: E501


        :return: The vlan of this PortVlanAssignment.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this PortVlanAssignment.


        :param vlan: The vlan of this PortVlanAssignment.  # noqa: E501
        :type vlan: int
        """

        self._vlan = vlan

    @property
    def port(self):
        """Gets the port of this PortVlanAssignment.  # noqa: E501


        :return: The port of this PortVlanAssignment.  # noqa: E501
        :rtype: Href
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PortVlanAssignment.


        :param port: The port of this PortVlanAssignment.  # noqa: E501
        :type port: Href
        """

        self._port = port

    @property
    def virtual_network(self):
        """Gets the virtual_network of this PortVlanAssignment.  # noqa: E501


        :return: The virtual_network of this PortVlanAssignment.  # noqa: E501
        :rtype: Href
        """
        return self._virtual_network

    @virtual_network.setter
    def virtual_network(self, virtual_network):
        """Sets the virtual_network of this PortVlanAssignment.


        :param virtual_network: The virtual_network of this PortVlanAssignment.  # noqa: E501
        :type virtual_network: Href
        """

        self._virtual_network = virtual_network

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
        if not isinstance(other, PortVlanAssignment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortVlanAssignment):
            return True

        return self.to_dict() != other.to_dict()
