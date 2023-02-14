# metal.types.device.Device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**always_pxe** | bool,  | BoolClass,  |  | [optional] 
**billing_cycle** | str,  | str,  |  | [optional] 
**bonding_mode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**created_by** | [**DeviceCreatedBy**](DeviceCreatedBy.md) | [**DeviceCreatedBy**](DeviceCreatedBy.md) |  | [optional] 
**[customdata](#customdata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] if omitted the server will use the default value of {}
**description** | str,  | str,  |  | [optional] 
**facility** | [**Facility**](Facility.md) | [**Facility**](Facility.md) |  | [optional] 
**hardware_reservation** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**hostname** | str,  | str,  |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**image_url** | str,  | str,  |  | [optional] 
**[ip_addresses](#ip_addresses)** | list, tuple,  | tuple,  |  | [optional] 
**ipxe_script_url** | str,  | str,  |  | [optional] 
**iqn** | str,  | str,  |  | [optional] 
**locked** | bool,  | BoolClass,  |  | [optional] 
**metro** | [**DeviceMetro**](DeviceMetro.md) | [**DeviceMetro**](DeviceMetro.md) |  | [optional] 
**[network_ports](#network_ports)** | list, tuple,  | tuple,  | By default, servers at Equinix Metal are configured in a “bonded” mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans may have a different number of ports and bonds available. | [optional] 
**operating_system** | [**OperatingSystem**](OperatingSystem.md) | [**OperatingSystem**](OperatingSystem.md) |  | [optional] 
**[actions](#actions)** | list, tuple,  | tuple,  | Actions supported by the device instance. | [optional] 
**plan** | [**Plan**](Plan.md) | [**Plan**](Plan.md) |  | [optional] 
**project** | [**DeviceProject**](DeviceProject.md) | [**DeviceProject**](DeviceProject.md) |  | [optional] 
**project_lite** | [**DeviceProjectLite**](DeviceProjectLite.md) | [**DeviceProjectLite**](DeviceProjectLite.md) |  | [optional] 
**[provisioning_events](#provisioning_events)** | list, tuple,  | tuple,  |  | [optional] 
**provisioning_percentage** | decimal.Decimal, int, float,  | decimal.Decimal,  | Only visible while device provisioning | [optional] value must be a 32 bit float
**root_password** | str,  | str,  | Root password is automatically generated when server is provisioned and it is removed after 24 hours | [optional] 
**short_id** | str,  | str,  |  | [optional] 
**spot_instance** | bool,  | BoolClass,  | Whether or not the device is a spot instance. | [optional] 
**spot_price_max** | decimal.Decimal, int, float,  | decimal.Decimal,  | The maximum price per hour you are willing to pay to keep this spot instance.  If you are outbid, the termination will be set allowing two minutes before shutdown. | [optional] value must be a 32 bit float
**[ssh_keys](#ssh_keys)** | list, tuple,  | tuple,  |  | [optional] 
**state** | str,  | str,  |  | [optional] must be one of ["active", "deleted", "deprovisioning", "failed", "inactive", "queued", "reinstalling", "post_provisioning", "powering_on", "powering_off", "provisioning", ] 
**switch_uuid** | str,  | str,  | Switch short id. This can be used to determine if two devices are connected to the same switch, for example. | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
**termination_time** | str, datetime,  | str,  | When the device will be terminated. This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid. | [optional] value must conform to RFC-3339 date-time
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**user** | str,  | str,  |  | [optional] 
**userdata** | str,  | str,  |  | [optional] 
**[volumes](#volumes)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# customdata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | if omitted the server will use the default value of {}

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ip_addresses

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IPAssignment**](IPAssignment.md) | [**IPAssignment**](IPAssignment.md) | [**IPAssignment**](IPAssignment.md) |  | 

# network_ports

By default, servers at Equinix Metal are configured in a “bonded” mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans may have a different number of ports and bonds available.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | By default, servers at Equinix Metal are configured in a “bonded” mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans may have a different number of ports and bonds available. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Port**](Port.md) | [**Port**](Port.md) | [**Port**](Port.md) |  | 

# actions

Actions supported by the device instance.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Actions supported by the device instance. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DeviceActionsInner**](DeviceActionsInner.md) | [**DeviceActionsInner**](DeviceActionsInner.md) | [**DeviceActionsInner**](DeviceActionsInner.md) |  | 

# provisioning_events

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Event**](Event.md) | [**Event**](Event.md) | [**Event**](Event.md) |  | 

# ssh_keys

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Href**](Href.md) | [**Href**](Href.md) | [**Href**](Href.md) |  | 

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# volumes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Href**](Href.md) | [**Href**](Href.md) | [**Href**](Href.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

