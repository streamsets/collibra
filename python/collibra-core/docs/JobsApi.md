# collibra_core.JobsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](JobsApi.md#cancel_job) | **POST** /jobs/{jobId}/canceled | Cancels given Job.
[**get_job**](JobsApi.md#get_job) | **GET** /jobs/{jobId} | Returns the Job identified by the given UUID.


# **cancel_job**
> cancel_job(job_id)

Cancels given Job.

Calling this endpoint will return immediately and not wait until the Job is actually stopped.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import jobs_api
from collibra_core.model.cancel_job_request import CancelJobRequest
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
    api_instance = jobs_api.JobsApi(api_client)
    job_id = "jobId_example" # str | The unique identifier of the Job.
    cancel_job_request = CancelJobRequest(
        message="message_example",
    ) # CancelJobRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cancels given Job.
        api_instance.cancel_job(job_id)
    except collibra_core.ApiException as e:
        print("Exception when calling JobsApi->cancel_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancels given Job.
        api_instance.cancel_job(job_id, cancel_job_request=cancel_job_request)
    except collibra_core.ApiException as e:
        print("Exception when calling JobsApi->cancel_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The unique identifier of the Job. |
 **cancel_job_request** | [**CancelJobRequest**](CancelJobRequest.md)|  | [optional]

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
**202** | Job cancellation accepted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> Job get_job(job_id)

Returns the Job identified by the given UUID.

Returns the Job identified by the given UUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import jobs_api
from collibra_core.model.job import Job
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
    api_instance = jobs_api.JobsApi(api_client)
    job_id = "jobId_example" # str | The ID of the job.

    # example passing only required values which don't have defaults set
    try:
        # Returns the Job identified by the given UUID.
        api_response = api_instance.get_job(job_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The ID of the job. |

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job found. |  -  |
**404** | Job not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

