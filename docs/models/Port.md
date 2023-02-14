# metal.types.port.Port

Port is a hardware port associated with a reserved or instantiated hardware device.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Port is a hardware port associated with a reserved or instantiated hardware device. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bond** | [**BondPortData**](BondPortData.md) | [**BondPortData**](BondPortData.md) |  | [optional] 
**data** | [**PortData**](PortData.md) | [**PortData**](PortData.md) |  | [optional] 
**disbond_operation_supported** | bool,  | BoolClass,  | Indicates whether or not the bond can be broken on the port (when applicable). | [optional] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  | Type is either \&quot;NetworkBondPort\&quot; for bond ports or \&quot;NetworkPort\&quot; for bondable ethernet ports | [optional] must be one of ["NetworkPort", "NetworkBondPort", ] 
**network_type** | str,  | str,  | Composite network type of the bond | [optional] must be one of ["layer2-bonded", "layer2-individual", "layer3", "hybrid", "hybrid-bonded", ] 
**native_virtual_network** | [**VirtualNetwork**](VirtualNetwork.md) | [**VirtualNetwork**](VirtualNetwork.md) |  | [optional] 
**[virtual_networks](#virtual_networks)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# virtual_networks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Href**](Href.md) | [**Href**](Href.md) | [**Href**](Href.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

