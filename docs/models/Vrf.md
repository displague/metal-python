# metal.types.vrf.Vrf

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  | Optional field that can be set to describe the VRF | [optional] 
**local_asn** | decimal.Decimal, int,  | decimal.Decimal,  | A 4-byte ASN associated with the VRF. | [optional] value must be a 32 bit integer
**[ip_ranges](#ip_ranges)** | list, tuple,  | tuple,  | A list of CIDR network addresses. Like [\&quot;10.0.0.0/16\&quot;, \&quot;2001:d78::/56\&quot;]. | [optional] 
**project** | [**Project**](Project.md) | [**Project**](Project.md) |  | [optional] 
**metro** | [**Metro**](Metro.md) | [**Metro**](Metro.md) |  | [optional] 
**created_by** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ip_ranges

A list of CIDR network addresses. Like [\"10.0.0.0/16\", \"2001:d78::/56\"].

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of CIDR network addresses. Like [\&quot;10.0.0.0/16\&quot;, \&quot;2001:d78::/56\&quot;]. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

