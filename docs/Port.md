# Port

Port is a hardware port associated with a reserved or instantiated hardware device.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bond** | [**BondPortData**](BondPortData.md) |  | [optional] 
**data** | [**PortData**](PortData.md) |  | [optional] 
**disbond_operation_supported** | **bool** | Indicates whether or not the bond can be broken on the port (when applicable). | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** | Type is either \&quot;NetworkBondPort\&quot; for bond ports or \&quot;NetworkPort\&quot; for bondable ethernet ports | [optional] 
**network_type** | **str** | Composite network type of the bond | [optional] 
**native_virtual_network** | [**VirtualNetwork**](VirtualNetwork.md) |  | [optional] 
**virtual_networks** | [**list[Href]**](Href.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


