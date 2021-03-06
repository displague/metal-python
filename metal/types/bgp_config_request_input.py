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


class BgpConfigRequestInput(object):
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
        'deployment_type': 'str',
        'asn': 'int',
        'md5': 'str',
        'use_case': 'str'
    }

    attribute_map = {
        'deployment_type': 'deployment_type',
        'asn': 'asn',
        'md5': 'md5',
        'use_case': 'use_case'
    }

    def __init__(self, deployment_type=None, asn=None, md5=None, use_case=None, local_vars_configuration=None):  # noqa: E501
        """BgpConfigRequestInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._deployment_type = None
        self._asn = None
        self._md5 = None
        self._use_case = None
        self.discriminator = None

        self.deployment_type = deployment_type
        self.asn = asn
        if md5 is not None:
            self.md5 = md5
        if use_case is not None:
            self.use_case = use_case

    @property
    def deployment_type(self):
        """Gets the deployment_type of this BgpConfigRequestInput.  # noqa: E501


        :return: The deployment_type of this BgpConfigRequestInput.  # noqa: E501
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this BgpConfigRequestInput.


        :param deployment_type: The deployment_type of this BgpConfigRequestInput.  # noqa: E501
        :type deployment_type: str
        """
        if self.local_vars_configuration.client_side_validation and deployment_type is None:  # noqa: E501
            raise ValueError("Invalid value for `deployment_type`, must not be `None`")  # noqa: E501

        self._deployment_type = deployment_type

    @property
    def asn(self):
        """Gets the asn of this BgpConfigRequestInput.  # noqa: E501


        :return: The asn of this BgpConfigRequestInput.  # noqa: E501
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this BgpConfigRequestInput.


        :param asn: The asn of this BgpConfigRequestInput.  # noqa: E501
        :type asn: int
        """
        if self.local_vars_configuration.client_side_validation and asn is None:  # noqa: E501
            raise ValueError("Invalid value for `asn`, must not be `None`")  # noqa: E501

        self._asn = asn

    @property
    def md5(self):
        """Gets the md5 of this BgpConfigRequestInput.  # noqa: E501


        :return: The md5 of this BgpConfigRequestInput.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this BgpConfigRequestInput.


        :param md5: The md5 of this BgpConfigRequestInput.  # noqa: E501
        :type md5: str
        """

        self._md5 = md5

    @property
    def use_case(self):
        """Gets the use_case of this BgpConfigRequestInput.  # noqa: E501


        :return: The use_case of this BgpConfigRequestInput.  # noqa: E501
        :rtype: str
        """
        return self._use_case

    @use_case.setter
    def use_case(self, use_case):
        """Sets the use_case of this BgpConfigRequestInput.


        :param use_case: The use_case of this BgpConfigRequestInput.  # noqa: E501
        :type use_case: str
        """

        self._use_case = use_case

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
        if not isinstance(other, BgpConfigRequestInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BgpConfigRequestInput):
            return True

        return self.to_dict() != other.to_dict()
