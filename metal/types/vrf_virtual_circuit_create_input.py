# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from metal.types.base_model_ import Model
from metal import util


class VrfVirtualCircuitCreateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, customer_ip: str=None, description: str=None, md5: str=None, metal_ip: str=None, name: str=None, nni_vlan: int=None, peer_asn: int=None, project_id: str=None, speed: int=None, subnet: str=None, tags: List[str]=None, vrf: str=None):
        """VrfVirtualCircuitCreateInput - a model defined in OpenAPI

        :param customer_ip: The customer_ip of this VrfVirtualCircuitCreateInput.
        :param description: The description of this VrfVirtualCircuitCreateInput.
        :param md5: The md5 of this VrfVirtualCircuitCreateInput.
        :param metal_ip: The metal_ip of this VrfVirtualCircuitCreateInput.
        :param name: The name of this VrfVirtualCircuitCreateInput.
        :param nni_vlan: The nni_vlan of this VrfVirtualCircuitCreateInput.
        :param peer_asn: The peer_asn of this VrfVirtualCircuitCreateInput.
        :param project_id: The project_id of this VrfVirtualCircuitCreateInput.
        :param speed: The speed of this VrfVirtualCircuitCreateInput.
        :param subnet: The subnet of this VrfVirtualCircuitCreateInput.
        :param tags: The tags of this VrfVirtualCircuitCreateInput.
        :param vrf: The vrf of this VrfVirtualCircuitCreateInput.
        """
        self.openapi_types = {
            'customer_ip': str,
            'description': str,
            'md5': str,
            'metal_ip': str,
            'name': str,
            'nni_vlan': int,
            'peer_asn': int,
            'project_id': str,
            'speed': int,
            'subnet': str,
            'tags': List[str],
            'vrf': str
        }

        self.attribute_map = {
            'customer_ip': 'customer_ip',
            'description': 'description',
            'md5': 'md5',
            'metal_ip': 'metal_ip',
            'name': 'name',
            'nni_vlan': 'nni_vlan',
            'peer_asn': 'peer_asn',
            'project_id': 'project_id',
            'speed': 'speed',
            'subnet': 'subnet',
            'tags': 'tags',
            'vrf': 'vrf'
        }

        self._customer_ip = customer_ip
        self._description = description
        self._md5 = md5
        self._metal_ip = metal_ip
        self._name = name
        self._nni_vlan = nni_vlan
        self._peer_asn = peer_asn
        self._project_id = project_id
        self._speed = speed
        self._subnet = subnet
        self._tags = tags
        self._vrf = vrf

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VrfVirtualCircuitCreateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VrfVirtualCircuitCreateInput of this VrfVirtualCircuitCreateInput.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_ip(self):
        """Gets the customer_ip of this VrfVirtualCircuitCreateInput.

        An IP address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used.

        :return: The customer_ip of this VrfVirtualCircuitCreateInput.
        :rtype: str
        """
        return self._customer_ip

    @customer_ip.setter
    def customer_ip(self, customer_ip):
        """Sets the customer_ip of this VrfVirtualCircuitCreateInput.

        An IP address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used.

        :param customer_ip: The customer_ip of this VrfVirtualCircuitCreateInput.
        :type customer_ip: str
        """

        self._customer_ip = customer_ip

    @property
    def description(self):
        """Gets the description of this VrfVirtualCircuitCreateInput.


        :return: The description of this VrfVirtualCircuitCreateInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VrfVirtualCircuitCreateInput.


        :param description: The description of this VrfVirtualCircuitCreateInput.
        :type description: str
        """

        self._description = description

    @property
    def md5(self):
        """Gets the md5 of this VrfVirtualCircuitCreateInput.

        The MD5 password for the BGP peering in plaintext (not a checksum).

        :return: The md5 of this VrfVirtualCircuitCreateInput.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this VrfVirtualCircuitCreateInput.

        The MD5 password for the BGP peering in plaintext (not a checksum).

        :param md5: The md5 of this VrfVirtualCircuitCreateInput.
        :type md5: str
        """

        self._md5 = md5

    @property
    def metal_ip(self):
        """Gets the metal_ip of this VrfVirtualCircuitCreateInput.

        An IP address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used.

        :return: The metal_ip of this VrfVirtualCircuitCreateInput.
        :rtype: str
        """
        return self._metal_ip

    @metal_ip.setter
    def metal_ip(self, metal_ip):
        """Sets the metal_ip of this VrfVirtualCircuitCreateInput.

        An IP address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used.

        :param metal_ip: The metal_ip of this VrfVirtualCircuitCreateInput.
        :type metal_ip: str
        """

        self._metal_ip = metal_ip

    @property
    def name(self):
        """Gets the name of this VrfVirtualCircuitCreateInput.


        :return: The name of this VrfVirtualCircuitCreateInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VrfVirtualCircuitCreateInput.


        :param name: The name of this VrfVirtualCircuitCreateInput.
        :type name: str
        """

        self._name = name

    @property
    def nni_vlan(self):
        """Gets the nni_vlan of this VrfVirtualCircuitCreateInput.


        :return: The nni_vlan of this VrfVirtualCircuitCreateInput.
        :rtype: int
        """
        return self._nni_vlan

    @nni_vlan.setter
    def nni_vlan(self, nni_vlan):
        """Sets the nni_vlan of this VrfVirtualCircuitCreateInput.


        :param nni_vlan: The nni_vlan of this VrfVirtualCircuitCreateInput.
        :type nni_vlan: int
        """
        if nni_vlan is None:
            raise ValueError("Invalid value for `nni_vlan`, must not be `None`")
        if nni_vlan is not None and nni_vlan > 4094:
            raise ValueError("Invalid value for `nni_vlan`, must be a value less than or equal to `4094`")
        if nni_vlan is not None and nni_vlan < 2:
            raise ValueError("Invalid value for `nni_vlan`, must be a value greater than or equal to `2`")

        self._nni_vlan = nni_vlan

    @property
    def peer_asn(self):
        """Gets the peer_asn of this VrfVirtualCircuitCreateInput.

        The peer ASN that will be used with the VRF on the Virtual Circuit.

        :return: The peer_asn of this VrfVirtualCircuitCreateInput.
        :rtype: int
        """
        return self._peer_asn

    @peer_asn.setter
    def peer_asn(self, peer_asn):
        """Sets the peer_asn of this VrfVirtualCircuitCreateInput.

        The peer ASN that will be used with the VRF on the Virtual Circuit.

        :param peer_asn: The peer_asn of this VrfVirtualCircuitCreateInput.
        :type peer_asn: int
        """
        if peer_asn is None:
            raise ValueError("Invalid value for `peer_asn`, must not be `None`")

        self._peer_asn = peer_asn

    @property
    def project_id(self):
        """Gets the project_id of this VrfVirtualCircuitCreateInput.


        :return: The project_id of this VrfVirtualCircuitCreateInput.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this VrfVirtualCircuitCreateInput.


        :param project_id: The project_id of this VrfVirtualCircuitCreateInput.
        :type project_id: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")

        self._project_id = project_id

    @property
    def speed(self):
        """Gets the speed of this VrfVirtualCircuitCreateInput.

        speed can be passed as integer number representing bps speed or string (e.g. '52m' or '100g' or '4 gbps')

        :return: The speed of this VrfVirtualCircuitCreateInput.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this VrfVirtualCircuitCreateInput.

        speed can be passed as integer number representing bps speed or string (e.g. '52m' or '100g' or '4 gbps')

        :param speed: The speed of this VrfVirtualCircuitCreateInput.
        :type speed: int
        """

        self._speed = speed

    @property
    def subnet(self):
        """Gets the subnet of this VrfVirtualCircuitCreateInput.

        The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP. The subnet specified must be contained within an already-defined IP Range for the VRF.

        :return: The subnet of this VrfVirtualCircuitCreateInput.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this VrfVirtualCircuitCreateInput.

        The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP. The subnet specified must be contained within an already-defined IP Range for the VRF.

        :param subnet: The subnet of this VrfVirtualCircuitCreateInput.
        :type subnet: str
        """
        if subnet is None:
            raise ValueError("Invalid value for `subnet`, must not be `None`")

        self._subnet = subnet

    @property
    def tags(self):
        """Gets the tags of this VrfVirtualCircuitCreateInput.


        :return: The tags of this VrfVirtualCircuitCreateInput.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VrfVirtualCircuitCreateInput.


        :param tags: The tags of this VrfVirtualCircuitCreateInput.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def vrf(self):
        """Gets the vrf of this VrfVirtualCircuitCreateInput.

        The UUID of the VRF that will be associated with the Virtual Circuit.

        :return: The vrf of this VrfVirtualCircuitCreateInput.
        :rtype: str
        """
        return self._vrf

    @vrf.setter
    def vrf(self, vrf):
        """Sets the vrf of this VrfVirtualCircuitCreateInput.

        The UUID of the VRF that will be associated with the Virtual Circuit.

        :param vrf: The vrf of this VrfVirtualCircuitCreateInput.
        :type vrf: str
        """
        if vrf is None:
            raise ValueError("Invalid value for `vrf`, must not be `None`")

        self._vrf = vrf
