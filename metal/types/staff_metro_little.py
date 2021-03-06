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


class StaffMetroLittle(object):
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
        'code': 'str',
        'features': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'features': 'features'
    }

    def __init__(self, id=None, name=None, code=None, features=None, local_vars_configuration=None):  # noqa: E501
        """StaffMetroLittle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._code = None
        self._features = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if features is not None:
            self.features = features

    @property
    def id(self):
        """Gets the id of this StaffMetroLittle.  # noqa: E501


        :return: The id of this StaffMetroLittle.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StaffMetroLittle.


        :param id: The id of this StaffMetroLittle.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StaffMetroLittle.  # noqa: E501


        :return: The name of this StaffMetroLittle.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StaffMetroLittle.


        :param name: The name of this StaffMetroLittle.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this StaffMetroLittle.  # noqa: E501


        :return: The code of this StaffMetroLittle.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StaffMetroLittle.


        :param code: The code of this StaffMetroLittle.  # noqa: E501
        :type code: str
        """

        self._code = code

    @property
    def features(self):
        """Gets the features of this StaffMetroLittle.  # noqa: E501


        :return: The features of this StaffMetroLittle.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this StaffMetroLittle.


        :param features: The features of this StaffMetroLittle.  # noqa: E501
        :type features: list[str]
        """

        self._features = features

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
        if not isinstance(other, StaffMetroLittle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StaffMetroLittle):
            return True

        return self.to_dict() != other.to_dict()
