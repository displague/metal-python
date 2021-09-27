# VirtualNetwork


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**vxlan** | **int** |  | [optional] 
**facility** | [**Href**](Href.md) |  | [optional] 
**instances** | [**list[Href]**](Href.md) | A list of instances with ports currently associated to this Virtual Network. | [optional] 
**metro_code** | **str** | The Metro code of the metro in which this Virtual Network is defined. | [optional] 
**metro** | [**Href**](Href.md) |  | [optional] 
**assigned_to_virtual_circuit** | **bool** | True if the virtual network is attached to a virtual circuit. False if not. | [optional] 
**assigned_to** | [**Href**](Href.md) |  | [optional] 
**href** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


