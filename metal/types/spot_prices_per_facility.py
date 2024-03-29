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


class SpotPricesPerFacility(object):
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
        'baremetal_0': 'SpotPricesPerBaremetal',
        'baremetal_1': 'SpotPricesPerBaremetal',
        'baremetal_2': 'SpotPricesPerBaremetal',
        'baremetal_2a': 'SpotPricesPerBaremetal',
        'baremetal_2a2': 'SpotPricesPerBaremetal',
        'baremetal_3': 'SpotPricesPerBaremetal',
        'baremetal_s': 'SpotPricesPerBaremetal',
        'c2_medium_x86': 'SpotPricesPerBaremetal',
        'm2_xlarge_x86': 'SpotPricesPerBaremetal'
    }

    attribute_map = {
        'baremetal_0': 'baremetal_0',
        'baremetal_1': 'baremetal_1',
        'baremetal_2': 'baremetal_2',
        'baremetal_2a': 'baremetal_2a',
        'baremetal_2a2': 'baremetal_2a2',
        'baremetal_3': 'baremetal_3',
        'baremetal_s': 'baremetal_s',
        'c2_medium_x86': 'c2.medium.x86',
        'm2_xlarge_x86': 'm2.xlarge.x86'
    }

    def __init__(self, baremetal_0=None, baremetal_1=None, baremetal_2=None, baremetal_2a=None, baremetal_2a2=None, baremetal_3=None, baremetal_s=None, c2_medium_x86=None, m2_xlarge_x86=None, local_vars_configuration=None):  # noqa: E501
        """SpotPricesPerFacility - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._baremetal_0 = None
        self._baremetal_1 = None
        self._baremetal_2 = None
        self._baremetal_2a = None
        self._baremetal_2a2 = None
        self._baremetal_3 = None
        self._baremetal_s = None
        self._c2_medium_x86 = None
        self._m2_xlarge_x86 = None
        self.discriminator = None

        if baremetal_0 is not None:
            self.baremetal_0 = baremetal_0
        if baremetal_1 is not None:
            self.baremetal_1 = baremetal_1
        if baremetal_2 is not None:
            self.baremetal_2 = baremetal_2
        if baremetal_2a is not None:
            self.baremetal_2a = baremetal_2a
        if baremetal_2a2 is not None:
            self.baremetal_2a2 = baremetal_2a2
        if baremetal_3 is not None:
            self.baremetal_3 = baremetal_3
        if baremetal_s is not None:
            self.baremetal_s = baremetal_s
        if c2_medium_x86 is not None:
            self.c2_medium_x86 = c2_medium_x86
        if m2_xlarge_x86 is not None:
            self.m2_xlarge_x86 = m2_xlarge_x86

    @property
    def baremetal_0(self):
        """Gets the baremetal_0 of this SpotPricesPerFacility.  # noqa: E501


        :return: The baremetal_0 of this SpotPricesPerFacility.  # noqa: E501
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_0

    @baremetal_0.setter
    def baremetal_0(self, baremetal_0):
        """Sets the baremetal_0 of this SpotPricesPerFacility.


        :param baremetal_0: The baremetal_0 of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_0: SpotPricesPerBaremetal
        """

        self._baremetal_0 = baremetal_0

    @property
    def baremetal_1(self):
        """Gets the baremetal_1 of this SpotPricesPerFacility.  # noqa: E501


        :return: The baremetal_1 of this SpotPricesPerFacility.  # noqa: E501
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_1

    @baremetal_1.setter
    def baremetal_1(self, baremetal_1):
        """Sets the baremetal_1 of this SpotPricesPerFacility.


        :param baremetal_1: The baremetal_1 of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_1: SpotPricesPerBaremetal
        """

        self._baremetal_1 = baremetal_1

    @property
    def baremetal_2(self):
        """Gets the baremetal_2 of this SpotPricesPerFacility.  # noqa: E501


        :return: The baremetal_2 of this SpotPricesPerFacility.  # noqa: E501
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_2

    @baremetal_2.setter
    def baremetal_2(self, baremetal_2):
        """Sets the baremetal_2 of this SpotPricesPerFacility.


        :param baremetal_2: The baremetal_2 of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_2: SpotPricesPerBaremetal
        """

        self._baremetal_2 = baremetal_2

    @property
    def baremetal_2a(self):
        """Gets the baremetal_2a of this SpotPricesPerFacility.  # noqa: E501


        :return: The baremetal_2a of this SpotPricesPerFacility.  # noqa: E501
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_2a

    @baremetal_2a.setter
    def baremetal_2a(self, baremetal_2a):
        """Sets the baremetal_2a of this SpotPricesPerFacility.


        :param baremetal_2a: The baremetal_2a of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_2a: SpotPricesPerBaremetal
        """

        self._baremetal_2a = baremetal_2a

    @property
    def baremetal_2a2(self):
        """Gets the baremetal_2a2 of this SpotPricesPerFacility.  # noqa: E501


        :return: The baremetal_2a2 of this SpotPricesPerFacility.  # noqa: E501
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_2a2

    @baremetal_2a2.setter
    def baremetal_2a2(self, baremetal_2a2):
        """Sets the baremetal_2a2 of this SpotPricesPerFacility.


        :param baremetal_2a2: The baremetal_2a2 of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_2a2: SpotPricesPerBaremetal
        """

        self._baremetal_2a2 = baremetal_2a2

    @property
    def baremetal_3(self):
        """Gets the baremetal_3 of this SpotPricesPerFacility.  # noqa: E501


        :return: The baremetal_3 of this SpotPricesPerFacility.  # noqa: E501
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_3

    @baremetal_3.setter
    def baremetal_3(self, baremetal_3):
        """Sets the baremetal_3 of this SpotPricesPerFacility.


        :param baremetal_3: The baremetal_3 of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_3: SpotPricesPerBaremetal
        """

        self._baremetal_3 = baremetal_3

    @property
    def baremetal_s(self):
        """Gets the baremetal_s of this SpotPricesPerFacility.  # noqa: E501


        :return: The baremetal_s of this SpotPricesPerFacility.  # noqa: E501
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_s

    @baremetal_s.setter
    def baremetal_s(self, baremetal_s):
        """Sets the baremetal_s of this SpotPricesPerFacility.


        :param baremetal_s: The baremetal_s of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_s: SpotPricesPerBaremetal
        """

        self._baremetal_s = baremetal_s

    @property
    def c2_medium_x86(self):
        """Gets the c2_medium_x86 of this SpotPricesPerFacility.  # noqa: E501


        :return: The c2_medium_x86 of this SpotPricesPerFacility.  # noqa: E501
        :rtype: SpotPricesPerBaremetal
        """
        return self._c2_medium_x86

    @c2_medium_x86.setter
    def c2_medium_x86(self, c2_medium_x86):
        """Sets the c2_medium_x86 of this SpotPricesPerFacility.


        :param c2_medium_x86: The c2_medium_x86 of this SpotPricesPerFacility.  # noqa: E501
        :type c2_medium_x86: SpotPricesPerBaremetal
        """

        self._c2_medium_x86 = c2_medium_x86

    @property
    def m2_xlarge_x86(self):
        """Gets the m2_xlarge_x86 of this SpotPricesPerFacility.  # noqa: E501


        :return: The m2_xlarge_x86 of this SpotPricesPerFacility.  # noqa: E501
        :rtype: SpotPricesPerBaremetal
        """
        return self._m2_xlarge_x86

    @m2_xlarge_x86.setter
    def m2_xlarge_x86(self, m2_xlarge_x86):
        """Sets the m2_xlarge_x86 of this SpotPricesPerFacility.


        :param m2_xlarge_x86: The m2_xlarge_x86 of this SpotPricesPerFacility.  # noqa: E501
        :type m2_xlarge_x86: SpotPricesPerBaremetal
        """

        self._m2_xlarge_x86 = m2_xlarge_x86

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
        if not isinstance(other, SpotPricesPerFacility):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpotPricesPerFacility):
            return True

        return self.to_dict() != other.to_dict()
