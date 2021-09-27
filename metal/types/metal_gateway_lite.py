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


class MetalGatewayLite(object):
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
        'state': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'gateway_address': 'str',
        'vlan': 'float',
        'href': 'str'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'gateway_address': 'gateway_address',
        'vlan': 'vlan',
        'href': 'href'
    }

    def __init__(self, id=None, state=None, created_at=None, updated_at=None, gateway_address=None, vlan=None, href=None, local_vars_configuration=None):  # noqa: E501
        """MetalGatewayLite - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._gateway_address = None
        self._vlan = None
        self._href = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if gateway_address is not None:
            self.gateway_address = gateway_address
        if vlan is not None:
            self.vlan = vlan
        if href is not None:
            self.href = href

    @property
    def id(self):
        """Gets the id of this MetalGatewayLite.  # noqa: E501


        :return: The id of this MetalGatewayLite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetalGatewayLite.


        :param id: The id of this MetalGatewayLite.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this MetalGatewayLite.  # noqa: E501

        The current state of the Metal Gateway. 'Ready' indicates the gateway record has been configured, but is currently not active on the network. 'Active' indicates the gateway has been configured on the network. 'Deleting' is a temporary state used to indicate that the gateway is in the process of being un-configured from the network, after which the gateway record will be deleted.  # noqa: E501

        :return: The state of this MetalGatewayLite.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MetalGatewayLite.

        The current state of the Metal Gateway. 'Ready' indicates the gateway record has been configured, but is currently not active on the network. 'Active' indicates the gateway has been configured on the network. 'Deleting' is a temporary state used to indicate that the gateway is in the process of being un-configured from the network, after which the gateway record will be deleted.  # noqa: E501

        :param state: The state of this MetalGatewayLite.  # noqa: E501
        :type state: str
        """
        allowed_values = ["ready", "active", "deleting"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def created_at(self):
        """Gets the created_at of this MetalGatewayLite.  # noqa: E501


        :return: The created_at of this MetalGatewayLite.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MetalGatewayLite.


        :param created_at: The created_at of this MetalGatewayLite.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this MetalGatewayLite.  # noqa: E501


        :return: The updated_at of this MetalGatewayLite.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this MetalGatewayLite.


        :param updated_at: The updated_at of this MetalGatewayLite.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def gateway_address(self):
        """Gets the gateway_address of this MetalGatewayLite.  # noqa: E501

        The gateway address with subnet CIDR value for this Metal Gateway. For example, a Metal Gateway using an IP reservation with block 10.1.2.0/27 would have a gateway address of 10.1.2.1/27.  # noqa: E501

        :return: The gateway_address of this MetalGatewayLite.  # noqa: E501
        :rtype: str
        """
        return self._gateway_address

    @gateway_address.setter
    def gateway_address(self, gateway_address):
        """Sets the gateway_address of this MetalGatewayLite.

        The gateway address with subnet CIDR value for this Metal Gateway. For example, a Metal Gateway using an IP reservation with block 10.1.2.0/27 would have a gateway address of 10.1.2.1/27.  # noqa: E501

        :param gateway_address: The gateway_address of this MetalGatewayLite.  # noqa: E501
        :type gateway_address: str
        """

        self._gateway_address = gateway_address

    @property
    def vlan(self):
        """Gets the vlan of this MetalGatewayLite.  # noqa: E501

        The VLAN id of the Virtual Network record associated to this Metal Gateway. Example: 1001.  # noqa: E501

        :return: The vlan of this MetalGatewayLite.  # noqa: E501
        :rtype: float
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this MetalGatewayLite.

        The VLAN id of the Virtual Network record associated to this Metal Gateway. Example: 1001.  # noqa: E501

        :param vlan: The vlan of this MetalGatewayLite.  # noqa: E501
        :type vlan: float
        """

        self._vlan = vlan

    @property
    def href(self):
        """Gets the href of this MetalGatewayLite.  # noqa: E501


        :return: The href of this MetalGatewayLite.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this MetalGatewayLite.


        :param href: The href of this MetalGatewayLite.  # noqa: E501
        :type href: str
        """

        self._href = href

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
        if not isinstance(other, MetalGatewayLite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetalGatewayLite):
            return True

        return self.to_dict() != other.to_dict()