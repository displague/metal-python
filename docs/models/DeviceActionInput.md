# metal.types.device_action_input.DeviceActionInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Action to perform. See Device.actions for possible actions. | must be one of ["power_on", "power_off", "reboot", "rescue", "reinstall", ] 
**force_delete** | bool,  | BoolClass,  | May be required to perform actions under certain conditions | [optional] 
**deprovision_fast** | bool,  | BoolClass,  | When type is &#x60;reinstall&#x60;, enabling fast deprovisioning will bypass full disk wiping. | [optional] 
**preserve_data** | bool,  | BoolClass,  | When type is &#x60;reinstall&#x60;, preserve the existing data on all disks except the operating-system disk. | [optional] 
**operating_system** | str,  | str,  | When type is &#x60;reinstall&#x60;, use this &#x60;operating_system&#x60; (defaults to the current &#x60;operating system&#x60;) | [optional] 
**ipxe_script_url** | str,  | str,  | When type is &#x60;reinstall&#x60;, use this &#x60;ipxe_script_url&#x60; (&#x60;operating_system&#x60; must be &#x60;custom_ipxe&#x60;, defaults to the current &#x60;ipxe_script_url&#x60;) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

