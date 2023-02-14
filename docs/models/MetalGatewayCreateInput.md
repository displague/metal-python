# metal.types.metal_gateway_create_input.MetalGatewayCreateInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**virtual_network_id** | str, uuid.UUID,  | str,  | The UUID of a metro virtual network that belongs to the same project as where the metal gateway will be created in. | value must be a uuid
**ip_reservation_id** | str, uuid.UUID,  | str,  | The UUID of an IP reservation that belongs to the same project as where the metal gateway will be created in. This field is required unless the private IPv4 subnet size is specified. | [optional] value must be a uuid
**private_ipv4_subnet_size** | decimal.Decimal, int,  | decimal.Decimal,  | The subnet size (8, 16, 32, 64, or 128) of the private IPv4 reservation that will be created for the metal gateway. This field is required unless a project IP reservation was specified.           Please keep in mind that the number of private metal gateway ranges are limited per project. If you would like to increase the limit per project, please contact support for assistance. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

