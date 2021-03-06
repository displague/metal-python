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


class StaffProvider(object):
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
        'slug': 'str',
        'type': 'str',
        'contact_name': 'str',
        'contact_phone': 'str',
        'contact_email': 'str',
        'website_url': 'str',
        'logo_url': 'str',
        'address': 'StaffAddress'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'type': 'type',
        'contact_name': 'contact_name',
        'contact_phone': 'contact_phone',
        'contact_email': 'contact_email',
        'website_url': 'website_url',
        'logo_url': 'logo_url',
        'address': 'address'
    }

    def __init__(self, id=None, name=None, slug=None, type=None, contact_name=None, contact_phone=None, contact_email=None, website_url=None, logo_url=None, address=None, local_vars_configuration=None):  # noqa: E501
        """StaffProvider - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._slug = None
        self._type = None
        self._contact_name = None
        self._contact_phone = None
        self._contact_email = None
        self._website_url = None
        self._logo_url = None
        self._address = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if type is not None:
            self.type = type
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_phone is not None:
            self.contact_phone = contact_phone
        if contact_email is not None:
            self.contact_email = contact_email
        if website_url is not None:
            self.website_url = website_url
        if logo_url is not None:
            self.logo_url = logo_url
        if address is not None:
            self.address = address

    @property
    def id(self):
        """Gets the id of this StaffProvider.  # noqa: E501


        :return: The id of this StaffProvider.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StaffProvider.


        :param id: The id of this StaffProvider.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StaffProvider.  # noqa: E501


        :return: The name of this StaffProvider.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StaffProvider.


        :param name: The name of this StaffProvider.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this StaffProvider.  # noqa: E501


        :return: The slug of this StaffProvider.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this StaffProvider.


        :param slug: The slug of this StaffProvider.  # noqa: E501
        :type slug: str
        """

        self._slug = slug

    @property
    def type(self):
        """Gets the type of this StaffProvider.  # noqa: E501


        :return: The type of this StaffProvider.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StaffProvider.


        :param type: The type of this StaffProvider.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def contact_name(self):
        """Gets the contact_name of this StaffProvider.  # noqa: E501


        :return: The contact_name of this StaffProvider.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this StaffProvider.


        :param contact_name: The contact_name of this StaffProvider.  # noqa: E501
        :type contact_name: str
        """

        self._contact_name = contact_name

    @property
    def contact_phone(self):
        """Gets the contact_phone of this StaffProvider.  # noqa: E501


        :return: The contact_phone of this StaffProvider.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this StaffProvider.


        :param contact_phone: The contact_phone of this StaffProvider.  # noqa: E501
        :type contact_phone: str
        """

        self._contact_phone = contact_phone

    @property
    def contact_email(self):
        """Gets the contact_email of this StaffProvider.  # noqa: E501


        :return: The contact_email of this StaffProvider.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this StaffProvider.


        :param contact_email: The contact_email of this StaffProvider.  # noqa: E501
        :type contact_email: str
        """

        self._contact_email = contact_email

    @property
    def website_url(self):
        """Gets the website_url of this StaffProvider.  # noqa: E501


        :return: The website_url of this StaffProvider.  # noqa: E501
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this StaffProvider.


        :param website_url: The website_url of this StaffProvider.  # noqa: E501
        :type website_url: str
        """

        self._website_url = website_url

    @property
    def logo_url(self):
        """Gets the logo_url of this StaffProvider.  # noqa: E501


        :return: The logo_url of this StaffProvider.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this StaffProvider.


        :param logo_url: The logo_url of this StaffProvider.  # noqa: E501
        :type logo_url: str
        """

        self._logo_url = logo_url

    @property
    def address(self):
        """Gets the address of this StaffProvider.  # noqa: E501


        :return: The address of this StaffProvider.  # noqa: E501
        :rtype: StaffAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this StaffProvider.


        :param address: The address of this StaffProvider.  # noqa: E501
        :type address: StaffAddress
        """

        self._address = address

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
        if not isinstance(other, StaffProvider):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StaffProvider):
            return True

        return self.to_dict() != other.to_dict()
