# metal.types.interconnection.Interconnection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**contact_email** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**facility** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**metro** | [**InterconnectionMetro**](InterconnectionMetro.md) | [**InterconnectionMetro**](InterconnectionMetro.md) |  | [optional] 
**mode** | str,  | str,  | The mode of the interconnection (only relevant to Dedicated Ports). Shared connections won&#x27;t have this field. Can be either &#x27;standard&#x27; or &#x27;tunnel&#x27;.   The default mode of an interconnection on a Dedicated Port is &#x27;standard&#x27;. The mode can only be changed when there are no associated virtual circuits on the interconnection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances. | [optional] must be one of ["standard", "tunnel", ] 
**name** | str,  | str,  |  | [optional] 
**organization** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**[ports](#ports)** | list, tuple,  | tuple,  | For Fabric VCs, these represent Virtual Port(s) created for the interconnection. For dedicated interconnections, these represent the Dedicated Port(s). | [optional] 
**redundancy** | str,  | str,  | Either &#x27;primary&#x27;, meaning a single interconnection, or &#x27;redundant&#x27;, meaning a redundant interconnection. | [optional] must be one of ["primary", "redundant", ] 
**[service_tokens](#service_tokens)** | list, tuple,  | tuple,  | For Fabric VCs (Metal Billed), this will show details of the A-Side service tokens issued for the interconnection. For Fabric VCs (Fabric Billed), this will show the details of the Z-Side service tokens issued for the interconnection. Dedicated interconnections will not have any service tokens issued. There will be one per interconnection, so for redundant interconnections, there should be two service tokens issued. | [optional] 
**speed** | decimal.Decimal, int,  | decimal.Decimal,  | For interconnections on Dedicated Ports and shared connections, this represents the interconnection&#x27;s speed in bps. For Fabric VCs, this field refers to the maximum speed of the interconnection in bps. This value will default to 10Gbps for Fabric VCs (Fabric Billed). | [optional] 
**status** | str,  | str,  |  | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
**token** | str, uuid.UUID,  | str,  | This token is used for shared interconnections to be used as the Fabric Token. This field is entirely deprecated. | [optional] value must be a uuid
**type** | str,  | str,  | The &#x27;shared&#x27; type of interconnection refers to shared connections, or later also known as Fabric Virtual Connections (or Fabric VCs). The &#x27;dedicated&#x27; type of interconnection refers to interconnections created with Dedicated Ports. | [optional] must be one of ["shared", "dedicated", ] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**requested_by** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ports

For Fabric VCs, these represent Virtual Port(s) created for the interconnection. For dedicated interconnections, these represent the Dedicated Port(s).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | For Fabric VCs, these represent Virtual Port(s) created for the interconnection. For dedicated interconnections, these represent the Dedicated Port(s). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InterconnectionPort**](InterconnectionPort.md) | [**InterconnectionPort**](InterconnectionPort.md) | [**InterconnectionPort**](InterconnectionPort.md) |  | 

# service_tokens

For Fabric VCs (Metal Billed), this will show details of the A-Side service tokens issued for the interconnection. For Fabric VCs (Fabric Billed), this will show the details of the Z-Side service tokens issued for the interconnection. Dedicated interconnections will not have any service tokens issued. There will be one per interconnection, so for redundant interconnections, there should be two service tokens issued.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | For Fabric VCs (Metal Billed), this will show details of the A-Side service tokens issued for the interconnection. For Fabric VCs (Fabric Billed), this will show the details of the Z-Side service tokens issued for the interconnection. Dedicated interconnections will not have any service tokens issued. There will be one per interconnection, so for redundant interconnections, there should be two service tokens issued. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FabricServiceToken**](FabricServiceToken.md) | [**FabricServiceToken**](FabricServiceToken.md) | [**FabricServiceToken**](FabricServiceToken.md) |  | 

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

