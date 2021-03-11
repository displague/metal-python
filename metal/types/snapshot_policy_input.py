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


class SnapshotPolicyInput(object):
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
        'snapshot_count': 'int',
        'snapshot_frequency': 'str'
    }

    attribute_map = {
        'snapshot_count': 'snapshot_count',
        'snapshot_frequency': 'snapshot_frequency'
    }

    def __init__(self, snapshot_count=None, snapshot_frequency=None, local_vars_configuration=None):  # noqa: E501
        """SnapshotPolicyInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._snapshot_count = None
        self._snapshot_frequency = None
        self.discriminator = None

        if snapshot_count is not None:
            self.snapshot_count = snapshot_count
        if snapshot_frequency is not None:
            self.snapshot_frequency = snapshot_frequency

    @property
    def snapshot_count(self):
        """Gets the snapshot_count of this SnapshotPolicyInput.  # noqa: E501


        :return: The snapshot_count of this SnapshotPolicyInput.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_count

    @snapshot_count.setter
    def snapshot_count(self, snapshot_count):
        """Sets the snapshot_count of this SnapshotPolicyInput.


        :param snapshot_count: The snapshot_count of this SnapshotPolicyInput.  # noqa: E501
        :type snapshot_count: int
        """

        self._snapshot_count = snapshot_count

    @property
    def snapshot_frequency(self):
        """Gets the snapshot_frequency of this SnapshotPolicyInput.  # noqa: E501


        :return: The snapshot_frequency of this SnapshotPolicyInput.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_frequency

    @snapshot_frequency.setter
    def snapshot_frequency(self, snapshot_frequency):
        """Sets the snapshot_frequency of this SnapshotPolicyInput.


        :param snapshot_frequency: The snapshot_frequency of this SnapshotPolicyInput.  # noqa: E501
        :type snapshot_frequency: str
        """

        self._snapshot_frequency = snapshot_frequency

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
        if not isinstance(other, SnapshotPolicyInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotPolicyInput):
            return True

        return self.to_dict() != other.to_dict()