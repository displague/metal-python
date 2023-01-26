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


class DeviceActionInput(object):
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
        'type': 'str',
        'force_delete': 'bool',
        'deprovision_fast': 'bool',
        'preserve_data': 'bool',
        'operating_system': 'str',
        'ipxe_script_url': 'str'
    }

    attribute_map = {
        'type': 'type',
        'force_delete': 'force_delete',
        'deprovision_fast': 'deprovision_fast',
        'preserve_data': 'preserve_data',
        'operating_system': 'operating_system',
        'ipxe_script_url': 'ipxe_script_url'
    }

    def __init__(self, type=None, force_delete=None, deprovision_fast=None, preserve_data=None, operating_system=None, ipxe_script_url=None, local_vars_configuration=None):  # noqa: E501
        """DeviceActionInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._force_delete = None
        self._deprovision_fast = None
        self._preserve_data = None
        self._operating_system = None
        self._ipxe_script_url = None
        self.discriminator = None

        self.type = type
        if force_delete is not None:
            self.force_delete = force_delete
        if deprovision_fast is not None:
            self.deprovision_fast = deprovision_fast
        if preserve_data is not None:
            self.preserve_data = preserve_data
        if operating_system is not None:
            self.operating_system = operating_system
        if ipxe_script_url is not None:
            self.ipxe_script_url = ipxe_script_url

    @property
    def type(self):
        """Gets the type of this DeviceActionInput.  # noqa: E501

        Action to perform. See Device.actions for possible actions.  # noqa: E501

        :return: The type of this DeviceActionInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceActionInput.

        Action to perform. See Device.actions for possible actions.  # noqa: E501

        :param type: The type of this DeviceActionInput.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["power_on", "power_off", "reboot", "rescue", "reinstall"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def force_delete(self):
        """Gets the force_delete of this DeviceActionInput.  # noqa: E501

        May be required to perform actions under certain conditions  # noqa: E501

        :return: The force_delete of this DeviceActionInput.  # noqa: E501
        :rtype: bool
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        """Sets the force_delete of this DeviceActionInput.

        May be required to perform actions under certain conditions  # noqa: E501

        :param force_delete: The force_delete of this DeviceActionInput.  # noqa: E501
        :type force_delete: bool
        """

        self._force_delete = force_delete

    @property
    def deprovision_fast(self):
        """Gets the deprovision_fast of this DeviceActionInput.  # noqa: E501

        When type is `reinstall`, enabling fast deprovisioning will bypass full disk wiping.  # noqa: E501

        :return: The deprovision_fast of this DeviceActionInput.  # noqa: E501
        :rtype: bool
        """
        return self._deprovision_fast

    @deprovision_fast.setter
    def deprovision_fast(self, deprovision_fast):
        """Sets the deprovision_fast of this DeviceActionInput.

        When type is `reinstall`, enabling fast deprovisioning will bypass full disk wiping.  # noqa: E501

        :param deprovision_fast: The deprovision_fast of this DeviceActionInput.  # noqa: E501
        :type deprovision_fast: bool
        """

        self._deprovision_fast = deprovision_fast

    @property
    def preserve_data(self):
        """Gets the preserve_data of this DeviceActionInput.  # noqa: E501

        When type is `reinstall`, preserve the existing data on all disks except the operating-system disk.  # noqa: E501

        :return: The preserve_data of this DeviceActionInput.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_data

    @preserve_data.setter
    def preserve_data(self, preserve_data):
        """Sets the preserve_data of this DeviceActionInput.

        When type is `reinstall`, preserve the existing data on all disks except the operating-system disk.  # noqa: E501

        :param preserve_data: The preserve_data of this DeviceActionInput.  # noqa: E501
        :type preserve_data: bool
        """

        self._preserve_data = preserve_data

    @property
    def operating_system(self):
        """Gets the operating_system of this DeviceActionInput.  # noqa: E501

        When type is `reinstall`, use this `operating_system` (defaults to the current `operating system`)  # noqa: E501

        :return: The operating_system of this DeviceActionInput.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this DeviceActionInput.

        When type is `reinstall`, use this `operating_system` (defaults to the current `operating system`)  # noqa: E501

        :param operating_system: The operating_system of this DeviceActionInput.  # noqa: E501
        :type operating_system: str
        """

        self._operating_system = operating_system

    @property
    def ipxe_script_url(self):
        """Gets the ipxe_script_url of this DeviceActionInput.  # noqa: E501

        When type is `reinstall`, use this `ipxe_script_url` (`operating_system` must be `custom_ipxe`, defaults to the current `ipxe_script_url`)  # noqa: E501

        :return: The ipxe_script_url of this DeviceActionInput.  # noqa: E501
        :rtype: str
        """
        return self._ipxe_script_url

    @ipxe_script_url.setter
    def ipxe_script_url(self, ipxe_script_url):
        """Sets the ipxe_script_url of this DeviceActionInput.

        When type is `reinstall`, use this `ipxe_script_url` (`operating_system` must be `custom_ipxe`, defaults to the current `ipxe_script_url`)  # noqa: E501

        :param ipxe_script_url: The ipxe_script_url of this DeviceActionInput.  # noqa: E501
        :type ipxe_script_url: str
        """

        self._ipxe_script_url = ipxe_script_url

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
        if not isinstance(other, DeviceActionInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceActionInput):
            return True

        return self.to_dict() != other.to_dict()
