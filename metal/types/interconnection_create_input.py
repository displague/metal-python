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


class InterconnectionCreateInput(object):
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
        'name': 'str',
        'description': 'str',
        'facility': 'str',
        'metro': 'str',
        'type': 'str',
        'redundancy': 'str',
        'contact_email': 'str',
        'project': 'str',
        'speed': 'str',
        'tags': 'list[str]',
        'mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'facility': 'facility',
        'metro': 'metro',
        'type': 'type',
        'redundancy': 'redundancy',
        'contact_email': 'contact_email',
        'project': 'project',
        'speed': 'speed',
        'tags': 'tags',
        'mode': 'mode'
    }

    def __init__(self, name=None, description=None, facility=None, metro=None, type=None, redundancy=None, contact_email=None, project=None, speed=None, tags=None, mode=None, local_vars_configuration=None):  # noqa: E501
        """InterconnectionCreateInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._facility = None
        self._metro = None
        self._type = None
        self._redundancy = None
        self._contact_email = None
        self._project = None
        self._speed = None
        self._tags = None
        self._mode = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.facility = facility
        if metro is not None:
            self.metro = metro
        self.type = type
        self.redundancy = redundancy
        if contact_email is not None:
            self.contact_email = contact_email
        if project is not None:
            self.project = project
        if speed is not None:
            self.speed = speed
        if tags is not None:
            self.tags = tags
        if mode is not None:
            self.mode = mode

    @property
    def name(self):
        """Gets the name of this InterconnectionCreateInput.  # noqa: E501


        :return: The name of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InterconnectionCreateInput.


        :param name: The name of this InterconnectionCreateInput.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this InterconnectionCreateInput.  # noqa: E501


        :return: The description of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InterconnectionCreateInput.


        :param description: The description of this InterconnectionCreateInput.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def facility(self):
        """Gets the facility of this InterconnectionCreateInput.  # noqa: E501

        A Facility ID or code.  # noqa: E501

        :return: The facility of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this InterconnectionCreateInput.

        A Facility ID or code.  # noqa: E501

        :param facility: The facility of this InterconnectionCreateInput.  # noqa: E501
        :type facility: str
        """
        if self.local_vars_configuration.client_side_validation and facility is None:  # noqa: E501
            raise ValueError("Invalid value for `facility`, must not be `None`")  # noqa: E501

        self._facility = facility

    @property
    def metro(self):
        """Gets the metro of this InterconnectionCreateInput.  # noqa: E501

        A Metro ID or code. Required for creating a connection, unless creating with facility.  # noqa: E501

        :return: The metro of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this InterconnectionCreateInput.

        A Metro ID or code. Required for creating a connection, unless creating with facility.  # noqa: E501

        :param metro: The metro of this InterconnectionCreateInput.  # noqa: E501
        :type metro: str
        """

        self._metro = metro

    @property
    def type(self):
        """Gets the type of this InterconnectionCreateInput.  # noqa: E501

        Either 'shared' or 'dedicated'.  # noqa: E501

        :return: The type of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InterconnectionCreateInput.

        Either 'shared' or 'dedicated'.  # noqa: E501

        :param type: The type of this InterconnectionCreateInput.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def redundancy(self):
        """Gets the redundancy of this InterconnectionCreateInput.  # noqa: E501

        Either 'primary' or 'redundant'.  # noqa: E501

        :return: The redundancy of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._redundancy

    @redundancy.setter
    def redundancy(self, redundancy):
        """Sets the redundancy of this InterconnectionCreateInput.

        Either 'primary' or 'redundant'.  # noqa: E501

        :param redundancy: The redundancy of this InterconnectionCreateInput.  # noqa: E501
        :type redundancy: str
        """
        if self.local_vars_configuration.client_side_validation and redundancy is None:  # noqa: E501
            raise ValueError("Invalid value for `redundancy`, must not be `None`")  # noqa: E501

        self._redundancy = redundancy

    @property
    def contact_email(self):
        """Gets the contact_email of this InterconnectionCreateInput.  # noqa: E501


        :return: The contact_email of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this InterconnectionCreateInput.


        :param contact_email: The contact_email of this InterconnectionCreateInput.  # noqa: E501
        :type contact_email: str
        """

        self._contact_email = contact_email

    @property
    def project(self):
        """Gets the project of this InterconnectionCreateInput.  # noqa: E501


        :return: The project of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this InterconnectionCreateInput.


        :param project: The project of this InterconnectionCreateInput.  # noqa: E501
        :type project: str
        """

        self._project = project

    @property
    def speed(self):
        """Gets the speed of this InterconnectionCreateInput.  # noqa: E501

        A connection speed, in bps, mbps, or gbps. Ex: '100000000' or '100 mbps'.  # noqa: E501

        :return: The speed of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this InterconnectionCreateInput.

        A connection speed, in bps, mbps, or gbps. Ex: '100000000' or '100 mbps'.  # noqa: E501

        :param speed: The speed of this InterconnectionCreateInput.  # noqa: E501
        :type speed: str
        """

        self._speed = speed

    @property
    def tags(self):
        """Gets the tags of this InterconnectionCreateInput.  # noqa: E501


        :return: The tags of this InterconnectionCreateInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InterconnectionCreateInput.


        :param tags: The tags of this InterconnectionCreateInput.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def mode(self):
        """Gets the mode of this InterconnectionCreateInput.  # noqa: E501

        The mode of the connection (only relevant to dedicated connections). Shared connections won't have this field. Can be either 'standard' or 'tunnel'.   The default mode of a dedicated connection is 'standard'. The mode can only be changed when there are no associated virtual circuits on the connection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances.  # noqa: E501

        :return: The mode of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this InterconnectionCreateInput.

        The mode of the connection (only relevant to dedicated connections). Shared connections won't have this field. Can be either 'standard' or 'tunnel'.   The default mode of a dedicated connection is 'standard'. The mode can only be changed when there are no associated virtual circuits on the connection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances.  # noqa: E501

        :param mode: The mode of this InterconnectionCreateInput.  # noqa: E501
        :type mode: str
        """
        allowed_values = ["standard", "tunnel"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

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
        if not isinstance(other, InterconnectionCreateInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InterconnectionCreateInput):
            return True

        return self.to_dict() != other.to_dict()
