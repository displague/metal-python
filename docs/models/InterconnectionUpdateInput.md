# metal.types.interconnection_update_input.InterconnectionUpdateInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**contact_email** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**mode** | str,  | str,  | The mode of the interconnection (only relevant to Dedicated Ports). Shared connections won&#x27;t have this field. Can be either &#x27;standard&#x27; or &#x27;tunnel&#x27;.   The default mode of an interconnection on a Dedicated Port is &#x27;standard&#x27;. The mode can only be changed when there are no associated virtual circuits on the interconnection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances. | [optional] must be one of ["standard", "tunnel", ] 
**name** | str,  | str,  |  | [optional] 
**redundancy** | str,  | str,  | Updating from &#x27;redundant&#x27; to &#x27;primary&#x27; will remove a secondary port, while updating from &#x27;primary&#x27; to &#x27;redundant&#x27; will add one. | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
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

