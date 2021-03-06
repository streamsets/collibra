# collibra_core.AttributesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_attribute**](AttributesApi.md#add_attribute) | **POST** /attributes | Add attribute
[**add_attributes**](AttributesApi.md#add_attributes) | **POST** /attributes/bulk | Add attributes
[**change_attribute**](AttributesApi.md#change_attribute) | **PATCH** /attributes/{attributeId} | Change attribute
[**change_attributes**](AttributesApi.md#change_attributes) | **PATCH** /attributes/bulk | Change attributes
[**find_attributes**](AttributesApi.md#find_attributes) | **GET** /attributes | Find attributes
[**get_attribute**](AttributesApi.md#get_attribute) | **GET** /attributes/{attributeId} | Get attribute
[**remove_attribute**](AttributesApi.md#remove_attribute) | **DELETE** /attributes/{attributeId} | Remove attribute
[**remove_attributes**](AttributesApi.md#remove_attributes) | **DELETE** /attributes/bulk | Remove attributes


# **add_attribute**
> Attribute add_attribute()

Add attribute

Adds a new attribute to an asset.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attributes_api
from collibra_core.model.add_attribute_request import AddAttributeRequest
from collibra_core.model.attribute import Attribute
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)
    add_attribute_request = AddAttributeRequest(
        asset_id="asset_id_example",
        type_id="type_id_example",
        value={},
    ) # AddAttributeRequest | the properties of the attribute to be added (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add attribute
        api_response = api_instance.add_attribute(add_attribute_request=add_attribute_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributesApi->add_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_attribute_request** | [**AddAttributeRequest**](AddAttributeRequest.md)| the properties of the attribute to be added | [optional]

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attribute successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_attributes**
> [Attribute] add_attributes()

Add attributes

Adds multiple attributes.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attributes_api
from collibra_core.model.add_attribute_request import AddAttributeRequest
from collibra_core.model.attribute import Attribute
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)
    add_attribute_request = [
        AddAttributeRequest(
            asset_id="asset_id_example",
            type_id="type_id_example",
            value={},
        ),
    ] # [AddAttributeRequest] | the list of the properties of the attributes to be added (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add attributes
        api_response = api_instance.add_attributes(add_attribute_request=add_attribute_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributesApi->add_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_attribute_request** | [**[AddAttributeRequest]**](AddAttributeRequest.md)| the list of the properties of the attributes to be added | [optional]

### Return type

[**[Attribute]**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attributes successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_attribute**
> Attribute change_attribute(attribute_id)

Change attribute

Changes the attribute with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attributes_api
from collibra_core.model.attribute import Attribute
from collibra_core.model.change_attribute_request import ChangeAttributeRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)
    attribute_id = "attributeId_example" # str | the id of the attribute
    change_attribute_request = ChangeAttributeRequest(
        id="id_example",
        value={},
    ) # ChangeAttributeRequest | the properties of the attribute to be changed (optional)

    # example passing only required values which don't have defaults set
    try:
        # Change attribute
        api_response = api_instance.change_attribute(attribute_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributesApi->change_attribute: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change attribute
        api_response = api_instance.change_attribute(attribute_id, change_attribute_request=change_attribute_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributesApi->change_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**| the id of the attribute |
 **change_attribute_request** | [**ChangeAttributeRequest**](ChangeAttributeRequest.md)| the properties of the attribute to be changed | [optional]

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The changed attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_attributes**
> Attribute change_attributes()

Change attributes

Changes multiple attributes with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attributes_api
from collibra_core.model.attribute import Attribute
from collibra_core.model.change_attribute_request import ChangeAttributeRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)
    change_attribute_request = [
        ChangeAttributeRequest(
            id="id_example",
            value={},
        ),
    ] # [ChangeAttributeRequest] | the list of properties of the attributes to be changed (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change attributes
        api_response = api_instance.change_attributes(change_attribute_request=change_attribute_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributesApi->change_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_attribute_request** | [**[ChangeAttributeRequest]**](ChangeAttributeRequest.md)| the list of properties of the attributes to be changed | [optional]

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The changed attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_attributes**
> AttributePagedResponse find_attributes()

Find attributes

Returns attributes matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned attributes satisfy all constraints that are specified in this search criteria. By default a result containing 1000 attributes is returned.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attributes_api
from collibra_core.model.attribute_paged_response import AttributePagedResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) if omitted the server will use the default value of 0
    limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) if omitted the server will use the default value of 0
    type_ids = [
        "typeIds_example",
    ] # [str] | The list of IDs of the attribute types the found attributes should have. (optional)
    asset_id = "assetId_example" # str | The ID of the asset to find the attributes in. (optional)
    sort_order = "DESC" # str | The sorting order. (optional) if omitted the server will use the default value of "DESC"
    sort_field = "LAST_MODIFIED" # str | The field on which the results are sorted. (optional) if omitted the server will use the default value of "LAST_MODIFIED"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find attributes
        api_response = api_instance.find_attributes(offset=offset, limit=limit, type_ids=type_ids, asset_id=asset_id, sort_order=sort_order, sort_field=sort_field)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributesApi->find_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] if omitted the server will use the default value of 0
 **type_ids** | **[str]**| The list of IDs of the attribute types the found attributes should have. | [optional]
 **asset_id** | **str**| The ID of the asset to find the attributes in. | [optional]
 **sort_order** | **str**| The sorting order. | [optional] if omitted the server will use the default value of "DESC"
 **sort_field** | **str**| The field on which the results are sorted. | [optional] if omitted the server will use the default value of "LAST_MODIFIED"

### Return type

[**AttributePagedResponse**](AttributePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute**
> Attribute get_attribute(attribute_id)

Get attribute

Returns the attribute identified by given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attributes_api
from collibra_core.model.attribute import Attribute
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)
    attribute_id = "attributeId_example" # str | the id of the attribute

    # example passing only required values which don't have defaults set
    try:
        # Get attribute
        api_response = api_instance.get_attribute(attribute_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributesApi->get_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**| the id of the attribute |

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_attribute**
> remove_attribute(attribute_id)

Remove attribute

Removes the attribute identified by given id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attributes_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)
    attribute_id = "attributeId_example" # str | the id of the attribute

    # example passing only required values which don't have defaults set
    try:
        # Remove attribute
        api_instance.remove_attribute(attribute_id)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributesApi->remove_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**| the id of the attribute |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The attribute has been successfully removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_attributes**
> remove_attributes()

Remove attributes

Removes the attributes identified by given ids.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import attributes_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)
    request_body = [
        "request_body_example",
    ] # [str] | the ids of the attributes to remove (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove attributes
        api_instance.remove_attributes(request_body=request_body)
    except collibra_core.ApiException as e:
        print("Exception when calling AttributesApi->remove_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[str]**| the ids of the attributes to remove | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The attribute has been successfully removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

