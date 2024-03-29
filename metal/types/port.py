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


class Port(object):
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
        'bond': 'BondPortData',
        'data': 'PortData',
        'disbond_operation_supported': 'bool',
        'href': 'str',
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'network_type': 'str',
        'native_virtual_network': 'VirtualNetwork',
        'virtual_networks': 'list[Href]'
    }

    attribute_map = {
        'bond': 'bond',
        'data': 'data',
        'disbond_operation_supported': 'disbond_operation_supported',
        'href': 'href',
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'network_type': 'network_type',
        'native_virtual_network': 'native_virtual_network',
        'virtual_networks': 'virtual_networks'
    }

    def __init__(self, bond=None, data=None, disbond_operation_supported=None, href=None, id=None, name=None, type=None, network_type=None, native_virtual_network=None, virtual_networks=None, local_vars_configuration=None):  # noqa: E501
        """Port - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._bond = None
        self._data = None
        self._disbond_operation_supported = None
        self._href = None
        self._id = None
        self._name = None
        self._type = None
        self._network_type = None
        self._native_virtual_network = None
        self._virtual_networks = None
        self.discriminator = None

        if bond is not None:
            self.bond = bond
        if data is not None:
            self.data = data
        if disbond_operation_supported is not None:
            self.disbond_operation_supported = disbond_operation_supported
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if network_type is not None:
            self.network_type = network_type
        if native_virtual_network is not None:
            self.native_virtual_network = native_virtual_network
        if virtual_networks is not None:
            self.virtual_networks = virtual_networks

    @property
    def bond(self):
        """Gets the bond of this Port.  # noqa: E501


        :return: The bond of this Port.  # noqa: E501
        :rtype: BondPortData
        """
        return self._bond

    @bond.setter
    def bond(self, bond):
        """Sets the bond of this Port.


        :param bond: The bond of this Port.  # noqa: E501
        :type bond: BondPortData
        """

        self._bond = bond

    @property
    def data(self):
        """Gets the data of this Port.  # noqa: E501


        :return: The data of this Port.  # noqa: E501
        :rtype: PortData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Port.


        :param data: The data of this Port.  # noqa: E501
        :type data: PortData
        """

        self._data = data

    @property
    def disbond_operation_supported(self):
        """Gets the disbond_operation_supported of this Port.  # noqa: E501

        Indicates whether or not the bond can be broken on the port (when applicable).  # noqa: E501

        :return: The disbond_operation_supported of this Port.  # noqa: E501
        :rtype: bool
        """
        return self._disbond_operation_supported

    @disbond_operation_supported.setter
    def disbond_operation_supported(self, disbond_operation_supported):
        """Sets the disbond_operation_supported of this Port.

        Indicates whether or not the bond can be broken on the port (when applicable).  # noqa: E501

        :param disbond_operation_supported: The disbond_operation_supported of this Port.  # noqa: E501
        :type disbond_operation_supported: bool
        """

        self._disbond_operation_supported = disbond_operation_supported

    @property
    def href(self):
        """Gets the href of this Port.  # noqa: E501


        :return: The href of this Port.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Port.


        :param href: The href of this Port.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Port.  # noqa: E501


        :return: The id of this Port.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Port.


        :param id: The id of this Port.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Port.  # noqa: E501


        :return: The name of this Port.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Port.


        :param name: The name of this Port.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Port.  # noqa: E501

        Type is either \"NetworkBondPort\" for bond ports or \"NetworkPort\" for bondable ethernet ports  # noqa: E501

        :return: The type of this Port.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Port.

        Type is either \"NetworkBondPort\" for bond ports or \"NetworkPort\" for bondable ethernet ports  # noqa: E501

        :param type: The type of this Port.  # noqa: E501
        :type type: str
        """
        allowed_values = ["NetworkPort", "NetworkBondPort"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def network_type(self):
        """Gets the network_type of this Port.  # noqa: E501

        Composite network type of the bond  # noqa: E501

        :return: The network_type of this Port.  # noqa: E501
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this Port.

        Composite network type of the bond  # noqa: E501

        :param network_type: The network_type of this Port.  # noqa: E501
        :type network_type: str
        """
        allowed_values = ["layer2-bonded", "layer2-individual", "layer3", "hybrid", "hybrid-bonded"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and network_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `network_type` ({0}), must be one of {1}"  # noqa: E501
                .format(network_type, allowed_values)
            )

        self._network_type = network_type

    @property
    def native_virtual_network(self):
        """Gets the native_virtual_network of this Port.  # noqa: E501


        :return: The native_virtual_network of this Port.  # noqa: E501
        :rtype: VirtualNetwork
        """
        return self._native_virtual_network

    @native_virtual_network.setter
    def native_virtual_network(self, native_virtual_network):
        """Sets the native_virtual_network of this Port.


        :param native_virtual_network: The native_virtual_network of this Port.  # noqa: E501
        :type native_virtual_network: VirtualNetwork
        """

        self._native_virtual_network = native_virtual_network

    @property
    def virtual_networks(self):
        """Gets the virtual_networks of this Port.  # noqa: E501


        :return: The virtual_networks of this Port.  # noqa: E501
        :rtype: list[Href]
        """
        return self._virtual_networks

    @virtual_networks.setter
    def virtual_networks(self, virtual_networks):
        """Sets the virtual_networks of this Port.


        :param virtual_networks: The virtual_networks of this Port.  # noqa: E501
        :type virtual_networks: list[Href]
        """

        self._virtual_networks = virtual_networks

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
        if not isinstance(other, Port):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Port):
            return True

        return self.to_dict() != other.to_dict()
