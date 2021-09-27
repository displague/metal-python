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


class SelfServiceReservationItemResponse(object):
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
        'metro_id': 'str',
        'metro_code': 'str',
        'metro_name': 'str',
        'plan_id': 'str',
        'plan_name': 'str',
        'plan_slug': 'str',
        'quantity': 'int',
        'amount': 'float',
        'term': 'str'
    }

    attribute_map = {
        'id': 'id',
        'metro_id': 'metro_id',
        'metro_code': 'metro_code',
        'metro_name': 'metro_name',
        'plan_id': 'plan_id',
        'plan_name': 'plan_name',
        'plan_slug': 'plan_slug',
        'quantity': 'quantity',
        'amount': 'amount',
        'term': 'term'
    }

    def __init__(self, id=None, metro_id=None, metro_code=None, metro_name=None, plan_id=None, plan_name=None, plan_slug=None, quantity=None, amount=None, term=None, local_vars_configuration=None):  # noqa: E501
        """SelfServiceReservationItemResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._metro_id = None
        self._metro_code = None
        self._metro_name = None
        self._plan_id = None
        self._plan_name = None
        self._plan_slug = None
        self._quantity = None
        self._amount = None
        self._term = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if metro_id is not None:
            self.metro_id = metro_id
        if metro_code is not None:
            self.metro_code = metro_code
        if metro_name is not None:
            self.metro_name = metro_name
        if plan_id is not None:
            self.plan_id = plan_id
        if plan_name is not None:
            self.plan_name = plan_name
        if plan_slug is not None:
            self.plan_slug = plan_slug
        if quantity is not None:
            self.quantity = quantity
        if amount is not None:
            self.amount = amount
        if term is not None:
            self.term = term

    @property
    def id(self):
        """Gets the id of this SelfServiceReservationItemResponse.  # noqa: E501


        :return: The id of this SelfServiceReservationItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SelfServiceReservationItemResponse.


        :param id: The id of this SelfServiceReservationItemResponse.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def metro_id(self):
        """Gets the metro_id of this SelfServiceReservationItemResponse.  # noqa: E501


        :return: The metro_id of this SelfServiceReservationItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._metro_id

    @metro_id.setter
    def metro_id(self, metro_id):
        """Sets the metro_id of this SelfServiceReservationItemResponse.


        :param metro_id: The metro_id of this SelfServiceReservationItemResponse.  # noqa: E501
        :type metro_id: str
        """

        self._metro_id = metro_id

    @property
    def metro_code(self):
        """Gets the metro_code of this SelfServiceReservationItemResponse.  # noqa: E501


        :return: The metro_code of this SelfServiceReservationItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._metro_code

    @metro_code.setter
    def metro_code(self, metro_code):
        """Sets the metro_code of this SelfServiceReservationItemResponse.


        :param metro_code: The metro_code of this SelfServiceReservationItemResponse.  # noqa: E501
        :type metro_code: str
        """

        self._metro_code = metro_code

    @property
    def metro_name(self):
        """Gets the metro_name of this SelfServiceReservationItemResponse.  # noqa: E501


        :return: The metro_name of this SelfServiceReservationItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._metro_name

    @metro_name.setter
    def metro_name(self, metro_name):
        """Sets the metro_name of this SelfServiceReservationItemResponse.


        :param metro_name: The metro_name of this SelfServiceReservationItemResponse.  # noqa: E501
        :type metro_name: str
        """

        self._metro_name = metro_name

    @property
    def plan_id(self):
        """Gets the plan_id of this SelfServiceReservationItemResponse.  # noqa: E501


        :return: The plan_id of this SelfServiceReservationItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this SelfServiceReservationItemResponse.


        :param plan_id: The plan_id of this SelfServiceReservationItemResponse.  # noqa: E501
        :type plan_id: str
        """

        self._plan_id = plan_id

    @property
    def plan_name(self):
        """Gets the plan_name of this SelfServiceReservationItemResponse.  # noqa: E501


        :return: The plan_name of this SelfServiceReservationItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this SelfServiceReservationItemResponse.


        :param plan_name: The plan_name of this SelfServiceReservationItemResponse.  # noqa: E501
        :type plan_name: str
        """

        self._plan_name = plan_name

    @property
    def plan_slug(self):
        """Gets the plan_slug of this SelfServiceReservationItemResponse.  # noqa: E501


        :return: The plan_slug of this SelfServiceReservationItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._plan_slug

    @plan_slug.setter
    def plan_slug(self, plan_slug):
        """Sets the plan_slug of this SelfServiceReservationItemResponse.


        :param plan_slug: The plan_slug of this SelfServiceReservationItemResponse.  # noqa: E501
        :type plan_slug: str
        """

        self._plan_slug = plan_slug

    @property
    def quantity(self):
        """Gets the quantity of this SelfServiceReservationItemResponse.  # noqa: E501


        :return: The quantity of this SelfServiceReservationItemResponse.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SelfServiceReservationItemResponse.


        :param quantity: The quantity of this SelfServiceReservationItemResponse.  # noqa: E501
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def amount(self):
        """Gets the amount of this SelfServiceReservationItemResponse.  # noqa: E501


        :return: The amount of this SelfServiceReservationItemResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SelfServiceReservationItemResponse.


        :param amount: The amount of this SelfServiceReservationItemResponse.  # noqa: E501
        :type amount: float
        """

        self._amount = amount

    @property
    def term(self):
        """Gets the term of this SelfServiceReservationItemResponse.  # noqa: E501


        :return: The term of this SelfServiceReservationItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this SelfServiceReservationItemResponse.


        :param term: The term of this SelfServiceReservationItemResponse.  # noqa: E501
        :type term: str
        """

        self._term = term

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
        if not isinstance(other, SelfServiceReservationItemResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SelfServiceReservationItemResponse):
            return True

        return self.to_dict() != other.to_dict()