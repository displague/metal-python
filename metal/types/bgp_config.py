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


class BgpConfig(object):
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
        'asn': 'int',
        'created_at': 'datetime',
        'deployment_type': 'str',
        'href': 'str',
        'id': 'str',
        'max_prefix': 'int',
        'md5': 'str',
        'project': 'Href',
        'ranges': 'list[GlobalBgpRange]',
        'requested_at': 'datetime',
        'route_object': 'str',
        'sessions': 'list[BgpSession]',
        'status': 'str'
    }

    attribute_map = {
        'asn': 'asn',
        'created_at': 'created_at',
        'deployment_type': 'deployment_type',
        'href': 'href',
        'id': 'id',
        'max_prefix': 'max_prefix',
        'md5': 'md5',
        'project': 'project',
        'ranges': 'ranges',
        'requested_at': 'requested_at',
        'route_object': 'route_object',
        'sessions': 'sessions',
        'status': 'status'
    }

    def __init__(self, asn=None, created_at=None, deployment_type=None, href=None, id=None, max_prefix=10, md5=None, project=None, ranges=None, requested_at=None, route_object=None, sessions=None, status=None, local_vars_configuration=None):  # noqa: E501
        """BgpConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._asn = None
        self._created_at = None
        self._deployment_type = None
        self._href = None
        self._id = None
        self._max_prefix = None
        self._md5 = None
        self._project = None
        self._ranges = None
        self._requested_at = None
        self._route_object = None
        self._sessions = None
        self._status = None
        self.discriminator = None

        if asn is not None:
            self.asn = asn
        if created_at is not None:
            self.created_at = created_at
        if deployment_type is not None:
            self.deployment_type = deployment_type
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if max_prefix is not None:
            self.max_prefix = max_prefix
        self.md5 = md5
        if project is not None:
            self.project = project
        if ranges is not None:
            self.ranges = ranges
        if requested_at is not None:
            self.requested_at = requested_at
        if route_object is not None:
            self.route_object = route_object
        if sessions is not None:
            self.sessions = sessions
        if status is not None:
            self.status = status

    @property
    def asn(self):
        """Gets the asn of this BgpConfig.  # noqa: E501

        Autonomous System Number. ASN is required with Global BGP. With Local BGP the private ASN, 65000, is assigned.  # noqa: E501

        :return: The asn of this BgpConfig.  # noqa: E501
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this BgpConfig.

        Autonomous System Number. ASN is required with Global BGP. With Local BGP the private ASN, 65000, is assigned.  # noqa: E501

        :param asn: The asn of this BgpConfig.  # noqa: E501
        :type asn: int
        """

        self._asn = asn

    @property
    def created_at(self):
        """Gets the created_at of this BgpConfig.  # noqa: E501


        :return: The created_at of this BgpConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BgpConfig.


        :param created_at: The created_at of this BgpConfig.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def deployment_type(self):
        """Gets the deployment_type of this BgpConfig.  # noqa: E501

        In a Local BGP deployment, a customer uses an internal ASN to control routes within a single Equinix Metal datacenter. This means that the routes are never advertised to the global Internet. Global BGP, on the other hand, requires a customer to have a registered ASN and IP space.   # noqa: E501

        :return: The deployment_type of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this BgpConfig.

        In a Local BGP deployment, a customer uses an internal ASN to control routes within a single Equinix Metal datacenter. This means that the routes are never advertised to the global Internet. Global BGP, on the other hand, requires a customer to have a registered ASN and IP space.   # noqa: E501

        :param deployment_type: The deployment_type of this BgpConfig.  # noqa: E501
        :type deployment_type: str
        """
        allowed_values = ["global", "local"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deployment_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deployment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_type, allowed_values)
            )

        self._deployment_type = deployment_type

    @property
    def href(self):
        """Gets the href of this BgpConfig.  # noqa: E501


        :return: The href of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BgpConfig.


        :param href: The href of this BgpConfig.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this BgpConfig.  # noqa: E501


        :return: The id of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BgpConfig.


        :param id: The id of this BgpConfig.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def max_prefix(self):
        """Gets the max_prefix of this BgpConfig.  # noqa: E501

        The maximum number of route filters allowed per server  # noqa: E501

        :return: The max_prefix of this BgpConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_prefix

    @max_prefix.setter
    def max_prefix(self, max_prefix):
        """Sets the max_prefix of this BgpConfig.

        The maximum number of route filters allowed per server  # noqa: E501

        :param max_prefix: The max_prefix of this BgpConfig.  # noqa: E501
        :type max_prefix: int
        """

        self._max_prefix = max_prefix

    @property
    def md5(self):
        """Gets the md5 of this BgpConfig.  # noqa: E501

        (Optional) Password for BGP session in plaintext (not a checksum)  # noqa: E501

        :return: The md5 of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this BgpConfig.

        (Optional) Password for BGP session in plaintext (not a checksum)  # noqa: E501

        :param md5: The md5 of this BgpConfig.  # noqa: E501
        :type md5: str
        """

        self._md5 = md5

    @property
    def project(self):
        """Gets the project of this BgpConfig.  # noqa: E501


        :return: The project of this BgpConfig.  # noqa: E501
        :rtype: Href
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this BgpConfig.


        :param project: The project of this BgpConfig.  # noqa: E501
        :type project: Href
        """

        self._project = project

    @property
    def ranges(self):
        """Gets the ranges of this BgpConfig.  # noqa: E501

        The IP block ranges associated to the ASN (Populated in Global BGP only)  # noqa: E501

        :return: The ranges of this BgpConfig.  # noqa: E501
        :rtype: list[GlobalBgpRange]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """Sets the ranges of this BgpConfig.

        The IP block ranges associated to the ASN (Populated in Global BGP only)  # noqa: E501

        :param ranges: The ranges of this BgpConfig.  # noqa: E501
        :type ranges: list[GlobalBgpRange]
        """

        self._ranges = ranges

    @property
    def requested_at(self):
        """Gets the requested_at of this BgpConfig.  # noqa: E501


        :return: The requested_at of this BgpConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._requested_at

    @requested_at.setter
    def requested_at(self, requested_at):
        """Sets the requested_at of this BgpConfig.


        :param requested_at: The requested_at of this BgpConfig.  # noqa: E501
        :type requested_at: datetime
        """

        self._requested_at = requested_at

    @property
    def route_object(self):
        """Gets the route_object of this BgpConfig.  # noqa: E501

        Specifies AS-MACRO (aka AS-SET) to use when building client route filters  # noqa: E501

        :return: The route_object of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._route_object

    @route_object.setter
    def route_object(self, route_object):
        """Sets the route_object of this BgpConfig.

        Specifies AS-MACRO (aka AS-SET) to use when building client route filters  # noqa: E501

        :param route_object: The route_object of this BgpConfig.  # noqa: E501
        :type route_object: str
        """

        self._route_object = route_object

    @property
    def sessions(self):
        """Gets the sessions of this BgpConfig.  # noqa: E501

        The direct connections between neighboring routers that want to exchange routing information.  # noqa: E501

        :return: The sessions of this BgpConfig.  # noqa: E501
        :rtype: list[BgpSession]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        """Sets the sessions of this BgpConfig.

        The direct connections between neighboring routers that want to exchange routing information.  # noqa: E501

        :param sessions: The sessions of this BgpConfig.  # noqa: E501
        :type sessions: list[BgpSession]
        """

        self._sessions = sessions

    @property
    def status(self):
        """Gets the status of this BgpConfig.  # noqa: E501

        Status of the BGP Config. Status \"requested\" is valid only with the \"global\" deployment_type.  # noqa: E501

        :return: The status of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BgpConfig.

        Status of the BGP Config. Status \"requested\" is valid only with the \"global\" deployment_type.  # noqa: E501

        :param status: The status of this BgpConfig.  # noqa: E501
        :type status: str
        """
        allowed_values = ["requested", "enabled", "disabled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, BgpConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BgpConfig):
            return True

        return self.to_dict() != other.to_dict()
