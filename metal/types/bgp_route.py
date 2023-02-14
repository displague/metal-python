# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal import util


class BgpRoute(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, exact: bool=None, route: str=None):
        """BgpRoute - a model defined in OpenAPI

        :param exact: The exact of this BgpRoute.
        :param route: The route of this BgpRoute.
        """
        self.openapi_types = {
            'exact': bool,
            'route': str
        }

        self.attribute_map = {
            'exact': 'exact',
            'route': 'route'
        }

        self._exact = exact
        self._route = route

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BgpRoute':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BgpRoute of this BgpRoute.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def exact(self):
        """Gets the exact of this BgpRoute.


        :return: The exact of this BgpRoute.
        :rtype: bool
        """
        return self._exact

    @exact.setter
    def exact(self, exact):
        """Sets the exact of this BgpRoute.


        :param exact: The exact of this BgpRoute.
        :type exact: bool
        """

        self._exact = exact

    @property
    def route(self):
        """Gets the route of this BgpRoute.


        :return: The route of this BgpRoute.
        :rtype: str
        """
        return self._route

    @route.setter
    def route(self, route):
        """Sets the route of this BgpRoute.


        :param route: The route of this BgpRoute.
        :type route: str
        """

        self._route = route
