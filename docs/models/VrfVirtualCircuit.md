# metal.types.vrf_virtual_circuit.VrfVirtualCircuit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**customer_ip** | str,  | str,  | An IP address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used. | [optional] 
**description** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**md5** | str,  | str,  | The MD5 password for the BGP peering in plaintext (not a checksum). | [optional] 
**metal_ip** | str,  | str,  | An IP address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used. | [optional] 
**name** | str,  | str,  |  | [optional] 
**port** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**nni_vlan** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**peer_asn** | decimal.Decimal, int,  | decimal.Decimal,  | The peer ASN that will be used with the VRF on the Virtual Circuit. | [optional] 
**project** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**speed** | decimal.Decimal, int,  | decimal.Decimal,  | integer representing bps speed | [optional] 
**status** | str,  | str,  |  | [optional] 
**subnet** | str,  | str,  | The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP. | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
**vrf** | [**Vrf**](Vrf.md) | [**Vrf**](Vrf.md) |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

