# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal import util


class MembershipInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, role: List[str]=None):
        """MembershipInput - a model defined in OpenAPI

        :param role: The role of this MembershipInput.
        """
        self.openapi_types = {
            'role': List[str]
        }

        self.attribute_map = {
            'role': 'role'
        }

        self._role = role

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MembershipInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MembershipInput of this MembershipInput.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def role(self):
        """Gets the role of this MembershipInput.


        :return: The role of this MembershipInput.
        :rtype: List[str]
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this MembershipInput.


        :param role: The role of this MembershipInput.
        :type role: List[str]
        """

        self._role = role
