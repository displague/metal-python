# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal import util


class Metro(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, country: str=None, id: str=None, name: str=None):
        """Metro - a model defined in OpenAPI

        :param code: The code of this Metro.
        :param country: The country of this Metro.
        :param id: The id of this Metro.
        :param name: The name of this Metro.
        """
        self.openapi_types = {
            'code': str,
            'country': str,
            'id': str,
            'name': str
        }

        self.attribute_map = {
            'code': 'code',
            'country': 'country',
            'id': 'id',
            'name': 'name'
        }

        self._code = code
        self._country = country
        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Metro':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Metro of this Metro.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this Metro.


        :return: The code of this Metro.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Metro.


        :param code: The code of this Metro.
        :type code: str
        """

        self._code = code

    @property
    def country(self):
        """Gets the country of this Metro.


        :return: The country of this Metro.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Metro.


        :param country: The country of this Metro.
        :type country: str
        """

        self._country = country

    @property
    def id(self):
        """Gets the id of this Metro.


        :return: The id of this Metro.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Metro.


        :param id: The id of this Metro.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Metro.


        :return: The name of this Metro.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Metro.


        :param name: The name of this Metro.
        :type name: str
        """

        self._name = name
