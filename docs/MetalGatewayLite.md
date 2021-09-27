# MetalGatewayLite


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**state** | **str** | The current state of the Metal Gateway. &#39;Ready&#39; indicates the gateway record has been configured, but is currently not active on the network. &#39;Active&#39; indicates the gateway has been configured on the network. &#39;Deleting&#39; is a temporary state used to indicate that the gateway is in the process of being un-configured from the network, after which the gateway record will be deleted. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**gateway_address** | **str** | The gateway address with subnet CIDR value for this Metal Gateway. For example, a Metal Gateway using an IP reservation with block 10.1.2.0/27 would have a gateway address of 10.1.2.1/27. | [optional] 
**vlan** | **float** | The VLAN id of the Virtual Network record associated to this Metal Gateway. Example: 1001. | [optional] 
**href** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


