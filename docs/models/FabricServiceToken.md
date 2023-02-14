# metal.types.fabric_service_token.FabricServiceToken

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**expires_at** | str, datetime,  | str,  | The expiration date and time of the Fabric service token. Once a service token is expired, it is no longer redeemable. | [optional] value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  | The UUID that can be used on the Fabric Portal to redeem either an A-Side or Z-Side Service Token. For Fabric VCs (Metal Billed), this UUID will represent an A-Side Service Token, which will allow interconnections to be made from Equinix Metal to other Service Providers on Fabric. For Fabric VCs (Fabric Billed), this UUID will represent a Z-Side Service Token, which will allow interconnections to be made to connect an owned Fabric Port or  Virtual Device to Equinix Metal. | [optional] value must be a uuid
**max_allowed_speed** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum speed that can be selected on the Fabric Portal when configuring a interconnection with either  an A-Side or Z-Side Service Token. For Fabric VCs (Metal Billed), this is what the billing is based off of, and can be one of the following options, &#x27;50mbps&#x27;, &#x27;200mbps&#x27;, &#x27;500mbps&#x27;, &#x27;1gbps&#x27;, &#x27;2gbps&#x27;, &#x27;5gbps&#x27; or &#x27;10gbps&#x27;. For Fabric VCs (Fabric Billed), this will default to 10Gbps. | [optional] 
**role** | str,  | str,  | Either primary or secondary, depending on which interconnection the service token is associated to. | [optional] must be one of ["primary", "secondary", ] 
**service_token_type** | str,  | str,  | Either &#x27;a_side&#x27; or &#x27;z_side&#x27;, depending on which type of Fabric VC was requested. | [optional] must be one of ["a_side", "z_side", ] 
**state** | str,  | str,  | The state of the service token that corresponds with the service token state on Fabric. An &#x27;inactive&#x27; state refers to a token that has not been redeemed yet on the Fabric side, an &#x27;active&#x27; state refers to a token that has already been redeemed, and an &#x27;expired&#x27; state refers to a token that has reached its expiry time. | [optional] must be one of ["inactive", "active", "expired", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

