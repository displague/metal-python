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


class ProjectUpdateInput(object):
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
        'payment_method_id': 'str',
        'backend_transfer_enabled': 'bool',
        'customdata': 'object'
    }

    attribute_map = {
        'name': 'name',
        'payment_method_id': 'payment_method_id',
        'backend_transfer_enabled': 'backend_transfer_enabled',
        'customdata': 'customdata'
    }

    def __init__(self, name=None, payment_method_id=None, backend_transfer_enabled=None, customdata=None, local_vars_configuration=None):  # noqa: E501
        """ProjectUpdateInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._payment_method_id = None
        self._backend_transfer_enabled = None
        self._customdata = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if backend_transfer_enabled is not None:
            self.backend_transfer_enabled = backend_transfer_enabled
        if customdata is not None:
            self.customdata = customdata

    @property
    def name(self):
        """Gets the name of this ProjectUpdateInput.  # noqa: E501


        :return: The name of this ProjectUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectUpdateInput.


        :param name: The name of this ProjectUpdateInput.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this ProjectUpdateInput.  # noqa: E501


        :return: The payment_method_id of this ProjectUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this ProjectUpdateInput.


        :param payment_method_id: The payment_method_id of this ProjectUpdateInput.  # noqa: E501
        :type payment_method_id: str
        """

        self._payment_method_id = payment_method_id

    @property
    def backend_transfer_enabled(self):
        """Gets the backend_transfer_enabled of this ProjectUpdateInput.  # noqa: E501


        :return: The backend_transfer_enabled of this ProjectUpdateInput.  # noqa: E501
        :rtype: bool
        """
        return self._backend_transfer_enabled

    @backend_transfer_enabled.setter
    def backend_transfer_enabled(self, backend_transfer_enabled):
        """Sets the backend_transfer_enabled of this ProjectUpdateInput.


        :param backend_transfer_enabled: The backend_transfer_enabled of this ProjectUpdateInput.  # noqa: E501
        :type backend_transfer_enabled: bool
        """

        self._backend_transfer_enabled = backend_transfer_enabled

    @property
    def customdata(self):
        """Gets the customdata of this ProjectUpdateInput.  # noqa: E501


        :return: The customdata of this ProjectUpdateInput.  # noqa: E501
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this ProjectUpdateInput.


        :param customdata: The customdata of this ProjectUpdateInput.  # noqa: E501
        :type customdata: object
        """

        self._customdata = customdata

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
        if not isinstance(other, ProjectUpdateInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectUpdateInput):
            return True

        return self.to_dict() != other.to_dict()
