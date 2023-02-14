# metal.types.virtual_circuit.VirtualCircuit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**virtual_network** | [**Href**](Href.md) | [**Href**](Href.md) |  | 
**nni_vlan** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**vnid** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**port** | [**Href**](Href.md) | [**Href**](Href.md) |  | 
**name** | str,  | str,  |  | 
**bill** | bool,  | BoolClass,  | True if the Virtual Circuit is being billed. Currently, only Virtual Circuits of Fabric VCs (Metal Billed) will be billed. Usage will start the first time the Virtual Circuit becomes active, and will not stop until it is deleted from Metal. | if omitted the server will use the default value of False
**description** | str,  | str,  |  | 
**project** | [**Href**](Href.md) | [**Href**](Href.md) |  | 
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**status** | str,  | str,  | The status of a Virtual Circuit is always &#x27;Pending&#x27; on creation. The status can turn to &#x27;Waiting on Customer VLAN&#x27; if a Metro VLAN was not set yet on the Virtual Circuit and is the last step needed for full activation. For Dedicated interconnections, as long as the Dedicated Port has been associated to the Virtual Circuit and a NNI VNID has been set, it will turn to &#x27;Waiting on Customer VLAN&#x27;. For Fabric VCs, it will only change to &#x27;Waiting on Customer VLAN&#x27; once the corresponding Fabric connection has been found on the Fabric side. Once a Metro VLAN is set on the Virtual Circuit (which for Fabric VCs, can be set on creation) and the necessary set up is done, it will turn into &#x27;Activating&#x27; status as it tries to activate the Virtual Circuit. Once the Virtual Circuit fully activates and is configured on the switch, it will turn to staus &#x27;Active&#x27;. For Fabric VCs (Metal Billed), we will start billing the moment the status of the Virtual Circuit turns to &#x27;Active&#x27;. If there are any changes to the VLAN after the Virtual Circuit is in an &#x27;Active&#x27; status, the status will show &#x27;Changing VLAN&#x27; if a new VLAN has been provided, or &#x27;Deactivating&#x27; if we are removing the VLAN. When a deletion request is issued for the Virtual Circuit, it will move to a &#x27;deleting&#x27; status until it is fully deleted. If the Virtual Circuit is on a Fabric VC, it can also change into an &#x27;Expired&#x27; status if the associated service token has expired. | must be one of ["pending", "waiting_on_customer_vlan", "activating", "changing_vlan", "deactivating", "deleting", "active", "expired", "activation_failed", "changing_vlan_failed", "deactivation_failed", "delete_failed", ] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | 
**speed** | decimal.Decimal, int,  | decimal.Decimal,  | For Virtual Circuits on shared and dedicated connections, this speed should match the one set on their Interconnection Ports. For Virtual Circuits on Fabric VCs (both Metal and Fabric Billed) that have found their corresponding Fabric connection, this is the actual speed of the interconnection that was configured when setting up the interconnection on the Fabric Portal. Details on Fabric VCs are included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details. | [optional] 
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

