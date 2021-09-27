import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.device_create_input_billing_cycle import DeviceCreateInputBillingCycle
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.device_create_input_customdata import DeviceCreateInputCustomdata
  from ..models.device_create_input_ip_addresses_inner import DeviceCreateInputIpAddressesInner
  from ..models.ssh_key_input import SSHKeyInput




T = TypeVar("T", bound="DeviceCreateInput")

@attr.s(auto_attribs=True)
class DeviceCreateInput:
    """
    Attributes:
        operating_system (str): The slug of the operating system to provision. Check the Equinix Metal operating system
            documentation for rules that may be imposed per operating system, including restrictions on IP address options
            and device plans.
        plan (str): The slug of the device plan to provision. Example: c3.large.x86.
        always_pxe (Union[Unset, bool]): When true, devices with a `custom_ipxe` OS will always boot to iPXE. The
            default setting of false ensures that iPXE will be used on only the
            first boot.
        billing_cycle (Union[Unset, DeviceCreateInputBillingCycle]): The billing cycle of the device.
        customdata (Union[Unset, DeviceCreateInputCustomdata]): Customdata is an arbitrary JSON value that can be
            accessed via the
            metadata service.
        description (Union[Unset, str]): Any description of the device or how it will be used. This may be used
            to inform other API consumers with project access.
        features (Union[Unset, List[str]]): The features attribute allows you to optionally specify what features your
            server should have.

            In the API shorthand syntax, all features listed are `required`:

            ```
            { "features": ["tpm"] }
            ```

            Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that
            feature if there are any available, you may specify that feature with a `preferred` value. The request will not
            fail if we have no servers with that feature in our inventory. The API offers an alternative syntax for mixing
            preferred and required features:

            ```
            { "features": { "tpm": "required", "raid": "preferred" } }
            ```

            The request will only fail if there are no available servers matching the required `tpm` criteria.
        hardware_reservation_id (Union[Unset, str]): The Hardware Reservation UUID to provision. Alternatively, `next-
            available` can be specified to select from any of the available hardware reservations. An error will be returned
            if the requested reservation option is not available.

            See [Reserved Hardware](https://metal.equinix.com/developers/docs/deploy/reserved/) for more details. Default:
            ''. Example: next-available.
        hostname (Union[Unset, str]): The hostname to use within the operating system. The same hostname may be used on
            multiple devices within a project.
        ip_addresses (Union[Unset, List['DeviceCreateInputIpAddressesInner']]): The `ip_addresses attribute will allow
            you to specify the addresses you want created with your device.

            The default value configures public IPv4, public IPv6, and private IPv4.

            Private IPv4 address is required. When specifying `ip_addresses`, one of the array items must enable private
            IPv4.

            Some operating systems require public IPv4 address. In those cases you will receive an error message if public
            IPv4 is not enabled.

            For example, to only configure your server with a private IPv4 address, you can send `{ "ip_addresses": [{
            "address_family": 4, "public": false }] }`.

            It is possible to request a subnet size larger than a `/30` by assigning addresses using the UUID(s) of
            ip_reservations in your project.

            For example, `{ "ip_addresses": [..., {"address_family": 4, "public": true, "ip_reservations": ["uuid1",
            "uuid2"]}] }`

            To access a server without public IPs, you can use our Out-of-Band console access (SOS) or proxy through another
            server in the project with public IPs enabled.
        ipxe_script_url (Union[Unset, str]): When set, the device will chainload an iPXE Script at boot fetched from the
            supplied URL.

            See [Custom iPXE](https://metal.equinix.com/developers/docs/operating-systems/custom-ipxe/) for more details.
        locked (Union[Unset, bool]): Whether the device should be locked, preventing accidental deletion.
        no_ssh_keys (Union[Unset, bool]): Overrides default behaviour of attaching all of the organization members ssh
            keys and project ssh keys to device if no specific keys specified
        private_ipv4_subnet_size (Union[Unset, float]): Deprecated. Use ip_addresses. Subnet range for addresses
            allocated to this device. Default: 28.0.
        project_ssh_keys (Union[Unset, List[str]]): A list of UUIDs identifying the device parent project
            that should be authorized to access this device (typically
            via /root/.ssh/authorized_keys). These keys will also appear in the device metadata.

            If no SSH keys are specified (`user_ssh_keys`, `project_ssh_keys`, and `ssh_keys` are all empty lists or
            omitted),
            all parent project keys, parent project members keys and organization members keys will be included. This
            behaviour can
            be changed with 'no_ssh_keys' option to omit any SSH key being added.
        public_ipv4_subnet_size (Union[Unset, float]): Deprecated. Use ip_addresses. Subnet range for addresses
            allocated to this device. Your project must have addresses available for a non-default request. Default: 31.0.
        spot_instance (Union[Unset, bool]): Create a spot instance. Spot instances are created with a maximum bid price.
            If the bid price is not met, the spot instance will be terminated as indicated by the `termination_time` field.
        spot_price_max (Union[Unset, float]): The maximum amount to bid for a spot instance. Example: 1.23.
        ssh_keys (Union[Unset, List['SSHKeyInput']]): A list of new or existing project ssh_keys
            that should be authorized to access this device (typically
            via /root/.ssh/authorized_keys). These keys will also
            appear in the device metadata.

            These keys are added in addition to any keys defined by
              `project_ssh_keys` and `user_ssh_keys`.
        tags (Union[Unset, List[str]]):
        termination_time (Union[Unset, datetime.datetime]):
        user_ssh_keys (Union[Unset, List[str]]): A list of UUIDs identifying the users
            that should be authorized to access this device (typically
            via /root/.ssh/authorized_keys).  These keys will also
            appear in the device metadata.

            The users must be members of the project or organization.

            If no SSH keys are specified (`user_ssh_keys`, `project_ssh_keys`, and `ssh_keys` are all empty lists or
            omitted),
            all parent project keys, parent project members keys and organization members keys will be included. This
            behaviour can
            be changed with 'no_ssh_keys' option to omit any SSH key being added.
        userdata (Union[Unset, str]): The userdata presented in the metadata service for this device.  Userdata is
            fetched and interpreted by the operating system installed on the device. Acceptable formats are determined by
            the operating system, with the exception of a special iPXE enabling syntax which is handled before the operating
            system starts.

            See [Server User Data](https://metal.equinix.com/developers/docs/servers/user-data/) and [Provisioning with
            Custom iPXE](https://metal.equinix.com/developers/docs/operating-systems/custom-ipxe/#provisioning-with-custom-
            ipxe) for more details.
    """

    operating_system: str
    plan: str
    always_pxe: Union[Unset, bool] = False
    billing_cycle: Union[Unset, DeviceCreateInputBillingCycle] = UNSET
    customdata: Union[Unset, 'DeviceCreateInputCustomdata'] = UNSET
    description: Union[Unset, str] = UNSET
    features: Union[Unset, List[str]] = UNSET
    hardware_reservation_id: Union[Unset, str] = ''
    hostname: Union[Unset, str] = UNSET
    ip_addresses: Union[Unset, List['DeviceCreateInputIpAddressesInner']] = UNSET
    ipxe_script_url: Union[Unset, str] = UNSET
    locked: Union[Unset, bool] = False
    no_ssh_keys: Union[Unset, bool] = False
    private_ipv4_subnet_size: Union[Unset, float] = 28.0
    project_ssh_keys: Union[Unset, List[str]] = UNSET
    public_ipv4_subnet_size: Union[Unset, float] = 31.0
    spot_instance: Union[Unset, bool] = UNSET
    spot_price_max: Union[Unset, float] = UNSET
    ssh_keys: Union[Unset, List['SSHKeyInput']] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    termination_time: Union[Unset, datetime.datetime] = UNSET
    user_ssh_keys: Union[Unset, List[str]] = UNSET
    userdata: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        operating_system = self.operating_system
        plan = self.plan
        always_pxe = self.always_pxe
        billing_cycle: Union[Unset, str] = UNSET
        if not isinstance(self.billing_cycle, Unset):
            billing_cycle = self.billing_cycle.value

        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        description = self.description
        features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features




        hardware_reservation_id = self.hardware_reservation_id
        hostname = self.hostname
        ip_addresses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = []
            for ip_addresses_item_data in self.ip_addresses:
                ip_addresses_item = ip_addresses_item_data.to_dict()

                ip_addresses.append(ip_addresses_item)




        ipxe_script_url = self.ipxe_script_url
        locked = self.locked
        no_ssh_keys = self.no_ssh_keys
        private_ipv4_subnet_size = self.private_ipv4_subnet_size
        project_ssh_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.project_ssh_keys, Unset):
            project_ssh_keys = self.project_ssh_keys




        public_ipv4_subnet_size = self.public_ipv4_subnet_size
        spot_instance = self.spot_instance
        spot_price_max = self.spot_price_max
        ssh_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ssh_keys, Unset):
            ssh_keys = []
            for ssh_keys_item_data in self.ssh_keys:
                ssh_keys_item = ssh_keys_item_data.to_dict()

                ssh_keys.append(ssh_keys_item)




        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        termination_time: Union[Unset, str] = UNSET
        if not isinstance(self.termination_time, Unset):
            termination_time = self.termination_time.isoformat()

        user_ssh_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_ssh_keys, Unset):
            user_ssh_keys = self.user_ssh_keys




        userdata = self.userdata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "operating_system": operating_system,
            "plan": plan,
        })
        if always_pxe is not UNSET:
            field_dict["always_pxe"] = always_pxe
        if billing_cycle is not UNSET:
            field_dict["billing_cycle"] = billing_cycle
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if description is not UNSET:
            field_dict["description"] = description
        if features is not UNSET:
            field_dict["features"] = features
        if hardware_reservation_id is not UNSET:
            field_dict["hardware_reservation_id"] = hardware_reservation_id
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if ip_addresses is not UNSET:
            field_dict["ip_addresses"] = ip_addresses
        if ipxe_script_url is not UNSET:
            field_dict["ipxe_script_url"] = ipxe_script_url
        if locked is not UNSET:
            field_dict["locked"] = locked
        if no_ssh_keys is not UNSET:
            field_dict["no_ssh_keys"] = no_ssh_keys
        if private_ipv4_subnet_size is not UNSET:
            field_dict["private_ipv4_subnet_size"] = private_ipv4_subnet_size
        if project_ssh_keys is not UNSET:
            field_dict["project_ssh_keys"] = project_ssh_keys
        if public_ipv4_subnet_size is not UNSET:
            field_dict["public_ipv4_subnet_size"] = public_ipv4_subnet_size
        if spot_instance is not UNSET:
            field_dict["spot_instance"] = spot_instance
        if spot_price_max is not UNSET:
            field_dict["spot_price_max"] = spot_price_max
        if ssh_keys is not UNSET:
            field_dict["ssh_keys"] = ssh_keys
        if tags is not UNSET:
            field_dict["tags"] = tags
        if termination_time is not UNSET:
            field_dict["termination_time"] = termination_time
        if user_ssh_keys is not UNSET:
            field_dict["user_ssh_keys"] = user_ssh_keys
        if userdata is not UNSET:
            field_dict["userdata"] = userdata

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_create_input_customdata import DeviceCreateInputCustomdata
        from ..models.device_create_input_ip_addresses_inner import DeviceCreateInputIpAddressesInner
        from ..models.ssh_key_input import SSHKeyInput
        d = src_dict.copy()
        operating_system = d.pop("operating_system")

        plan = d.pop("plan")

        always_pxe = d.pop("always_pxe", UNSET)

        _billing_cycle = d.pop("billing_cycle", UNSET)
        billing_cycle: Union[Unset, DeviceCreateInputBillingCycle]
        if isinstance(_billing_cycle,  Unset):
            billing_cycle = UNSET
        else:
            billing_cycle = DeviceCreateInputBillingCycle(_billing_cycle)




        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, DeviceCreateInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = DeviceCreateInputCustomdata.from_dict(_customdata)




        description = d.pop("description", UNSET)

        features = cast(List[str], d.pop("features", UNSET))


        hardware_reservation_id = d.pop("hardware_reservation_id", UNSET)

        hostname = d.pop("hostname", UNSET)

        ip_addresses = []
        _ip_addresses = d.pop("ip_addresses", UNSET)
        for ip_addresses_item_data in (_ip_addresses or []):
            ip_addresses_item = DeviceCreateInputIpAddressesInner.from_dict(ip_addresses_item_data)



            ip_addresses.append(ip_addresses_item)


        ipxe_script_url = d.pop("ipxe_script_url", UNSET)

        locked = d.pop("locked", UNSET)

        no_ssh_keys = d.pop("no_ssh_keys", UNSET)

        private_ipv4_subnet_size = d.pop("private_ipv4_subnet_size", UNSET)

        project_ssh_keys = cast(List[str], d.pop("project_ssh_keys", UNSET))


        public_ipv4_subnet_size = d.pop("public_ipv4_subnet_size", UNSET)

        spot_instance = d.pop("spot_instance", UNSET)

        spot_price_max = d.pop("spot_price_max", UNSET)

        ssh_keys = []
        _ssh_keys = d.pop("ssh_keys", UNSET)
        for ssh_keys_item_data in (_ssh_keys or []):
            ssh_keys_item = SSHKeyInput.from_dict(ssh_keys_item_data)



            ssh_keys.append(ssh_keys_item)


        tags = cast(List[str], d.pop("tags", UNSET))


        _termination_time = d.pop("termination_time", UNSET)
        termination_time: Union[Unset, datetime.datetime]
        if isinstance(_termination_time,  Unset):
            termination_time = UNSET
        else:
            termination_time = isoparse(_termination_time)




        user_ssh_keys = cast(List[str], d.pop("user_ssh_keys", UNSET))


        userdata = d.pop("userdata", UNSET)

        device_create_input = cls(
            operating_system=operating_system,
            plan=plan,
            always_pxe=always_pxe,
            billing_cycle=billing_cycle,
            customdata=customdata,
            description=description,
            features=features,
            hardware_reservation_id=hardware_reservation_id,
            hostname=hostname,
            ip_addresses=ip_addresses,
            ipxe_script_url=ipxe_script_url,
            locked=locked,
            no_ssh_keys=no_ssh_keys,
            private_ipv4_subnet_size=private_ipv4_subnet_size,
            project_ssh_keys=project_ssh_keys,
            public_ipv4_subnet_size=public_ipv4_subnet_size,
            spot_instance=spot_instance,
            spot_price_max=spot_price_max,
            ssh_keys=ssh_keys,
            tags=tags,
            termination_time=termination_time,
            user_ssh_keys=user_ssh_keys,
            userdata=userdata,
        )

        device_create_input.additional_properties = d
        return device_create_input

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
