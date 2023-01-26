# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://metal.equinix.com/developers/api>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. The fields available for search differ by resource, as does the search strategy.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field.   # noqa: E501

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


class VirtualNetwork(object):
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
        'assigned_to': 'Href',
        'assigned_to_virtual_circuit': 'bool',
        'description': 'str',
        'facility': 'Href',
        'href': 'str',
        'id': 'str',
        'instances': 'list[Href]',
        'metal_gateways': 'list[MetalGatewayLite]',
        'metro': 'Href',
        'metro_code': 'str',
        'vxlan': 'int'
    }

    attribute_map = {
        'assigned_to': 'assigned_to',
        'assigned_to_virtual_circuit': 'assigned_to_virtual_circuit',
        'description': 'description',
        'facility': 'facility',
        'href': 'href',
        'id': 'id',
        'instances': 'instances',
        'metal_gateways': 'metal_gateways',
        'metro': 'metro',
        'metro_code': 'metro_code',
        'vxlan': 'vxlan'
    }

    def __init__(self, assigned_to=None, assigned_to_virtual_circuit=None, description=None, facility=None, href=None, id=None, instances=None, metal_gateways=None, metro=None, metro_code=None, vxlan=None, local_vars_configuration=None):  # noqa: E501
        """VirtualNetwork - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._assigned_to = None
        self._assigned_to_virtual_circuit = None
        self._description = None
        self._facility = None
        self._href = None
        self._id = None
        self._instances = None
        self._metal_gateways = None
        self._metro = None
        self._metro_code = None
        self._vxlan = None
        self.discriminator = None

        if assigned_to is not None:
            self.assigned_to = assigned_to
        if assigned_to_virtual_circuit is not None:
            self.assigned_to_virtual_circuit = assigned_to_virtual_circuit
        if description is not None:
            self.description = description
        if facility is not None:
            self.facility = facility
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if instances is not None:
            self.instances = instances
        if metal_gateways is not None:
            self.metal_gateways = metal_gateways
        if metro is not None:
            self.metro = metro
        if metro_code is not None:
            self.metro_code = metro_code
        if vxlan is not None:
            self.vxlan = vxlan

    @property
    def assigned_to(self):
        """Gets the assigned_to of this VirtualNetwork.  # noqa: E501


        :return: The assigned_to of this VirtualNetwork.  # noqa: E501
        :rtype: Href
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this VirtualNetwork.


        :param assigned_to: The assigned_to of this VirtualNetwork.  # noqa: E501
        :type assigned_to: Href
        """

        self._assigned_to = assigned_to

    @property
    def assigned_to_virtual_circuit(self):
        """Gets the assigned_to_virtual_circuit of this VirtualNetwork.  # noqa: E501

        True if the virtual network is attached to a virtual circuit. False if not.  # noqa: E501

        :return: The assigned_to_virtual_circuit of this VirtualNetwork.  # noqa: E501
        :rtype: bool
        """
        return self._assigned_to_virtual_circuit

    @assigned_to_virtual_circuit.setter
    def assigned_to_virtual_circuit(self, assigned_to_virtual_circuit):
        """Sets the assigned_to_virtual_circuit of this VirtualNetwork.

        True if the virtual network is attached to a virtual circuit. False if not.  # noqa: E501

        :param assigned_to_virtual_circuit: The assigned_to_virtual_circuit of this VirtualNetwork.  # noqa: E501
        :type assigned_to_virtual_circuit: bool
        """

        self._assigned_to_virtual_circuit = assigned_to_virtual_circuit

    @property
    def description(self):
        """Gets the description of this VirtualNetwork.  # noqa: E501


        :return: The description of this VirtualNetwork.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualNetwork.


        :param description: The description of this VirtualNetwork.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def facility(self):
        """Gets the facility of this VirtualNetwork.  # noqa: E501


        :return: The facility of this VirtualNetwork.  # noqa: E501
        :rtype: Href
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this VirtualNetwork.


        :param facility: The facility of this VirtualNetwork.  # noqa: E501
        :type facility: Href
        """

        self._facility = facility

    @property
    def href(self):
        """Gets the href of this VirtualNetwork.  # noqa: E501


        :return: The href of this VirtualNetwork.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this VirtualNetwork.


        :param href: The href of this VirtualNetwork.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this VirtualNetwork.  # noqa: E501


        :return: The id of this VirtualNetwork.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualNetwork.


        :param id: The id of this VirtualNetwork.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def instances(self):
        """Gets the instances of this VirtualNetwork.  # noqa: E501

        A list of instances with ports currently associated to this Virtual Network.  # noqa: E501

        :return: The instances of this VirtualNetwork.  # noqa: E501
        :rtype: list[Href]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this VirtualNetwork.

        A list of instances with ports currently associated to this Virtual Network.  # noqa: E501

        :param instances: The instances of this VirtualNetwork.  # noqa: E501
        :type instances: list[Href]
        """

        self._instances = instances

    @property
    def metal_gateways(self):
        """Gets the metal_gateways of this VirtualNetwork.  # noqa: E501

        A list of metal gateways currently associated to this Virtual Network.  # noqa: E501

        :return: The metal_gateways of this VirtualNetwork.  # noqa: E501
        :rtype: list[MetalGatewayLite]
        """
        return self._metal_gateways

    @metal_gateways.setter
    def metal_gateways(self, metal_gateways):
        """Sets the metal_gateways of this VirtualNetwork.

        A list of metal gateways currently associated to this Virtual Network.  # noqa: E501

        :param metal_gateways: The metal_gateways of this VirtualNetwork.  # noqa: E501
        :type metal_gateways: list[MetalGatewayLite]
        """

        self._metal_gateways = metal_gateways

    @property
    def metro(self):
        """Gets the metro of this VirtualNetwork.  # noqa: E501


        :return: The metro of this VirtualNetwork.  # noqa: E501
        :rtype: Href
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this VirtualNetwork.


        :param metro: The metro of this VirtualNetwork.  # noqa: E501
        :type metro: Href
        """

        self._metro = metro

    @property
    def metro_code(self):
        """Gets the metro_code of this VirtualNetwork.  # noqa: E501

        The Metro code of the metro in which this Virtual Network is defined.  # noqa: E501

        :return: The metro_code of this VirtualNetwork.  # noqa: E501
        :rtype: str
        """
        return self._metro_code

    @metro_code.setter
    def metro_code(self, metro_code):
        """Sets the metro_code of this VirtualNetwork.

        The Metro code of the metro in which this Virtual Network is defined.  # noqa: E501

        :param metro_code: The metro_code of this VirtualNetwork.  # noqa: E501
        :type metro_code: str
        """

        self._metro_code = metro_code

    @property
    def vxlan(self):
        """Gets the vxlan of this VirtualNetwork.  # noqa: E501


        :return: The vxlan of this VirtualNetwork.  # noqa: E501
        :rtype: int
        """
        return self._vxlan

    @vxlan.setter
    def vxlan(self, vxlan):
        """Sets the vxlan of this VirtualNetwork.


        :param vxlan: The vxlan of this VirtualNetwork.  # noqa: E501
        :type vxlan: int
        """

        self._vxlan = vxlan

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
        if not isinstance(other, VirtualNetwork):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualNetwork):
            return True

        return self.to_dict() != other.to_dict()
