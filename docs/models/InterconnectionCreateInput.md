# metal.types.interconnection_create_input.InterconnectionCreateInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metro** | str,  | str,  | A Metro ID or code. For interconnections with Dedicated Ports, this will be the location of the issued Dedicated Ports. When creating Fabric VCs (Metal Billed), this is where interconnection will be originating from, as we pre-authorize the use of one of our shared ports as the origin of the interconnection using A-Side service tokens. We only allow local connections for Fabric VCs (Metal Billed), so the destination location must be the same as the origin. For Fabric VCs (Fabric Billed), or shared connections, this will be the destination of the interconnection. We allow remote connections for Fabric VCs (Fabric Billed), so the origin of the interconnection can be a different metro set here. | 
**name** | str,  | str,  |  | 
**redundancy** | str,  | str,  | Either &#x27;primary&#x27; or &#x27;redundant&#x27;. | 
**type** | str,  | str,  | Either &#x27;shared&#x27; or &#x27;dedicated&#x27;. The &#x27;shared&#x27; type represents shared interconnections, or also known as Fabric VCs. The &#x27;dedicated&#x27; type represents dedicated interconnections, or also known as Dedicated Ports. | 
**contact_email** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**mode** | str,  | str,  | The mode of the interconnection (only relevant to Dedicated Ports). Fabric VCs won&#x27;t have this field. Can be either &#x27;standard&#x27; or &#x27;tunnel&#x27;.   The default mode of an interconnection on a Dedicated Port is &#x27;standard&#x27;. The mode can only be changed when there are no associated virtual circuits on the interconnection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances. | [optional] must be one of ["standard", "tunnel", ] 
**project** | str,  | str,  |  | [optional] 
**service_token_type** | str,  | str,  | Either &#x27;a_side&#x27; or &#x27;z_side&#x27;. Setting this field to &#x27;a_side&#x27; will create an interconnection with Fabric VCs (Metal Billed). Setting this field to &#x27;z_side&#x27; will create an interconnection with Fabric VCs (Fabric Billed). This is required when the &#x27;type&#x27; is &#x27;shared&#x27;, but this is not applicable when the &#x27;type&#x27; is &#x27;dedicated&#x27;. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details. | [optional] must be one of ["a_side", "z_side", ] 
**speed** | decimal.Decimal, int,  | decimal.Decimal,  | A interconnection speed, in bps, mbps, or gbps. For Dedicated Ports, this can be 10Gbps or 100Gbps. For Fabric VCs, this represents the maximum speed of the interconnection. For Fabric VCs (Metal Billed), this can only be one of the following:  &#x27;&#x27;50mbps&#x27;&#x27;, &#x27;&#x27;200mbps&#x27;&#x27;, &#x27;&#x27;500mbps&#x27;&#x27;, &#x27;&#x27;1gbps&#x27;&#x27;, &#x27;&#x27;2gbps&#x27;&#x27;, &#x27;&#x27;5gbps&#x27;&#x27; or &#x27;&#x27;10gbps&#x27;&#x27;, and is required for creation. For Fabric VCs (Fabric Billed), this field will always default to &#x27;&#x27;10gbps&#x27;&#x27; even if it is not provided. For example, &#x27;&#x27;500000000&#x27;&#x27;, &#x27;&#x27;50m&#x27;&#x27;, or&#x27; &#x27;&#x27;500mbps&#x27;&#x27; will all work as valid inputs. | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
**[vlans](#vlans)** | list, tuple,  | tuple,  | A list of one or two metro-based VLANs that will be set on the virtual circuits of primary and/or secondary (if redundant) interconnections respectively when creating Fabric VCs. VLANs can also be set after the interconnection is created, but are required to fully activate the interconnection. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details. | [optional] 
**[vrfs](#vrfs)** | list, tuple,  | tuple,  | Can only be set when creating Fabric VCs in VRF(s). This field holds a list of VRF UUIDs that will be set automatically on the virtual circuits on creation, and can hold up to two UUIDs. Two UUIDs are required when requesting redundant Fabric VCs. The first UUID will be set on the primary virtual circuit, while the second UUID will be set on the secondary. The two UUIDs can be the same if both the primary and secondary virtual circuits will be in the same VRF. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details. | [optional] 
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

# vlans

A list of one or two metro-based VLANs that will be set on the virtual circuits of primary and/or secondary (if redundant) interconnections respectively when creating Fabric VCs. VLANs can also be set after the interconnection is created, but are required to fully activate the interconnection. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of one or two metro-based VLANs that will be set on the virtual circuits of primary and/or secondary (if redundant) interconnections respectively when creating Fabric VCs. VLANs can also be set after the interconnection is created, but are required to fully activate the interconnection. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# vrfs

Can only be set when creating Fabric VCs in VRF(s). This field holds a list of VRF UUIDs that will be set automatically on the virtual circuits on creation, and can hold up to two UUIDs. Two UUIDs are required when requesting redundant Fabric VCs. The first UUID will be set on the primary virtual circuit, while the second UUID will be set on the secondary. The two UUIDs can be the same if both the primary and secondary virtual circuits will be in the same VRF. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Can only be set when creating Fabric VCs in VRF(s). This field holds a list of VRF UUIDs that will be set automatically on the virtual circuits on creation, and can hold up to two UUIDs. Two UUIDs are required when requesting redundant Fabric VCs. The first UUID will be set on the primary virtual circuit, while the second UUID will be set on the secondary. The two UUIDs can be the same if both the primary and secondary virtual circuits will be in the same VRF. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

