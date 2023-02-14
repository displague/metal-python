# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal.types.capacity_check_per_metro_info import CapacityCheckPerMetroInfo
from metal import util


class CapacityCheckPerMetroList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, servers: List[CapacityCheckPerMetroInfo]=None):
        """CapacityCheckPerMetroList - a model defined in OpenAPI

        :param servers: The servers of this CapacityCheckPerMetroList.
        """
        self.openapi_types = {
            'servers': List[CapacityCheckPerMetroInfo]
        }

        self.attribute_map = {
            'servers': 'servers'
        }

        self._servers = servers

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CapacityCheckPerMetroList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CapacityCheckPerMetroList of this CapacityCheckPerMetroList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def servers(self):
        """Gets the servers of this CapacityCheckPerMetroList.


        :return: The servers of this CapacityCheckPerMetroList.
        :rtype: List[CapacityCheckPerMetroInfo]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this CapacityCheckPerMetroList.


        :param servers: The servers of this CapacityCheckPerMetroList.
        :type servers: List[CapacityCheckPerMetroInfo]
        """

        self._servers = servers
