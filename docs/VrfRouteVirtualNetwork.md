# VrfRouteVirtualNetwork

A link to the Virtual Network to which this VRF Route is associated, through the Metal Gateway

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**assigned_to** | [**Href**](Href.md) |  | [optional] 
**assigned_to_virtual_circuit** | **bool** | True if the virtual network is attached to a virtual circuit. False if not. | [optional] 
**description** | **str** |  | [optional] 
**facility** | [**Href**](Href.md) |  | [optional] 
**id** | **str** |  | [optional] 
**instances** | [**list[Href]**](Href.md) | A list of instances with ports currently associated to this Virtual Network. | [optional] 
**metal_gateways** | [**list[MetalGatewayLite]**](MetalGatewayLite.md) | A list of metal gateways currently associated to this Virtual Network. | [optional] 
**metro** | [**Href**](Href.md) |  | [optional] 
**metro_code** | **str** | The Metro code of the metro in which this Virtual Network is defined. | [optional] 
**vxlan** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


