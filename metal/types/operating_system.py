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


class OperatingSystem(object):
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
        'distro': 'str',
        'distro_label': 'str',
        'id': 'str',
        'licensed': 'bool',
        'name': 'str',
        'preinstallable': 'bool',
        'pricing': 'object',
        'provisionable_on': 'list[str]',
        'slug': 'str',
        'version': 'str'
    }

    attribute_map = {
        'distro': 'distro',
        'distro_label': 'distro_label',
        'id': 'id',
        'licensed': 'licensed',
        'name': 'name',
        'preinstallable': 'preinstallable',
        'pricing': 'pricing',
        'provisionable_on': 'provisionable_on',
        'slug': 'slug',
        'version': 'version'
    }

    def __init__(self, distro=None, distro_label=None, id=None, licensed=None, name=None, preinstallable=None, pricing=None, provisionable_on=None, slug=None, version=None, local_vars_configuration=None):  # noqa: E501
        """OperatingSystem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._distro = None
        self._distro_label = None
        self._id = None
        self._licensed = None
        self._name = None
        self._preinstallable = None
        self._pricing = None
        self._provisionable_on = None
        self._slug = None
        self._version = None
        self.discriminator = None

        if distro is not None:
            self.distro = distro
        if distro_label is not None:
            self.distro_label = distro_label
        if id is not None:
            self.id = id
        if licensed is not None:
            self.licensed = licensed
        if name is not None:
            self.name = name
        if preinstallable is not None:
            self.preinstallable = preinstallable
        if pricing is not None:
            self.pricing = pricing
        if provisionable_on is not None:
            self.provisionable_on = provisionable_on
        if slug is not None:
            self.slug = slug
        if version is not None:
            self.version = version

    @property
    def distro(self):
        """Gets the distro of this OperatingSystem.  # noqa: E501


        :return: The distro of this OperatingSystem.  # noqa: E501
        :rtype: str
        """
        return self._distro

    @distro.setter
    def distro(self, distro):
        """Sets the distro of this OperatingSystem.


        :param distro: The distro of this OperatingSystem.  # noqa: E501
        :type distro: str
        """

        self._distro = distro

    @property
    def distro_label(self):
        """Gets the distro_label of this OperatingSystem.  # noqa: E501


        :return: The distro_label of this OperatingSystem.  # noqa: E501
        :rtype: str
        """
        return self._distro_label

    @distro_label.setter
    def distro_label(self, distro_label):
        """Sets the distro_label of this OperatingSystem.


        :param distro_label: The distro_label of this OperatingSystem.  # noqa: E501
        :type distro_label: str
        """

        self._distro_label = distro_label

    @property
    def id(self):
        """Gets the id of this OperatingSystem.  # noqa: E501


        :return: The id of this OperatingSystem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OperatingSystem.


        :param id: The id of this OperatingSystem.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def licensed(self):
        """Gets the licensed of this OperatingSystem.  # noqa: E501

        Licenced OS is priced according to pricing property  # noqa: E501

        :return: The licensed of this OperatingSystem.  # noqa: E501
        :rtype: bool
        """
        return self._licensed

    @licensed.setter
    def licensed(self, licensed):
        """Sets the licensed of this OperatingSystem.

        Licenced OS is priced according to pricing property  # noqa: E501

        :param licensed: The licensed of this OperatingSystem.  # noqa: E501
        :type licensed: bool
        """

        self._licensed = licensed

    @property
    def name(self):
        """Gets the name of this OperatingSystem.  # noqa: E501


        :return: The name of this OperatingSystem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OperatingSystem.


        :param name: The name of this OperatingSystem.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def preinstallable(self):
        """Gets the preinstallable of this OperatingSystem.  # noqa: E501

        Servers can be already preinstalled with OS in order to shorten provision time.  # noqa: E501

        :return: The preinstallable of this OperatingSystem.  # noqa: E501
        :rtype: bool
        """
        return self._preinstallable

    @preinstallable.setter
    def preinstallable(self, preinstallable):
        """Sets the preinstallable of this OperatingSystem.

        Servers can be already preinstalled with OS in order to shorten provision time.  # noqa: E501

        :param preinstallable: The preinstallable of this OperatingSystem.  # noqa: E501
        :type preinstallable: bool
        """

        self._preinstallable = preinstallable

    @property
    def pricing(self):
        """Gets the pricing of this OperatingSystem.  # noqa: E501

        This object contains price per time unit and optional multiplier value if licence price depends on hardware plan or components (e.g. number of cores)  # noqa: E501

        :return: The pricing of this OperatingSystem.  # noqa: E501
        :rtype: object
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this OperatingSystem.

        This object contains price per time unit and optional multiplier value if licence price depends on hardware plan or components (e.g. number of cores)  # noqa: E501

        :param pricing: The pricing of this OperatingSystem.  # noqa: E501
        :type pricing: object
        """

        self._pricing = pricing

    @property
    def provisionable_on(self):
        """Gets the provisionable_on of this OperatingSystem.  # noqa: E501


        :return: The provisionable_on of this OperatingSystem.  # noqa: E501
        :rtype: list[str]
        """
        return self._provisionable_on

    @provisionable_on.setter
    def provisionable_on(self, provisionable_on):
        """Sets the provisionable_on of this OperatingSystem.


        :param provisionable_on: The provisionable_on of this OperatingSystem.  # noqa: E501
        :type provisionable_on: list[str]
        """

        self._provisionable_on = provisionable_on

    @property
    def slug(self):
        """Gets the slug of this OperatingSystem.  # noqa: E501


        :return: The slug of this OperatingSystem.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this OperatingSystem.


        :param slug: The slug of this OperatingSystem.  # noqa: E501
        :type slug: str
        """

        self._slug = slug

    @property
    def version(self):
        """Gets the version of this OperatingSystem.  # noqa: E501


        :return: The version of this OperatingSystem.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OperatingSystem.


        :param version: The version of this OperatingSystem.  # noqa: E501
        :type version: str
        """

        self._version = version

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
        if not isinstance(other, OperatingSystem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OperatingSystem):
            return True

        return self.to_dict() != other.to_dict()
