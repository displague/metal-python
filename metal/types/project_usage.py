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


class ProjectUsage(object):
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
        'facility': 'str',
        'type': 'str',
        'name': 'str',
        'plan': 'str',
        'plan_version': 'str',
        'quantity': 'str',
        'unit': 'str',
        'price': 'str',
        'total': 'str'
    }

    attribute_map = {
        'facility': 'facility',
        'type': 'type',
        'name': 'name',
        'plan': 'plan',
        'plan_version': 'plan_version',
        'quantity': 'quantity',
        'unit': 'unit',
        'price': 'price',
        'total': 'total'
    }

    def __init__(self, facility=None, type=None, name=None, plan=None, plan_version=None, quantity=None, unit=None, price=None, total=None, local_vars_configuration=None):  # noqa: E501
        """ProjectUsage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._facility = None
        self._type = None
        self._name = None
        self._plan = None
        self._plan_version = None
        self._quantity = None
        self._unit = None
        self._price = None
        self._total = None
        self.discriminator = None

        if facility is not None:
            self.facility = facility
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if plan is not None:
            self.plan = plan
        if plan_version is not None:
            self.plan_version = plan_version
        if quantity is not None:
            self.quantity = quantity
        if unit is not None:
            self.unit = unit
        if price is not None:
            self.price = price
        if total is not None:
            self.total = total

    @property
    def facility(self):
        """Gets the facility of this ProjectUsage.  # noqa: E501


        :return: The facility of this ProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this ProjectUsage.


        :param facility: The facility of this ProjectUsage.  # noqa: E501
        :type facility: str
        """

        self._facility = facility

    @property
    def type(self):
        """Gets the type of this ProjectUsage.  # noqa: E501


        :return: The type of this ProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProjectUsage.


        :param type: The type of this ProjectUsage.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this ProjectUsage.  # noqa: E501


        :return: The name of this ProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectUsage.


        :param name: The name of this ProjectUsage.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def plan(self):
        """Gets the plan of this ProjectUsage.  # noqa: E501


        :return: The plan of this ProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this ProjectUsage.


        :param plan: The plan of this ProjectUsage.  # noqa: E501
        :type plan: str
        """

        self._plan = plan

    @property
    def plan_version(self):
        """Gets the plan_version of this ProjectUsage.  # noqa: E501


        :return: The plan_version of this ProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._plan_version

    @plan_version.setter
    def plan_version(self, plan_version):
        """Sets the plan_version of this ProjectUsage.


        :param plan_version: The plan_version of this ProjectUsage.  # noqa: E501
        :type plan_version: str
        """

        self._plan_version = plan_version

    @property
    def quantity(self):
        """Gets the quantity of this ProjectUsage.  # noqa: E501


        :return: The quantity of this ProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ProjectUsage.


        :param quantity: The quantity of this ProjectUsage.  # noqa: E501
        :type quantity: str
        """

        self._quantity = quantity

    @property
    def unit(self):
        """Gets the unit of this ProjectUsage.  # noqa: E501


        :return: The unit of this ProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ProjectUsage.


        :param unit: The unit of this ProjectUsage.  # noqa: E501
        :type unit: str
        """

        self._unit = unit

    @property
    def price(self):
        """Gets the price of this ProjectUsage.  # noqa: E501


        :return: The price of this ProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ProjectUsage.


        :param price: The price of this ProjectUsage.  # noqa: E501
        :type price: str
        """

        self._price = price

    @property
    def total(self):
        """Gets the total of this ProjectUsage.  # noqa: E501


        :return: The total of this ProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ProjectUsage.


        :param total: The total of this ProjectUsage.  # noqa: E501
        :type total: str
        """

        self._total = total

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
        if not isinstance(other, ProjectUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectUsage):
            return True

        return self.to_dict() != other.to_dict()
