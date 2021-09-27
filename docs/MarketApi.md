# metal.MarketApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_metro_spot_market_prices**](MarketApi.md#find_metro_spot_market_prices) | **GET** /market/spot/prices/metros | Get current spot market prices for metros
[**find_spot_market_prices**](MarketApi.md#find_spot_market_prices) | **GET** /market/spot/prices | Get current spot market prices
[**find_spot_market_prices_history**](MarketApi.md#find_spot_market_prices_history) | **GET** /market/spot/prices/history | Get spot market prices for a given period of time


# **find_metro_spot_market_prices**
> SpotMarketPricesPerMetroList find_metro_spot_market_prices(metro=metro, plan=plan)

Get current spot market prices for metros

Get Equinix Metal current spot market prices for all metros.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.MarketApi(api_client)
    metro = 'metro_example' # str | Metro to filter spot market prices (optional)
plan = 'plan_example' # str | Plan to filter spot market prices (optional)

    try:
        # Get current spot market prices for metros
        api_response = api_instance.find_metro_spot_market_prices(metro=metro, plan=plan)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketApi->find_metro_spot_market_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metro** | **str**| Metro to filter spot market prices | [optional] 
 **plan** | **str**| Plan to filter spot market prices | [optional] 

### Return type

[**SpotMarketPricesPerMetroList**](SpotMarketPricesPerMetroList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_spot_market_prices**
> SpotMarketPricesList find_spot_market_prices(facility=facility, plan=plan)

Get current spot market prices

Get Equinix Metal current spot market prices.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.MarketApi(api_client)
    facility = 'facility_example' # str | Facility to check spot market prices (optional)
plan = 'plan_example' # str | Plan to check spot market prices (optional)

    try:
        # Get current spot market prices
        api_response = api_instance.find_spot_market_prices(facility=facility, plan=plan)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketApi->find_spot_market_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility** | **str**| Facility to check spot market prices | [optional] 
 **plan** | **str**| Plan to check spot market prices | [optional] 

### Return type

[**SpotMarketPricesList**](SpotMarketPricesList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_spot_market_prices_history**
> SpotPricesHistoryReport find_spot_market_prices_history(facility, plan, _from, until, metro=metro)

Get spot market prices for a given period of time

Get spot market prices for a given plan and facility in a fixed period of time  *Note: In the `200` response, the property `datapoints` contains arrays of `[float, integer]`.*

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.MarketApi(api_client)
    facility = 'facility_example' # str | Facility to check spot market prices
plan = 'plan_example' # str | Plan to check spot market prices
_from = '_from_example' # str | Timestamp from range
until = 'until_example' # str | Timestamp to range
metro = 'metro_example' # str | Metro to check spot market price history (optional)

    try:
        # Get spot market prices for a given period of time
        api_response = api_instance.find_spot_market_prices_history(facility, plan, _from, until, metro=metro)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketApi->find_spot_market_prices_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility** | **str**| Facility to check spot market prices | 
 **plan** | **str**| Plan to check spot market prices | 
 **_from** | **str**| Timestamp from range | 
 **until** | **str**| Timestamp to range | 
 **metro** | **str**| Metro to check spot market price history | [optional] 

### Return type

[**SpotPricesHistoryReport**](SpotPricesHistoryReport.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

