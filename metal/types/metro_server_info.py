# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal import util


class MetroServerInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, metro: str=None, plan: str=None, quantity: str=None):
        """MetroServerInfo - a model defined in OpenAPI

        :param metro: The metro of this MetroServerInfo.
        :param plan: The plan of this MetroServerInfo.
        :param quantity: The quantity of this MetroServerInfo.
        """
        self.openapi_types = {
            'metro': str,
            'plan': str,
            'quantity': str
        }

        self.attribute_map = {
            'metro': 'metro',
            'plan': 'plan',
            'quantity': 'quantity'
        }

        self._metro = metro
        self._plan = plan
        self._quantity = quantity

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MetroServerInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MetroServerInfo of this MetroServerInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metro(self):
        """Gets the metro of this MetroServerInfo.

        The metro ID or code to check the capacity in.

        :return: The metro of this MetroServerInfo.
        :rtype: str
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this MetroServerInfo.

        The metro ID or code to check the capacity in.

        :param metro: The metro of this MetroServerInfo.
        :type metro: str
        """

        self._metro = metro

    @property
    def plan(self):
        """Gets the plan of this MetroServerInfo.

        The plan ID or slug to check the capacity of.

        :return: The plan of this MetroServerInfo.
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this MetroServerInfo.

        The plan ID or slug to check the capacity of.

        :param plan: The plan of this MetroServerInfo.
        :type plan: str
        """

        self._plan = plan

    @property
    def quantity(self):
        """Gets the quantity of this MetroServerInfo.

        The number of servers to check the capacity of.

        :return: The quantity of this MetroServerInfo.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this MetroServerInfo.

        The number of servers to check the capacity of.

        :param quantity: The quantity of this MetroServerInfo.
        :type quantity: str
        """

        self._quantity = quantity
