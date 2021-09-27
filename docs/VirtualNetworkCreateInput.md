# VirtualNetworkCreateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**description** | **str** |  | [optional] 
**facility** | **str** | The UUID (or facility code) for the Facility in which to create this Virtual network. | [optional] 
**metro** | **str** | The UUID (or metro code) for the Metro in which to create this Virtual Network. | [optional] 
**vxlan** | **int** | VLAN ID between 2-3999. Must be unique for the project within the Metro in which this Virtual Network is being created. If no value is specified, the next-available VLAN ID in the range 1000-1999 will be automatically selected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


