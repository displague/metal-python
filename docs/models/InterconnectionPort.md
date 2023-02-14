# metal.types.interconnection_port.InterconnectionPort

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**organization** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**role** | str,  | str,  | Either &#x27;primary&#x27; or &#x27;secondary&#x27;. | [optional] must be one of ["primary", "secondary", ] 
**status** | str,  | str,  | For both Fabric VCs and Dedicated Ports, this will be &#x27;requested&#x27; on creation and &#x27;deleting&#x27; on deletion. Once the Fabric VC has found its corresponding Fabric connection, this will turn to &#x27;active&#x27;. For Dedicated Ports, once the dedicated port is associated, this will also turn to &#x27;active&#x27;. For Fabric VCs, this can turn into an &#x27;expired&#x27; state if the service token associated is expired. | [optional] must be one of ["requested", "active", "deleting", "expired", ] 
**switch_id** | str,  | str,  | A switch &#x27;short ID&#x27; | [optional] 
**virtual_circuits** | [**VirtualCircuitList**](VirtualCircuitList.md) | [**VirtualCircuitList**](VirtualCircuitList.md) |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**speed** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**link_status** | str,  | str,  |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

