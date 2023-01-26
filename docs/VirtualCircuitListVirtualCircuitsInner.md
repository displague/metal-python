# VirtualCircuitListVirtualCircuitsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill** | **bool** | True if the Virtual Circuit is being billed. Currently, only Virtual Circuits of Fabric VCs (Metal Billed) will be billed. Usage will start the first time the Virtual Circuit becomes active, and will not stop until it is deleted from Metal. | [default to False]
**description** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**nni_vlan** | **int** |  | 
**port** | [**Href**](Href.md) |  | 
**project** | [**Href**](Href.md) |  | 
**speed** | **int** | integer representing bps speed | [optional] 
**status** | **str** |  | 
**tags** | **list[str]** |  | 
**virtual_network** | [**Href**](Href.md) |  | 
**vnid** | **int** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**customer_ip** | **str** | An IP address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used. | [optional] 
**md5** | **str** | The MD5 password for the BGP peering in plaintext (not a checksum). | [optional] 
**metal_ip** | **str** | An IP address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used. | [optional] 
**peer_asn** | **int** | The peer ASN that will be used with the VRF on the Virtual Circuit. | [optional] 
**subnet** | **str** | The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP. | [optional] 
**vrf** | [**Vrf**](Vrf.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


