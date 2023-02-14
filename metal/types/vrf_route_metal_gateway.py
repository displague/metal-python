# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal.types.href import Href
from metal.types.ip_reservation import IPReservation
from metal.types.metal_gateway import MetalGateway
from metal.types.project import Project
from metal.types.virtual_network import VirtualNetwork
from metal import util


class VrfRouteMetalGateway(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, href: str=None, created_at: datetime=None, created_by: Href=None, id: str=None, ip_reservation: IPReservation=None, project: Project=None, state: str=None, updated_at: datetime=None, virtual_network: VirtualNetwork=None):
        """VrfRouteMetalGateway - a model defined in OpenAPI

        :param href: The href of this VrfRouteMetalGateway.
        :param created_at: The created_at of this VrfRouteMetalGateway.
        :param created_by: The created_by of this VrfRouteMetalGateway.
        :param id: The id of this VrfRouteMetalGateway.
        :param ip_reservation: The ip_reservation of this VrfRouteMetalGateway.
        :param project: The project of this VrfRouteMetalGateway.
        :param state: The state of this VrfRouteMetalGateway.
        :param updated_at: The updated_at of this VrfRouteMetalGateway.
        :param virtual_network: The virtual_network of this VrfRouteMetalGateway.
        """
        self.openapi_types = {
            'href': str,
            'created_at': datetime,
            'created_by': Href,
            'id': str,
            'ip_reservation': IPReservation,
            'project': Project,
            'state': str,
            'updated_at': datetime,
            'virtual_network': VirtualNetwork
        }

        self.attribute_map = {
            'href': 'href',
            'created_at': 'created_at',
            'created_by': 'created_by',
            'id': 'id',
            'ip_reservation': 'ip_reservation',
            'project': 'project',
            'state': 'state',
            'updated_at': 'updated_at',
            'virtual_network': 'virtual_network'
        }

        self._href = href
        self._created_at = created_at
        self._created_by = created_by
        self._id = id
        self._ip_reservation = ip_reservation
        self._project = project
        self._state = state
        self._updated_at = updated_at
        self._virtual_network = virtual_network

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VrfRouteMetalGateway':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VrfRoute_metal_gateway of this VrfRouteMetalGateway.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def href(self):
        """Gets the href of this VrfRouteMetalGateway.


        :return: The href of this VrfRouteMetalGateway.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this VrfRouteMetalGateway.


        :param href: The href of this VrfRouteMetalGateway.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")

        self._href = href

    @property
    def created_at(self):
        """Gets the created_at of this VrfRouteMetalGateway.


        :return: The created_at of this VrfRouteMetalGateway.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VrfRouteMetalGateway.


        :param created_at: The created_at of this VrfRouteMetalGateway.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this VrfRouteMetalGateway.


        :return: The created_by of this VrfRouteMetalGateway.
        :rtype: Href
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this VrfRouteMetalGateway.


        :param created_by: The created_by of this VrfRouteMetalGateway.
        :type created_by: Href
        """

        self._created_by = created_by

    @property
    def id(self):
        """Gets the id of this VrfRouteMetalGateway.


        :return: The id of this VrfRouteMetalGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VrfRouteMetalGateway.


        :param id: The id of this VrfRouteMetalGateway.
        :type id: str
        """

        self._id = id

    @property
    def ip_reservation(self):
        """Gets the ip_reservation of this VrfRouteMetalGateway.


        :return: The ip_reservation of this VrfRouteMetalGateway.
        :rtype: IPReservation
        """
        return self._ip_reservation

    @ip_reservation.setter
    def ip_reservation(self, ip_reservation):
        """Sets the ip_reservation of this VrfRouteMetalGateway.


        :param ip_reservation: The ip_reservation of this VrfRouteMetalGateway.
        :type ip_reservation: IPReservation
        """

        self._ip_reservation = ip_reservation

    @property
    def project(self):
        """Gets the project of this VrfRouteMetalGateway.


        :return: The project of this VrfRouteMetalGateway.
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this VrfRouteMetalGateway.


        :param project: The project of this VrfRouteMetalGateway.
        :type project: Project
        """

        self._project = project

    @property
    def state(self):
        """Gets the state of this VrfRouteMetalGateway.

        The current state of the Metal Gateway. 'Ready' indicates the gateway record has been configured, but is currently not active on the network. 'Active' indicates the gateway has been configured on the network. 'Deleting' is a temporary state used to indicate that the gateway is in the process of being un-configured from the network, after which the gateway record will be deleted.

        :return: The state of this VrfRouteMetalGateway.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VrfRouteMetalGateway.

        The current state of the Metal Gateway. 'Ready' indicates the gateway record has been configured, but is currently not active on the network. 'Active' indicates the gateway has been configured on the network. 'Deleting' is a temporary state used to indicate that the gateway is in the process of being un-configured from the network, after which the gateway record will be deleted.

        :param state: The state of this VrfRouteMetalGateway.
        :type state: str
        """
        allowed_values = ["ready", "active", "deleting"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def updated_at(self):
        """Gets the updated_at of this VrfRouteMetalGateway.


        :return: The updated_at of this VrfRouteMetalGateway.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VrfRouteMetalGateway.


        :param updated_at: The updated_at of this VrfRouteMetalGateway.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def virtual_network(self):
        """Gets the virtual_network of this VrfRouteMetalGateway.


        :return: The virtual_network of this VrfRouteMetalGateway.
        :rtype: VirtualNetwork
        """
        return self._virtual_network

    @virtual_network.setter
    def virtual_network(self, virtual_network):
        """Sets the virtual_network of this VrfRouteMetalGateway.


        :param virtual_network: The virtual_network of this VrfRouteMetalGateway.
        :type virtual_network: VirtualNetwork
        """

        self._virtual_network = virtual_network
