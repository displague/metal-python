# metal.types.facility_input_facility.FacilityInputFacility

The datacenter where the device should be created.  Either metro or facility must be provided.  The API will accept either a single facility `{ \"facility\": \"f1\" }`, or it can be instructed to create the device in the best available datacenter `{ \"facility\": \"any\" }`.  Additionally it is possible to set a prioritized location selection. For example `{ \"facility\": [\"f3\", \"f2\", \"any\"] }` can be used to prioritize `f3` and then `f2` before accepting `any` facility. If none of the facilities provided have availability for the requested device the request will fail.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The datacenter where the device should be created.  Either metro or facility must be provided.  The API will accept either a single facility &#x60;{ \&quot;facility\&quot;: \&quot;f1\&quot; }&#x60;, or it can be instructed to create the device in the best available datacenter &#x60;{ \&quot;facility\&quot;: \&quot;any\&quot; }&#x60;.  Additionally it is possible to set a prioritized location selection. For example &#x60;{ \&quot;facility\&quot;: [\&quot;f3\&quot;, \&quot;f2\&quot;, \&quot;any\&quot;] }&#x60; can be used to prioritize &#x60;f3&#x60; and then &#x60;f2&#x60; before accepting &#x60;any&#x60; facility. If none of the facilities provided have availability for the requested device the request will fail. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | list, tuple,  | tuple,  |  | 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

