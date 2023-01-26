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


class VirtualCircuitListVirtualCircuitsInner(object):
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
        'bill': 'bool',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'nni_vlan': 'int',
        'port': 'Href',
        'project': 'Href',
        'speed': 'int',
        'status': 'str',
        'tags': 'list[str]',
        'virtual_network': 'Href',
        'vnid': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'customer_ip': 'str',
        'md5': 'str',
        'metal_ip': 'str',
        'peer_asn': 'int',
        'subnet': 'str',
        'vrf': 'Vrf'
    }

    attribute_map = {
        'bill': 'bill',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'nni_vlan': 'nni_vlan',
        'port': 'port',
        'project': 'project',
        'speed': 'speed',
        'status': 'status',
        'tags': 'tags',
        'virtual_network': 'virtual_network',
        'vnid': 'vnid',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'customer_ip': 'customer_ip',
        'md5': 'md5',
        'metal_ip': 'metal_ip',
        'peer_asn': 'peer_asn',
        'subnet': 'subnet',
        'vrf': 'vrf'
    }

    def __init__(self, bill=False, description=None, id=None, name=None, nni_vlan=None, port=None, project=None, speed=None, status=None, tags=None, virtual_network=None, vnid=None, created_at=None, updated_at=None, customer_ip=None, md5=None, metal_ip=None, peer_asn=None, subnet=None, vrf=None, local_vars_configuration=None):  # noqa: E501
        """VirtualCircuitListVirtualCircuitsInner - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._bill = None
        self._description = None
        self._id = None
        self._name = None
        self._nni_vlan = None
        self._port = None
        self._project = None
        self._speed = None
        self._status = None
        self._tags = None
        self._virtual_network = None
        self._vnid = None
        self._created_at = None
        self._updated_at = None
        self._customer_ip = None
        self._md5 = None
        self._metal_ip = None
        self._peer_asn = None
        self._subnet = None
        self._vrf = None
        self.discriminator = None

        self.bill = bill
        self.description = description
        self.id = id
        self.name = name
        self.nni_vlan = nni_vlan
        self.port = port
        self.project = project
        if speed is not None:
            self.speed = speed
        self.status = status
        self.tags = tags
        self.virtual_network = virtual_network
        self.vnid = vnid
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if customer_ip is not None:
            self.customer_ip = customer_ip
        if md5 is not None:
            self.md5 = md5
        if metal_ip is not None:
            self.metal_ip = metal_ip
        if peer_asn is not None:
            self.peer_asn = peer_asn
        if subnet is not None:
            self.subnet = subnet
        if vrf is not None:
            self.vrf = vrf

    @property
    def bill(self):
        """Gets the bill of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501

        True if the Virtual Circuit is being billed. Currently, only Virtual Circuits of Fabric VCs (Metal Billed) will be billed. Usage will start the first time the Virtual Circuit becomes active, and will not stop until it is deleted from Metal.  # noqa: E501

        :return: The bill of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: bool
        """
        return self._bill

    @bill.setter
    def bill(self, bill):
        """Sets the bill of this VirtualCircuitListVirtualCircuitsInner.

        True if the Virtual Circuit is being billed. Currently, only Virtual Circuits of Fabric VCs (Metal Billed) will be billed. Usage will start the first time the Virtual Circuit becomes active, and will not stop until it is deleted from Metal.  # noqa: E501

        :param bill: The bill of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type bill: bool
        """
        if self.local_vars_configuration.client_side_validation and bill is None:  # noqa: E501
            raise ValueError("Invalid value for `bill`, must not be `None`")  # noqa: E501

        self._bill = bill

    @property
    def description(self):
        """Gets the description of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The description of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualCircuitListVirtualCircuitsInner.


        :param description: The description of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The id of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualCircuitListVirtualCircuitsInner.


        :param id: The id of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The name of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualCircuitListVirtualCircuitsInner.


        :param name: The name of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def nni_vlan(self):
        """Gets the nni_vlan of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The nni_vlan of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: int
        """
        return self._nni_vlan

    @nni_vlan.setter
    def nni_vlan(self, nni_vlan):
        """Sets the nni_vlan of this VirtualCircuitListVirtualCircuitsInner.


        :param nni_vlan: The nni_vlan of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type nni_vlan: int
        """
        if self.local_vars_configuration.client_side_validation and nni_vlan is None:  # noqa: E501
            raise ValueError("Invalid value for `nni_vlan`, must not be `None`")  # noqa: E501

        self._nni_vlan = nni_vlan

    @property
    def port(self):
        """Gets the port of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The port of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: Href
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this VirtualCircuitListVirtualCircuitsInner.


        :param port: The port of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type port: Href
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def project(self):
        """Gets the project of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The project of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: Href
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this VirtualCircuitListVirtualCircuitsInner.


        :param project: The project of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type project: Href
        """
        if self.local_vars_configuration.client_side_validation and project is None:  # noqa: E501
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def speed(self):
        """Gets the speed of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501

        integer representing bps speed  # noqa: E501

        :return: The speed of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this VirtualCircuitListVirtualCircuitsInner.

        integer representing bps speed  # noqa: E501

        :param speed: The speed of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type speed: int
        """

        self._speed = speed

    @property
    def status(self):
        """Gets the status of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The status of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VirtualCircuitListVirtualCircuitsInner.


        :param status: The status of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The tags of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VirtualCircuitListVirtualCircuitsInner.


        :param tags: The tags of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def virtual_network(self):
        """Gets the virtual_network of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The virtual_network of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: Href
        """
        return self._virtual_network

    @virtual_network.setter
    def virtual_network(self, virtual_network):
        """Sets the virtual_network of this VirtualCircuitListVirtualCircuitsInner.


        :param virtual_network: The virtual_network of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type virtual_network: Href
        """
        if self.local_vars_configuration.client_side_validation and virtual_network is None:  # noqa: E501
            raise ValueError("Invalid value for `virtual_network`, must not be `None`")  # noqa: E501

        self._virtual_network = virtual_network

    @property
    def vnid(self):
        """Gets the vnid of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The vnid of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: int
        """
        return self._vnid

    @vnid.setter
    def vnid(self, vnid):
        """Sets the vnid of this VirtualCircuitListVirtualCircuitsInner.


        :param vnid: The vnid of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type vnid: int
        """
        if self.local_vars_configuration.client_side_validation and vnid is None:  # noqa: E501
            raise ValueError("Invalid value for `vnid`, must not be `None`")  # noqa: E501

        self._vnid = vnid

    @property
    def created_at(self):
        """Gets the created_at of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The created_at of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VirtualCircuitListVirtualCircuitsInner.


        :param created_at: The created_at of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The updated_at of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VirtualCircuitListVirtualCircuitsInner.


        :param updated_at: The updated_at of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def customer_ip(self):
        """Gets the customer_ip of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501

        An IP address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used.  # noqa: E501

        :return: The customer_ip of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: str
        """
        return self._customer_ip

    @customer_ip.setter
    def customer_ip(self, customer_ip):
        """Sets the customer_ip of this VirtualCircuitListVirtualCircuitsInner.

        An IP address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used.  # noqa: E501

        :param customer_ip: The customer_ip of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type customer_ip: str
        """

        self._customer_ip = customer_ip

    @property
    def md5(self):
        """Gets the md5 of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501

        The MD5 password for the BGP peering in plaintext (not a checksum).  # noqa: E501

        :return: The md5 of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this VirtualCircuitListVirtualCircuitsInner.

        The MD5 password for the BGP peering in plaintext (not a checksum).  # noqa: E501

        :param md5: The md5 of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type md5: str
        """

        self._md5 = md5

    @property
    def metal_ip(self):
        """Gets the metal_ip of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501

        An IP address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used.  # noqa: E501

        :return: The metal_ip of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: str
        """
        return self._metal_ip

    @metal_ip.setter
    def metal_ip(self, metal_ip):
        """Sets the metal_ip of this VirtualCircuitListVirtualCircuitsInner.

        An IP address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used.  # noqa: E501

        :param metal_ip: The metal_ip of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type metal_ip: str
        """

        self._metal_ip = metal_ip

    @property
    def peer_asn(self):
        """Gets the peer_asn of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501

        The peer ASN that will be used with the VRF on the Virtual Circuit.  # noqa: E501

        :return: The peer_asn of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: int
        """
        return self._peer_asn

    @peer_asn.setter
    def peer_asn(self, peer_asn):
        """Sets the peer_asn of this VirtualCircuitListVirtualCircuitsInner.

        The peer ASN that will be used with the VRF on the Virtual Circuit.  # noqa: E501

        :param peer_asn: The peer_asn of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type peer_asn: int
        """

        self._peer_asn = peer_asn

    @property
    def subnet(self):
        """Gets the subnet of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501

        The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP.  # noqa: E501

        :return: The subnet of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this VirtualCircuitListVirtualCircuitsInner.

        The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP.  # noqa: E501

        :param subnet: The subnet of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type subnet: str
        """

        self._subnet = subnet

    @property
    def vrf(self):
        """Gets the vrf of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501


        :return: The vrf of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :rtype: Vrf
        """
        return self._vrf

    @vrf.setter
    def vrf(self, vrf):
        """Sets the vrf of this VirtualCircuitListVirtualCircuitsInner.


        :param vrf: The vrf of this VirtualCircuitListVirtualCircuitsInner.  # noqa: E501
        :type vrf: Vrf
        """

        self._vrf = vrf

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
        if not isinstance(other, VirtualCircuitListVirtualCircuitsInner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualCircuitListVirtualCircuitsInner):
            return True

        return self.to_dict() != other.to_dict()