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


class Meta(object):
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
        'first': 'Href',
        'last': 'Href',
        'next': 'Href',
        'previous': 'Href',
        '_self': 'Href',
        'total': 'int',
        'current_page': 'int',
        'last_page': 'int'
    }

    attribute_map = {
        'first': 'first',
        'last': 'last',
        'next': 'next',
        'previous': 'previous',
        '_self': 'self',
        'total': 'total',
        'current_page': 'current_page',
        'last_page': 'last_page'
    }

    def __init__(self, first=None, last=None, next=None, previous=None, _self=None, total=None, current_page=None, last_page=None, local_vars_configuration=None):  # noqa: E501
        """Meta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._first = None
        self._last = None
        self._next = None
        self._previous = None
        self.__self = None
        self._total = None
        self._current_page = None
        self._last_page = None
        self.discriminator = None

        if first is not None:
            self.first = first
        if last is not None:
            self.last = last
        if next is not None:
            self.next = next
        if previous is not None:
            self.previous = previous
        if _self is not None:
            self._self = _self
        if total is not None:
            self.total = total
        if current_page is not None:
            self.current_page = current_page
        if last_page is not None:
            self.last_page = last_page

    @property
    def first(self):
        """Gets the first of this Meta.  # noqa: E501


        :return: The first of this Meta.  # noqa: E501
        :rtype: Href
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this Meta.


        :param first: The first of this Meta.  # noqa: E501
        :type first: Href
        """

        self._first = first

    @property
    def last(self):
        """Gets the last of this Meta.  # noqa: E501


        :return: The last of this Meta.  # noqa: E501
        :rtype: Href
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this Meta.


        :param last: The last of this Meta.  # noqa: E501
        :type last: Href
        """

        self._last = last

    @property
    def next(self):
        """Gets the next of this Meta.  # noqa: E501


        :return: The next of this Meta.  # noqa: E501
        :rtype: Href
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Meta.


        :param next: The next of this Meta.  # noqa: E501
        :type next: Href
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this Meta.  # noqa: E501


        :return: The previous of this Meta.  # noqa: E501
        :rtype: Href
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this Meta.


        :param previous: The previous of this Meta.  # noqa: E501
        :type previous: Href
        """

        self._previous = previous

    @property
    def _self(self):
        """Gets the _self of this Meta.  # noqa: E501


        :return: The _self of this Meta.  # noqa: E501
        :rtype: Href
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Meta.


        :param _self: The _self of this Meta.  # noqa: E501
        :type _self: Href
        """

        self.__self = _self

    @property
    def total(self):
        """Gets the total of this Meta.  # noqa: E501


        :return: The total of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Meta.


        :param total: The total of this Meta.  # noqa: E501
        :type total: int
        """

        self._total = total

    @property
    def current_page(self):
        """Gets the current_page of this Meta.  # noqa: E501


        :return: The current_page of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this Meta.


        :param current_page: The current_page of this Meta.  # noqa: E501
        :type current_page: int
        """

        self._current_page = current_page

    @property
    def last_page(self):
        """Gets the last_page of this Meta.  # noqa: E501


        :return: The last_page of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._last_page

    @last_page.setter
    def last_page(self, last_page):
        """Sets the last_page of this Meta.


        :param last_page: The last_page of this Meta.  # noqa: E501
        :type last_page: int
        """

        self._last_page = last_page

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
        if not isinstance(other, Meta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Meta):
            return True

        return self.to_dict() != other.to_dict()
