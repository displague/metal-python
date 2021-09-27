# Device


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**short_id** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**image_url** | **str** |  | [optional] 
**billing_cycle** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**iqn** | **str** |  | [optional] 
**locked** | **bool** |  | [optional] 
**bonding_mode** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**spot_instance** | **bool** | Whether or not the device is a spot instance. | [optional] 
**spot_price_max** | **float** | The maximum price per hour you are willing to pay to keep this spot instance.  If you are outbid, the termination will be set allowing two minutes before shutdown. | [optional] 
**termination_time** | **datetime** | When the device will be terminated. This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid. | [optional] 
**customdata** | **object** |  | [optional] 
**provisioning_percentage** | **float** | Only visible while device provisioning | [optional] 
**operating_system** | [**OperatingSystem**](OperatingSystem.md) |  | [optional] 
**always_pxe** | **bool** |  | [optional] 
**ipxe_script_url** | **str** |  | [optional] 
**facility** | [**Facility**](Facility.md) |  | [optional] 
**metro** | [**Metro**](Metro.md) |  | [optional] 
**plan** | [**Plan**](Plan.md) |  | [optional] 
**userdata** | **str** |  | [optional] 
**root_password** | **str** | Root password is automatically generated when server is provisioned and it is removed after 24 hours | [optional] 
**switch_uuid** | **str** | Switch short id. This can be used to determine if two devices are connected to the same switch, for example. | [optional] 
**network_ports** | [**Port**](Port.md) |  | [optional] 
**href** | **str** |  | [optional] 
**project** | [**Href**](Href.md) |  | [optional] 
**project_lite** | [**Href**](Href.md) |  | [optional] 
**volumes** | [**list[Href]**](Href.md) |  | [optional] 
**hardware_reservation** | [**Href**](Href.md) |  | [optional] 
**ssh_keys** | [**list[Href]**](Href.md) |  | [optional] 
**ip_addresses** | [**list[IPAssignment]**](IPAssignment.md) |  | [optional] 
**provisioning_events** | [**list[Event]**](Event.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


