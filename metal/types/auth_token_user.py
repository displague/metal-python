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


class AuthTokenUser(object):
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
        'avatar_thumb_url': 'str',
        'avatar_url': 'str',
        'created_at': 'datetime',
        'customdata': 'object',
        'email': 'str',
        'emails': 'list[Href]',
        'first_name': 'str',
        'fraud_score': 'str',
        'full_name': 'str',
        'href': 'str',
        'id': 'str',
        'last_login_at': 'datetime',
        'last_name': 'str',
        'max_organizations': 'int',
        'max_projects': 'int',
        'phone_number': 'str',
        'short_id': 'str',
        'timezone': 'str',
        'two_factor_auth': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'avatar_thumb_url': 'avatar_thumb_url',
        'avatar_url': 'avatar_url',
        'created_at': 'created_at',
        'customdata': 'customdata',
        'email': 'email',
        'emails': 'emails',
        'first_name': 'first_name',
        'fraud_score': 'fraud_score',
        'full_name': 'full_name',
        'href': 'href',
        'id': 'id',
        'last_login_at': 'last_login_at',
        'last_name': 'last_name',
        'max_organizations': 'max_organizations',
        'max_projects': 'max_projects',
        'phone_number': 'phone_number',
        'short_id': 'short_id',
        'timezone': 'timezone',
        'two_factor_auth': 'two_factor_auth',
        'updated_at': 'updated_at'
    }

    def __init__(self, avatar_thumb_url=None, avatar_url=None, created_at=None, customdata=None, email=None, emails=None, first_name=None, fraud_score=None, full_name=None, href=None, id=None, last_login_at=None, last_name=None, max_organizations=None, max_projects=None, phone_number=None, short_id=None, timezone=None, two_factor_auth=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """AuthTokenUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._avatar_thumb_url = None
        self._avatar_url = None
        self._created_at = None
        self._customdata = None
        self._email = None
        self._emails = None
        self._first_name = None
        self._fraud_score = None
        self._full_name = None
        self._href = None
        self._id = None
        self._last_login_at = None
        self._last_name = None
        self._max_organizations = None
        self._max_projects = None
        self._phone_number = None
        self._short_id = None
        self._timezone = None
        self._two_factor_auth = None
        self._updated_at = None
        self.discriminator = None

        if avatar_thumb_url is not None:
            self.avatar_thumb_url = avatar_thumb_url
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if created_at is not None:
            self.created_at = created_at
        if customdata is not None:
            self.customdata = customdata
        if email is not None:
            self.email = email
        if emails is not None:
            self.emails = emails
        if first_name is not None:
            self.first_name = first_name
        if fraud_score is not None:
            self.fraud_score = fraud_score
        if full_name is not None:
            self.full_name = full_name
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if last_login_at is not None:
            self.last_login_at = last_login_at
        if last_name is not None:
            self.last_name = last_name
        if max_organizations is not None:
            self.max_organizations = max_organizations
        if max_projects is not None:
            self.max_projects = max_projects
        if phone_number is not None:
            self.phone_number = phone_number
        if short_id is not None:
            self.short_id = short_id
        if timezone is not None:
            self.timezone = timezone
        if two_factor_auth is not None:
            self.two_factor_auth = two_factor_auth
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def avatar_thumb_url(self):
        """Gets the avatar_thumb_url of this AuthTokenUser.  # noqa: E501


        :return: The avatar_thumb_url of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._avatar_thumb_url

    @avatar_thumb_url.setter
    def avatar_thumb_url(self, avatar_thumb_url):
        """Sets the avatar_thumb_url of this AuthTokenUser.


        :param avatar_thumb_url: The avatar_thumb_url of this AuthTokenUser.  # noqa: E501
        :type avatar_thumb_url: str
        """

        self._avatar_thumb_url = avatar_thumb_url

    @property
    def avatar_url(self):
        """Gets the avatar_url of this AuthTokenUser.  # noqa: E501


        :return: The avatar_url of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this AuthTokenUser.


        :param avatar_url: The avatar_url of this AuthTokenUser.  # noqa: E501
        :type avatar_url: str
        """

        self._avatar_url = avatar_url

    @property
    def created_at(self):
        """Gets the created_at of this AuthTokenUser.  # noqa: E501


        :return: The created_at of this AuthTokenUser.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AuthTokenUser.


        :param created_at: The created_at of this AuthTokenUser.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def customdata(self):
        """Gets the customdata of this AuthTokenUser.  # noqa: E501


        :return: The customdata of this AuthTokenUser.  # noqa: E501
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this AuthTokenUser.


        :param customdata: The customdata of this AuthTokenUser.  # noqa: E501
        :type customdata: object
        """

        self._customdata = customdata

    @property
    def email(self):
        """Gets the email of this AuthTokenUser.  # noqa: E501


        :return: The email of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AuthTokenUser.


        :param email: The email of this AuthTokenUser.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def emails(self):
        """Gets the emails of this AuthTokenUser.  # noqa: E501


        :return: The emails of this AuthTokenUser.  # noqa: E501
        :rtype: list[Href]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this AuthTokenUser.


        :param emails: The emails of this AuthTokenUser.  # noqa: E501
        :type emails: list[Href]
        """

        self._emails = emails

    @property
    def first_name(self):
        """Gets the first_name of this AuthTokenUser.  # noqa: E501


        :return: The first_name of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AuthTokenUser.


        :param first_name: The first_name of this AuthTokenUser.  # noqa: E501
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def fraud_score(self):
        """Gets the fraud_score of this AuthTokenUser.  # noqa: E501


        :return: The fraud_score of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._fraud_score

    @fraud_score.setter
    def fraud_score(self, fraud_score):
        """Sets the fraud_score of this AuthTokenUser.


        :param fraud_score: The fraud_score of this AuthTokenUser.  # noqa: E501
        :type fraud_score: str
        """

        self._fraud_score = fraud_score

    @property
    def full_name(self):
        """Gets the full_name of this AuthTokenUser.  # noqa: E501


        :return: The full_name of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this AuthTokenUser.


        :param full_name: The full_name of this AuthTokenUser.  # noqa: E501
        :type full_name: str
        """

        self._full_name = full_name

    @property
    def href(self):
        """Gets the href of this AuthTokenUser.  # noqa: E501


        :return: The href of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AuthTokenUser.


        :param href: The href of this AuthTokenUser.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this AuthTokenUser.  # noqa: E501


        :return: The id of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthTokenUser.


        :param id: The id of this AuthTokenUser.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def last_login_at(self):
        """Gets the last_login_at of this AuthTokenUser.  # noqa: E501


        :return: The last_login_at of this AuthTokenUser.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_at

    @last_login_at.setter
    def last_login_at(self, last_login_at):
        """Sets the last_login_at of this AuthTokenUser.


        :param last_login_at: The last_login_at of this AuthTokenUser.  # noqa: E501
        :type last_login_at: datetime
        """

        self._last_login_at = last_login_at

    @property
    def last_name(self):
        """Gets the last_name of this AuthTokenUser.  # noqa: E501


        :return: The last_name of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AuthTokenUser.


        :param last_name: The last_name of this AuthTokenUser.  # noqa: E501
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def max_organizations(self):
        """Gets the max_organizations of this AuthTokenUser.  # noqa: E501


        :return: The max_organizations of this AuthTokenUser.  # noqa: E501
        :rtype: int
        """
        return self._max_organizations

    @max_organizations.setter
    def max_organizations(self, max_organizations):
        """Sets the max_organizations of this AuthTokenUser.


        :param max_organizations: The max_organizations of this AuthTokenUser.  # noqa: E501
        :type max_organizations: int
        """

        self._max_organizations = max_organizations

    @property
    def max_projects(self):
        """Gets the max_projects of this AuthTokenUser.  # noqa: E501


        :return: The max_projects of this AuthTokenUser.  # noqa: E501
        :rtype: int
        """
        return self._max_projects

    @max_projects.setter
    def max_projects(self, max_projects):
        """Sets the max_projects of this AuthTokenUser.


        :param max_projects: The max_projects of this AuthTokenUser.  # noqa: E501
        :type max_projects: int
        """

        self._max_projects = max_projects

    @property
    def phone_number(self):
        """Gets the phone_number of this AuthTokenUser.  # noqa: E501


        :return: The phone_number of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this AuthTokenUser.


        :param phone_number: The phone_number of this AuthTokenUser.  # noqa: E501
        :type phone_number: str
        """

        self._phone_number = phone_number

    @property
    def short_id(self):
        """Gets the short_id of this AuthTokenUser.  # noqa: E501


        :return: The short_id of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        """Sets the short_id of this AuthTokenUser.


        :param short_id: The short_id of this AuthTokenUser.  # noqa: E501
        :type short_id: str
        """

        self._short_id = short_id

    @property
    def timezone(self):
        """Gets the timezone of this AuthTokenUser.  # noqa: E501


        :return: The timezone of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this AuthTokenUser.


        :param timezone: The timezone of this AuthTokenUser.  # noqa: E501
        :type timezone: str
        """

        self._timezone = timezone

    @property
    def two_factor_auth(self):
        """Gets the two_factor_auth of this AuthTokenUser.  # noqa: E501


        :return: The two_factor_auth of this AuthTokenUser.  # noqa: E501
        :rtype: str
        """
        return self._two_factor_auth

    @two_factor_auth.setter
    def two_factor_auth(self, two_factor_auth):
        """Sets the two_factor_auth of this AuthTokenUser.


        :param two_factor_auth: The two_factor_auth of this AuthTokenUser.  # noqa: E501
        :type two_factor_auth: str
        """

        self._two_factor_auth = two_factor_auth

    @property
    def updated_at(self):
        """Gets the updated_at of this AuthTokenUser.  # noqa: E501


        :return: The updated_at of this AuthTokenUser.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AuthTokenUser.


        :param updated_at: The updated_at of this AuthTokenUser.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, AuthTokenUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthTokenUser):
            return True

        return self.to_dict() != other.to_dict()
