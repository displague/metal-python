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


class VirtualCircuit(object):
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
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'vnid': 'int',
        'nni_vlan': 'int',
        'speed': 'int',
        'tags': 'list[str]',
        'project': 'Href',
        'virtual_network': 'Href'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'vnid': 'vnid',
        'nni_vlan': 'nni_vlan',
        'speed': 'speed',
        'tags': 'tags',
        'project': 'project',
        'virtual_network': 'virtual_network'
    }

    def __init__(self, id=None, name=None, description=None, status=None, vnid=None, nni_vlan=None, speed=None, tags=None, project=None, virtual_network=None, local_vars_configuration=None):  # noqa: E501
        """VirtualCircuit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._vnid = None
        self._nni_vlan = None
        self._speed = None
        self._tags = None
        self._project = None
        self._virtual_network = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if vnid is not None:
            self.vnid = vnid
        if nni_vlan is not None:
            self.nni_vlan = nni_vlan
        if speed is not None:
            self.speed = speed
        if tags is not None:
            self.tags = tags
        if project is not None:
            self.project = project
        if virtual_network is not None:
            self.virtual_network = virtual_network

    @property
    def id(self):
        """Gets the id of this VirtualCircuit.  # noqa: E501


        :return: The id of this VirtualCircuit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualCircuit.


        :param id: The id of this VirtualCircuit.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VirtualCircuit.  # noqa: E501


        :return: The name of this VirtualCircuit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualCircuit.


        :param name: The name of this VirtualCircuit.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this VirtualCircuit.  # noqa: E501


        :return: The description of this VirtualCircuit.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualCircuit.


        :param description: The description of this VirtualCircuit.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this VirtualCircuit.  # noqa: E501


        :return: The status of this VirtualCircuit.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VirtualCircuit.


        :param status: The status of this VirtualCircuit.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def vnid(self):
        """Gets the vnid of this VirtualCircuit.  # noqa: E501


        :return: The vnid of this VirtualCircuit.  # noqa: E501
        :rtype: int
        """
        return self._vnid

    @vnid.setter
    def vnid(self, vnid):
        """Sets the vnid of this VirtualCircuit.


        :param vnid: The vnid of this VirtualCircuit.  # noqa: E501
        :type vnid: int
        """

        self._vnid = vnid

    @property
    def nni_vlan(self):
        """Gets the nni_vlan of this VirtualCircuit.  # noqa: E501


        :return: The nni_vlan of this VirtualCircuit.  # noqa: E501
        :rtype: int
        """
        return self._nni_vlan

    @nni_vlan.setter
    def nni_vlan(self, nni_vlan):
        """Sets the nni_vlan of this VirtualCircuit.


        :param nni_vlan: The nni_vlan of this VirtualCircuit.  # noqa: E501
        :type nni_vlan: int
        """

        self._nni_vlan = nni_vlan

    @property
    def speed(self):
        """Gets the speed of this VirtualCircuit.  # noqa: E501

        integer representing bps speed  # noqa: E501

        :return: The speed of this VirtualCircuit.  # noqa: E501
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this VirtualCircuit.

        integer representing bps speed  # noqa: E501

        :param speed: The speed of this VirtualCircuit.  # noqa: E501
        :type speed: int
        """

        self._speed = speed

    @property
    def tags(self):
        """Gets the tags of this VirtualCircuit.  # noqa: E501


        :return: The tags of this VirtualCircuit.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VirtualCircuit.


        :param tags: The tags of this VirtualCircuit.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def project(self):
        """Gets the project of this VirtualCircuit.  # noqa: E501


        :return: The project of this VirtualCircuit.  # noqa: E501
        :rtype: Href
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this VirtualCircuit.


        :param project: The project of this VirtualCircuit.  # noqa: E501
        :type project: Href
        """

        self._project = project

    @property
    def virtual_network(self):
        """Gets the virtual_network of this VirtualCircuit.  # noqa: E501


        :return: The virtual_network of this VirtualCircuit.  # noqa: E501
        :rtype: Href
        """
        return self._virtual_network

    @virtual_network.setter
    def virtual_network(self, virtual_network):
        """Sets the virtual_network of this VirtualCircuit.


        :param virtual_network: The virtual_network of this VirtualCircuit.  # noqa: E501
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
        if not isinstance(other, VirtualCircuit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualCircuit):
            return True

        return self.to_dict() != other.to_dict()
