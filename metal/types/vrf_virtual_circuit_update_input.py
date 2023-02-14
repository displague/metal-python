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


class VrfVirtualCircuitUpdateInput(object):
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
        'customer_ip': 'str',
        'description': 'str',
        'md5': 'str',
        'metal_ip': 'str',
        'name': 'str',
        'peer_asn': 'int',
        'speed': 'str',
        'subnet': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'customer_ip': 'customer_ip',
        'description': 'description',
        'md5': 'md5',
        'metal_ip': 'metal_ip',
        'name': 'name',
        'peer_asn': 'peer_asn',
        'speed': 'speed',
        'subnet': 'subnet',
        'tags': 'tags'
    }

    def __init__(self, customer_ip=None, description=None, md5=None, metal_ip=None, name=None, peer_asn=None, speed=None, subnet=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """VrfVirtualCircuitUpdateInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._customer_ip = None
        self._description = None
        self._md5 = None
        self._metal_ip = None
        self._name = None
        self._peer_asn = None
        self._speed = None
        self._subnet = None
        self._tags = None
        self.discriminator = None

        if customer_ip is not None:
            self.customer_ip = customer_ip
        if description is not None:
            self.description = description
        if md5 is not None:
            self.md5 = md5
        if metal_ip is not None:
            self.metal_ip = metal_ip
        if name is not None:
            self.name = name
        if peer_asn is not None:
            self.peer_asn = peer_asn
        if speed is not None:
            self.speed = speed
        if subnet is not None:
            self.subnet = subnet
        if tags is not None:
            self.tags = tags

    @property
    def customer_ip(self):
        """Gets the customer_ip of this VrfVirtualCircuitUpdateInput.  # noqa: E501

        An IP address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used.  # noqa: E501

        :return: The customer_ip of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._customer_ip

    @customer_ip.setter
    def customer_ip(self, customer_ip):
        """Sets the customer_ip of this VrfVirtualCircuitUpdateInput.

        An IP address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used.  # noqa: E501

        :param customer_ip: The customer_ip of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :type customer_ip: str
        """

        self._customer_ip = customer_ip

    @property
    def description(self):
        """Gets the description of this VrfVirtualCircuitUpdateInput.  # noqa: E501


        :return: The description of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VrfVirtualCircuitUpdateInput.


        :param description: The description of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def md5(self):
        """Gets the md5 of this VrfVirtualCircuitUpdateInput.  # noqa: E501

        The MD5 password for the BGP peering in plaintext (not a checksum).  # noqa: E501

        :return: The md5 of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this VrfVirtualCircuitUpdateInput.

        The MD5 password for the BGP peering in plaintext (not a checksum).  # noqa: E501

        :param md5: The md5 of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :type md5: str
        """

        self._md5 = md5

    @property
    def metal_ip(self):
        """Gets the metal_ip of this VrfVirtualCircuitUpdateInput.  # noqa: E501

        An IP address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used.  # noqa: E501

        :return: The metal_ip of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._metal_ip

    @metal_ip.setter
    def metal_ip(self, metal_ip):
        """Sets the metal_ip of this VrfVirtualCircuitUpdateInput.

        An IP address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used.  # noqa: E501

        :param metal_ip: The metal_ip of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :type metal_ip: str
        """

        self._metal_ip = metal_ip

    @property
    def name(self):
        """Gets the name of this VrfVirtualCircuitUpdateInput.  # noqa: E501


        :return: The name of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VrfVirtualCircuitUpdateInput.


        :param name: The name of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def peer_asn(self):
        """Gets the peer_asn of this VrfVirtualCircuitUpdateInput.  # noqa: E501

        The peer ASN that will be used with the VRF on the Virtual Circuit.  # noqa: E501

        :return: The peer_asn of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :rtype: int
        """
        return self._peer_asn

    @peer_asn.setter
    def peer_asn(self, peer_asn):
        """Sets the peer_asn of this VrfVirtualCircuitUpdateInput.

        The peer ASN that will be used with the VRF on the Virtual Circuit.  # noqa: E501

        :param peer_asn: The peer_asn of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :type peer_asn: int
        """

        self._peer_asn = peer_asn

    @property
    def speed(self):
        """Gets the speed of this VrfVirtualCircuitUpdateInput.  # noqa: E501

        Speed can be changed only if it is an interconnection on a Dedicated Port  # noqa: E501

        :return: The speed of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this VrfVirtualCircuitUpdateInput.

        Speed can be changed only if it is an interconnection on a Dedicated Port  # noqa: E501

        :param speed: The speed of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :type speed: str
        """

        self._speed = speed

    @property
    def subnet(self):
        """Gets the subnet of this VrfVirtualCircuitUpdateInput.  # noqa: E501

        The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP.  # noqa: E501

        :return: The subnet of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this VrfVirtualCircuitUpdateInput.

        The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP.  # noqa: E501

        :param subnet: The subnet of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :type subnet: str
        """

        self._subnet = subnet

    @property
    def tags(self):
        """Gets the tags of this VrfVirtualCircuitUpdateInput.  # noqa: E501


        :return: The tags of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VrfVirtualCircuitUpdateInput.


        :param tags: The tags of this VrfVirtualCircuitUpdateInput.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, VrfVirtualCircuitUpdateInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VrfVirtualCircuitUpdateInput):
            return True

        return self.to_dict() != other.to_dict()
