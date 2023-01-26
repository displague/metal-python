# Device


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_pxe** | **bool** |  | [optional] 
**billing_cycle** | **str** |  | [optional] 
**bonding_mode** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | [**DeviceCreatedBy**](DeviceCreatedBy.md) |  | [optional] 
**customdata** | **dict[str, object]** |  | [optional] 
**description** | **str** |  | [optional] 
**facility** | [**Facility**](Facility.md) |  | [optional] 
**hardware_reservation** | [**Href**](Href.md) |  | [optional] 
**hostname** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**ip_addresses** | [**list[IPAssignment]**](IPAssignment.md) |  | [optional] 
**ipxe_script_url** | **str** |  | [optional] 
**iqn** | **str** |  | [optional] 
**locked** | **bool** |  | [optional] 
**metro** | [**DeviceMetro**](DeviceMetro.md) |  | [optional] 
**network_ports** | [**list[Port]**](Port.md) | By default, servers at Equinix Metal are configured in a “bonded” mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans may have a different number of ports and bonds available. | [optional] 
**operating_system** | [**OperatingSystem**](OperatingSystem.md) |  | [optional] 
**actions** | [**list[DeviceActionsInner]**](DeviceActionsInner.md) | Actions supported by the device instance. | [optional] 
**plan** | [**Plan**](Plan.md) |  | [optional] 
**project** | [**DeviceProject**](DeviceProject.md) |  | [optional] 
**project_lite** | [**DeviceProjectLite**](DeviceProjectLite.md) |  | [optional] 
**provisioning_events** | [**list[Event]**](Event.md) |  | [optional] 
**provisioning_percentage** | **float** | Only visible while device provisioning | [optional] 
**root_password** | **str** | Root password is automatically generated when server is provisioned and it is removed after 24 hours | [optional] 
**short_id** | **str** |  | [optional] 
**spot_instance** | **bool** | Whether or not the device is a spot instance. | [optional] 
**spot_price_max** | **float** | The maximum price per hour you are willing to pay to keep this spot instance.  If you are outbid, the termination will be set allowing two minutes before shutdown. | [optional] 
**ssh_keys** | [**list[Href]**](Href.md) |  | [optional] 
**state** | **str** |  | [optional] 
**switch_uuid** | **str** | Switch short id. This can be used to determine if two devices are connected to the same switch, for example. | [optional] 
**tags** | **list[str]** |  | [optional] 
**termination_time** | **datetime** | When the device will be terminated. This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid. | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | **str** |  | [optional] 
**userdata** | **str** |  | [optional] 
**volumes** | [**list[Href]**](Href.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


