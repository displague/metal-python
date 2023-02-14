# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal.types.spot_market_request_create_input_instance_attributes import SpotMarketRequestCreateInputInstanceAttributes
from metal import util


class SpotMarketRequestCreateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, devices_max: int=None, devices_min: int=None, end_at: datetime=None, facilities: List[str]=None, instance_attributes: SpotMarketRequestCreateInputInstanceAttributes=None, max_bid_price: float=None, metro: str=None):
        """SpotMarketRequestCreateInput - a model defined in OpenAPI

        :param devices_max: The devices_max of this SpotMarketRequestCreateInput.
        :param devices_min: The devices_min of this SpotMarketRequestCreateInput.
        :param end_at: The end_at of this SpotMarketRequestCreateInput.
        :param facilities: The facilities of this SpotMarketRequestCreateInput.
        :param instance_attributes: The instance_attributes of this SpotMarketRequestCreateInput.
        :param max_bid_price: The max_bid_price of this SpotMarketRequestCreateInput.
        :param metro: The metro of this SpotMarketRequestCreateInput.
        """
        self.openapi_types = {
            'devices_max': int,
            'devices_min': int,
            'end_at': datetime,
            'facilities': List[str],
            'instance_attributes': SpotMarketRequestCreateInputInstanceAttributes,
            'max_bid_price': float,
            'metro': str
        }

        self.attribute_map = {
            'devices_max': 'devices_max',
            'devices_min': 'devices_min',
            'end_at': 'end_at',
            'facilities': 'facilities',
            'instance_attributes': 'instance_attributes',
            'max_bid_price': 'max_bid_price',
            'metro': 'metro'
        }

        self._devices_max = devices_max
        self._devices_min = devices_min
        self._end_at = end_at
        self._facilities = facilities
        self._instance_attributes = instance_attributes
        self._max_bid_price = max_bid_price
        self._metro = metro

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SpotMarketRequestCreateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SpotMarketRequestCreateInput of this SpotMarketRequestCreateInput.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def devices_max(self):
        """Gets the devices_max of this SpotMarketRequestCreateInput.


        :return: The devices_max of this SpotMarketRequestCreateInput.
        :rtype: int
        """
        return self._devices_max

    @devices_max.setter
    def devices_max(self, devices_max):
        """Sets the devices_max of this SpotMarketRequestCreateInput.


        :param devices_max: The devices_max of this SpotMarketRequestCreateInput.
        :type devices_max: int
        """

        self._devices_max = devices_max

    @property
    def devices_min(self):
        """Gets the devices_min of this SpotMarketRequestCreateInput.


        :return: The devices_min of this SpotMarketRequestCreateInput.
        :rtype: int
        """
        return self._devices_min

    @devices_min.setter
    def devices_min(self, devices_min):
        """Sets the devices_min of this SpotMarketRequestCreateInput.


        :param devices_min: The devices_min of this SpotMarketRequestCreateInput.
        :type devices_min: int
        """

        self._devices_min = devices_min

    @property
    def end_at(self):
        """Gets the end_at of this SpotMarketRequestCreateInput.


        :return: The end_at of this SpotMarketRequestCreateInput.
        :rtype: datetime
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this SpotMarketRequestCreateInput.


        :param end_at: The end_at of this SpotMarketRequestCreateInput.
        :type end_at: datetime
        """

        self._end_at = end_at

    @property
    def facilities(self):
        """Gets the facilities of this SpotMarketRequestCreateInput.


        :return: The facilities of this SpotMarketRequestCreateInput.
        :rtype: List[str]
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities):
        """Sets the facilities of this SpotMarketRequestCreateInput.


        :param facilities: The facilities of this SpotMarketRequestCreateInput.
        :type facilities: List[str]
        """

        self._facilities = facilities

    @property
    def instance_attributes(self):
        """Gets the instance_attributes of this SpotMarketRequestCreateInput.


        :return: The instance_attributes of this SpotMarketRequestCreateInput.
        :rtype: SpotMarketRequestCreateInputInstanceAttributes
        """
        return self._instance_attributes

    @instance_attributes.setter
    def instance_attributes(self, instance_attributes):
        """Sets the instance_attributes of this SpotMarketRequestCreateInput.


        :param instance_attributes: The instance_attributes of this SpotMarketRequestCreateInput.
        :type instance_attributes: SpotMarketRequestCreateInputInstanceAttributes
        """

        self._instance_attributes = instance_attributes

    @property
    def max_bid_price(self):
        """Gets the max_bid_price of this SpotMarketRequestCreateInput.


        :return: The max_bid_price of this SpotMarketRequestCreateInput.
        :rtype: float
        """
        return self._max_bid_price

    @max_bid_price.setter
    def max_bid_price(self, max_bid_price):
        """Sets the max_bid_price of this SpotMarketRequestCreateInput.


        :param max_bid_price: The max_bid_price of this SpotMarketRequestCreateInput.
        :type max_bid_price: float
        """

        self._max_bid_price = max_bid_price

    @property
    def metro(self):
        """Gets the metro of this SpotMarketRequestCreateInput.

        The metro ID or code the spot market request will be created in.

        :return: The metro of this SpotMarketRequestCreateInput.
        :rtype: str
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this SpotMarketRequestCreateInput.

        The metro ID or code the spot market request will be created in.

        :param metro: The metro of this SpotMarketRequestCreateInput.
        :type metro: str
        """

        self._metro = metro
