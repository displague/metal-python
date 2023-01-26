# DeviceActionInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Action to perform. See Device.actions for possible actions. | 
**force_delete** | **bool** | May be required to perform actions under certain conditions | [optional] 
**deprovision_fast** | **bool** | When type is &#x60;reinstall&#x60;, enabling fast deprovisioning will bypass full disk wiping. | [optional] 
**preserve_data** | **bool** | When type is &#x60;reinstall&#x60;, preserve the existing data on all disks except the operating-system disk. | [optional] 
**operating_system** | **str** | When type is &#x60;reinstall&#x60;, use this &#x60;operating_system&#x60; (defaults to the current &#x60;operating system&#x60;) | [optional] 
**ipxe_script_url** | **str** | When type is &#x60;reinstall&#x60;, use this &#x60;ipxe_script_url&#x60; (&#x60;operating_system&#x60; must be &#x60;custom_ipxe&#x60;, defaults to the current &#x60;ipxe_script_url&#x60;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


