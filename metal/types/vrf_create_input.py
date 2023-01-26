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


class VrfCreateInput(object):
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
        'description': 'str',
        'ip_ranges': 'list[str]',
        'local_asn': 'int',
        'metro': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'ip_ranges': 'ip_ranges',
        'local_asn': 'local_asn',
        'metro': 'metro',
        'name': 'name'
    }

    def __init__(self, description=None, ip_ranges=None, local_asn=None, metro=None, name=None, local_vars_configuration=None):  # noqa: E501
        """VrfCreateInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._ip_ranges = None
        self._local_asn = None
        self._metro = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if ip_ranges is not None:
            self.ip_ranges = ip_ranges
        if local_asn is not None:
            self.local_asn = local_asn
        self.metro = metro
        self.name = name

    @property
    def description(self):
        """Gets the description of this VrfCreateInput.  # noqa: E501


        :return: The description of this VrfCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VrfCreateInput.


        :param description: The description of this VrfCreateInput.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def ip_ranges(self):
        """Gets the ip_ranges of this VrfCreateInput.  # noqa: E501

        A list of CIDR network addresses. Like [\"10.0.0.0/16\", \"2001:d78::/56\"]. IPv4 blocks must be between /8 and /29 in size. IPv6 blocks must be between /56 and /64. A VRF\\'s IP ranges must be defined in order to create VRF IP Reservations, which can then be used for Metal Gateways or Virtual Circuits.  # noqa: E501

        :return: The ip_ranges of this VrfCreateInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_ranges

    @ip_ranges.setter
    def ip_ranges(self, ip_ranges):
        """Sets the ip_ranges of this VrfCreateInput.

        A list of CIDR network addresses. Like [\"10.0.0.0/16\", \"2001:d78::/56\"]. IPv4 blocks must be between /8 and /29 in size. IPv6 blocks must be between /56 and /64. A VRF\\'s IP ranges must be defined in order to create VRF IP Reservations, which can then be used for Metal Gateways or Virtual Circuits.  # noqa: E501

        :param ip_ranges: The ip_ranges of this VrfCreateInput.  # noqa: E501
        :type ip_ranges: list[str]
        """

        self._ip_ranges = ip_ranges

    @property
    def local_asn(self):
        """Gets the local_asn of this VrfCreateInput.  # noqa: E501


        :return: The local_asn of this VrfCreateInput.  # noqa: E501
        :rtype: int
        """
        return self._local_asn

    @local_asn.setter
    def local_asn(self, local_asn):
        """Sets the local_asn of this VrfCreateInput.


        :param local_asn: The local_asn of this VrfCreateInput.  # noqa: E501
        :type local_asn: int
        """

        self._local_asn = local_asn

    @property
    def metro(self):
        """Gets the metro of this VrfCreateInput.  # noqa: E501

        The UUID (or metro code) for the Metro in which to create this VRF.  # noqa: E501

        :return: The metro of this VrfCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this VrfCreateInput.

        The UUID (or metro code) for the Metro in which to create this VRF.  # noqa: E501

        :param metro: The metro of this VrfCreateInput.  # noqa: E501
        :type metro: str
        """
        if self.local_vars_configuration.client_side_validation and metro is None:  # noqa: E501
            raise ValueError("Invalid value for `metro`, must not be `None`")  # noqa: E501

        self._metro = metro

    @property
    def name(self):
        """Gets the name of this VrfCreateInput.  # noqa: E501


        :return: The name of this VrfCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VrfCreateInput.


        :param name: The name of this VrfCreateInput.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, VrfCreateInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VrfCreateInput):
            return True

        return self.to_dict() != other.to_dict()
