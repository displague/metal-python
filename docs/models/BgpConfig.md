# metal.types.bgp_config.BgpConfig

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**asn** | decimal.Decimal, int,  | decimal.Decimal,  | Autonomous System Number. ASN is required with Global BGP. With Local BGP the private ASN, 65000, is assigned. | [optional] value must be a 32 bit integer
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**deployment_type** | str,  | str,  | In a Local BGP deployment, a customer uses an internal ASN to control routes within a single Equinix Metal datacenter. This means that the routes are never advertised to the global Internet. Global BGP, on the other hand, requires a customer to have a registered ASN and IP space.  | [optional] must be one of ["global", "local", ] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**max_prefix** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of route filters allowed per server | [optional] if omitted the server will use the default value of 10
**md5** | None, str,  | NoneClass, str,  | (Optional) Password for BGP session in plaintext (not a checksum) | [optional] 
**project** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**[ranges](#ranges)** | list, tuple,  | tuple,  | The IP block ranges associated to the ASN (Populated in Global BGP only) | [optional] 
**requested_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**route_object** | str,  | str,  | Specifies AS-MACRO (aka AS-SET) to use when building client route filters | [optional] 
**[sessions](#sessions)** | list, tuple,  | tuple,  | The direct connections between neighboring routers that want to exchange routing information. | [optional] 
**status** | str,  | str,  | Status of the BGP Config. Status \&quot;requested\&quot; is valid only with the \&quot;global\&quot; deployment_type. | [optional] must be one of ["requested", "enabled", "disabled", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ranges

The IP block ranges associated to the ASN (Populated in Global BGP only)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The IP block ranges associated to the ASN (Populated in Global BGP only) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**GlobalBgpRange**](GlobalBgpRange.md) | [**GlobalBgpRange**](GlobalBgpRange.md) | [**GlobalBgpRange**](GlobalBgpRange.md) |  | 

# sessions

The direct connections between neighboring routers that want to exchange routing information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The direct connections between neighboring routers that want to exchange routing information. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BgpSession**](BgpSession.md) | [**BgpSession**](BgpSession.md) | [**BgpSession**](BgpSession.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

