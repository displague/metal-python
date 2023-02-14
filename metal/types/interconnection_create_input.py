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


class InterconnectionCreateInput(object):
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
        'contact_email': 'str',
        'description': 'str',
        'metro': 'str',
        'mode': 'str',
        'name': 'str',
        'project': 'str',
        'redundancy': 'str',
        'service_token_type': 'str',
        'speed': 'int',
        'tags': 'list[str]',
        'type': 'str',
        'vlans': 'list[int]',
        'vrfs': 'list[str]'
    }

    attribute_map = {
        'contact_email': 'contact_email',
        'description': 'description',
        'metro': 'metro',
        'mode': 'mode',
        'name': 'name',
        'project': 'project',
        'redundancy': 'redundancy',
        'service_token_type': 'service_token_type',
        'speed': 'speed',
        'tags': 'tags',
        'type': 'type',
        'vlans': 'vlans',
        'vrfs': 'vrfs'
    }

    def __init__(self, contact_email=None, description=None, metro=None, mode=None, name=None, project=None, redundancy=None, service_token_type=None, speed=None, tags=None, type=None, vlans=None, vrfs=None, local_vars_configuration=None):  # noqa: E501
        """InterconnectionCreateInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._contact_email = None
        self._description = None
        self._metro = None
        self._mode = None
        self._name = None
        self._project = None
        self._redundancy = None
        self._service_token_type = None
        self._speed = None
        self._tags = None
        self._type = None
        self._vlans = None
        self._vrfs = None
        self.discriminator = None

        if contact_email is not None:
            self.contact_email = contact_email
        if description is not None:
            self.description = description
        self.metro = metro
        if mode is not None:
            self.mode = mode
        self.name = name
        if project is not None:
            self.project = project
        self.redundancy = redundancy
        if service_token_type is not None:
            self.service_token_type = service_token_type
        if speed is not None:
            self.speed = speed
        if tags is not None:
            self.tags = tags
        self.type = type
        if vlans is not None:
            self.vlans = vlans
        if vrfs is not None:
            self.vrfs = vrfs

    @property
    def contact_email(self):
        """Gets the contact_email of this InterconnectionCreateInput.  # noqa: E501


        :return: The contact_email of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this InterconnectionCreateInput.


        :param contact_email: The contact_email of this InterconnectionCreateInput.  # noqa: E501
        :type contact_email: str
        """

        self._contact_email = contact_email

    @property
    def description(self):
        """Gets the description of this InterconnectionCreateInput.  # noqa: E501


        :return: The description of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InterconnectionCreateInput.


        :param description: The description of this InterconnectionCreateInput.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def metro(self):
        """Gets the metro of this InterconnectionCreateInput.  # noqa: E501

        A Metro ID or code. For interconnections with Dedicated Ports, this will be the location of the issued Dedicated Ports. When creating Fabric VCs (Metal Billed), this is where interconnection will be originating from, as we pre-authorize the use of one of our shared ports as the origin of the interconnection using A-Side service tokens. We only allow local connections for Fabric VCs (Metal Billed), so the destination location must be the same as the origin. For Fabric VCs (Fabric Billed), or shared connections, this will be the destination of the interconnection. We allow remote connections for Fabric VCs (Fabric Billed), so the origin of the interconnection can be a different metro set here.  # noqa: E501

        :return: The metro of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this InterconnectionCreateInput.

        A Metro ID or code. For interconnections with Dedicated Ports, this will be the location of the issued Dedicated Ports. When creating Fabric VCs (Metal Billed), this is where interconnection will be originating from, as we pre-authorize the use of one of our shared ports as the origin of the interconnection using A-Side service tokens. We only allow local connections for Fabric VCs (Metal Billed), so the destination location must be the same as the origin. For Fabric VCs (Fabric Billed), or shared connections, this will be the destination of the interconnection. We allow remote connections for Fabric VCs (Fabric Billed), so the origin of the interconnection can be a different metro set here.  # noqa: E501

        :param metro: The metro of this InterconnectionCreateInput.  # noqa: E501
        :type metro: str
        """
        if self.local_vars_configuration.client_side_validation and metro is None:  # noqa: E501
            raise ValueError("Invalid value for `metro`, must not be `None`")  # noqa: E501

        self._metro = metro

    @property
    def mode(self):
        """Gets the mode of this InterconnectionCreateInput.  # noqa: E501

        The mode of the interconnection (only relevant to Dedicated Ports). Fabric VCs won't have this field. Can be either 'standard' or 'tunnel'.   The default mode of an interconnection on a Dedicated Port is 'standard'. The mode can only be changed when there are no associated virtual circuits on the interconnection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances.  # noqa: E501

        :return: The mode of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this InterconnectionCreateInput.

        The mode of the interconnection (only relevant to Dedicated Ports). Fabric VCs won't have this field. Can be either 'standard' or 'tunnel'.   The default mode of an interconnection on a Dedicated Port is 'standard'. The mode can only be changed when there are no associated virtual circuits on the interconnection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances.  # noqa: E501

        :param mode: The mode of this InterconnectionCreateInput.  # noqa: E501
        :type mode: str
        """
        allowed_values = ["standard", "tunnel"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def name(self):
        """Gets the name of this InterconnectionCreateInput.  # noqa: E501


        :return: The name of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InterconnectionCreateInput.


        :param name: The name of this InterconnectionCreateInput.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def project(self):
        """Gets the project of this InterconnectionCreateInput.  # noqa: E501


        :return: The project of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this InterconnectionCreateInput.


        :param project: The project of this InterconnectionCreateInput.  # noqa: E501
        :type project: str
        """

        self._project = project

    @property
    def redundancy(self):
        """Gets the redundancy of this InterconnectionCreateInput.  # noqa: E501

        Either 'primary' or 'redundant'.  # noqa: E501

        :return: The redundancy of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._redundancy

    @redundancy.setter
    def redundancy(self, redundancy):
        """Sets the redundancy of this InterconnectionCreateInput.

        Either 'primary' or 'redundant'.  # noqa: E501

        :param redundancy: The redundancy of this InterconnectionCreateInput.  # noqa: E501
        :type redundancy: str
        """
        if self.local_vars_configuration.client_side_validation and redundancy is None:  # noqa: E501
            raise ValueError("Invalid value for `redundancy`, must not be `None`")  # noqa: E501

        self._redundancy = redundancy

    @property
    def service_token_type(self):
        """Gets the service_token_type of this InterconnectionCreateInput.  # noqa: E501

        Either 'a_side' or 'z_side'. Setting this field to 'a_side' will create an interconnection with Fabric VCs (Metal Billed). Setting this field to 'z_side' will create an interconnection with Fabric VCs (Fabric Billed). This is required when the 'type' is 'shared', but this is not applicable when the 'type' is 'dedicated'. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details.  # noqa: E501

        :return: The service_token_type of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._service_token_type

    @service_token_type.setter
    def service_token_type(self, service_token_type):
        """Sets the service_token_type of this InterconnectionCreateInput.

        Either 'a_side' or 'z_side'. Setting this field to 'a_side' will create an interconnection with Fabric VCs (Metal Billed). Setting this field to 'z_side' will create an interconnection with Fabric VCs (Fabric Billed). This is required when the 'type' is 'shared', but this is not applicable when the 'type' is 'dedicated'. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details.  # noqa: E501

        :param service_token_type: The service_token_type of this InterconnectionCreateInput.  # noqa: E501
        :type service_token_type: str
        """
        allowed_values = ["a_side", "z_side"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and service_token_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `service_token_type` ({0}), must be one of {1}"  # noqa: E501
                .format(service_token_type, allowed_values)
            )

        self._service_token_type = service_token_type

    @property
    def speed(self):
        """Gets the speed of this InterconnectionCreateInput.  # noqa: E501

        A interconnection speed, in bps, mbps, or gbps. For Dedicated Ports, this can be 10Gbps or 100Gbps. For Fabric VCs, this represents the maximum speed of the interconnection. For Fabric VCs (Metal Billed), this can only be one of the following:  ''50mbps'', ''200mbps'', ''500mbps'', ''1gbps'', ''2gbps'', ''5gbps'' or ''10gbps'', and is required for creation. For Fabric VCs (Fabric Billed), this field will always default to ''10gbps'' even if it is not provided. For example, ''500000000'', ''50m'', or' ''500mbps'' will all work as valid inputs.  # noqa: E501

        :return: The speed of this InterconnectionCreateInput.  # noqa: E501
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this InterconnectionCreateInput.

        A interconnection speed, in bps, mbps, or gbps. For Dedicated Ports, this can be 10Gbps or 100Gbps. For Fabric VCs, this represents the maximum speed of the interconnection. For Fabric VCs (Metal Billed), this can only be one of the following:  ''50mbps'', ''200mbps'', ''500mbps'', ''1gbps'', ''2gbps'', ''5gbps'' or ''10gbps'', and is required for creation. For Fabric VCs (Fabric Billed), this field will always default to ''10gbps'' even if it is not provided. For example, ''500000000'', ''50m'', or' ''500mbps'' will all work as valid inputs.  # noqa: E501

        :param speed: The speed of this InterconnectionCreateInput.  # noqa: E501
        :type speed: int
        """

        self._speed = speed

    @property
    def tags(self):
        """Gets the tags of this InterconnectionCreateInput.  # noqa: E501


        :return: The tags of this InterconnectionCreateInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InterconnectionCreateInput.


        :param tags: The tags of this InterconnectionCreateInput.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this InterconnectionCreateInput.  # noqa: E501

        Either 'shared' or 'dedicated'. The 'shared' type represents shared interconnections, or also known as Fabric VCs. The 'dedicated' type represents dedicated interconnections, or also known as Dedicated Ports.  # noqa: E501

        :return: The type of this InterconnectionCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InterconnectionCreateInput.

        Either 'shared' or 'dedicated'. The 'shared' type represents shared interconnections, or also known as Fabric VCs. The 'dedicated' type represents dedicated interconnections, or also known as Dedicated Ports.  # noqa: E501

        :param type: The type of this InterconnectionCreateInput.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def vlans(self):
        """Gets the vlans of this InterconnectionCreateInput.  # noqa: E501

        A list of one or two metro-based VLANs that will be set on the virtual circuits of primary and/or secondary (if redundant) interconnections respectively when creating Fabric VCs. VLANs can also be set after the interconnection is created, but are required to fully activate the interconnection. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details.  # noqa: E501

        :return: The vlans of this InterconnectionCreateInput.  # noqa: E501
        :rtype: list[int]
        """
        return self._vlans

    @vlans.setter
    def vlans(self, vlans):
        """Sets the vlans of this InterconnectionCreateInput.

        A list of one or two metro-based VLANs that will be set on the virtual circuits of primary and/or secondary (if redundant) interconnections respectively when creating Fabric VCs. VLANs can also be set after the interconnection is created, but are required to fully activate the interconnection. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details.  # noqa: E501

        :param vlans: The vlans of this InterconnectionCreateInput.  # noqa: E501
        :type vlans: list[int]
        """

        self._vlans = vlans

    @property
    def vrfs(self):
        """Gets the vrfs of this InterconnectionCreateInput.  # noqa: E501

        Can only be set when creating Fabric VCs in VRF(s). This field holds a list of VRF UUIDs that will be set automatically on the virtual circuits on creation, and can hold up to two UUIDs. Two UUIDs are required when requesting redundant Fabric VCs. The first UUID will be set on the primary virtual circuit, while the second UUID will be set on the secondary. The two UUIDs can be the same if both the primary and secondary virtual circuits will be in the same VRF. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details.  # noqa: E501

        :return: The vrfs of this InterconnectionCreateInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._vrfs

    @vrfs.setter
    def vrfs(self, vrfs):
        """Sets the vrfs of this InterconnectionCreateInput.

        Can only be set when creating Fabric VCs in VRF(s). This field holds a list of VRF UUIDs that will be set automatically on the virtual circuits on creation, and can hold up to two UUIDs. Two UUIDs are required when requesting redundant Fabric VCs. The first UUID will be set on the primary virtual circuit, while the second UUID will be set on the secondary. The two UUIDs can be the same if both the primary and secondary virtual circuits will be in the same VRF. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details.  # noqa: E501

        :param vrfs: The vrfs of this InterconnectionCreateInput.  # noqa: E501
        :type vrfs: list[str]
        """

        self._vrfs = vrfs

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
        if not isinstance(other, InterconnectionCreateInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InterconnectionCreateInput):
            return True

        return self.to_dict() != other.to_dict()
