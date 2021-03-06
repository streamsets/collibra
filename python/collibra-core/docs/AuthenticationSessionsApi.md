# collibra_core.AuthenticationSessionsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**is_logged_in**](AuthenticationSessionsApi.md#is_logged_in) | **GET** /auth/sessions/current | Get session
[**login**](AuthenticationSessionsApi.md#login) | **POST** /auth/sessions | Login
[**logout**](AuthenticationSessionsApi.md#logout) | **DELETE** /auth/sessions/current | Logout


# **is_logged_in**
> is_logged_in()

Get session

Gets current session (checks if user is logged in).

### Example

```python
import time
import collibra_core
from collibra_core.api import authentication__sessions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)


# Enter a context with an instance of the API client
with collibra_core.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication__sessions_api.AuthenticationSessionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get session
        api_instance.is_logged_in()
    except collibra_core.ApiException as e:
        print("Exception when calling AuthenticationSessionsApi->is_logged_in: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user is logged in. |  -  |
**401** | The user is not authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> DGCSession login()

Login

Authenticates a user and creates a new session on the server. Once the user is authenticated then the returned session id can be used to access DGC REST Api in subsequent requests. The method additionally returns the JSESSIONID cookie in a <code>Set-Cookie</code> header. If user already has an open session then this session will be terminated.

### Example

```python
import time
import collibra_core
from collibra_core.api import authentication__sessions_api
from collibra_core.model.login_request import LoginRequest
from collibra_core.model.dgc_session import DGCSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)


# Enter a context with an instance of the API client
with collibra_core.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication__sessions_api.AuthenticationSessionsApi(api_client)
    login_request = LoginRequest(
        username="username_example",
        password="password_example",
    ) # LoginRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Login
        api_response = api_instance.login(login_request=login_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling AuthenticationSessionsApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | [optional]

### Return type

[**DGCSession**](DGCSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user was logged in and a new session was created. The response includes the CSRF token that is created |  -  |
**401** | The user is not authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

Logout

Logs current user out and destroys the active session.

### Example

```python
import time
import collibra_core
from collibra_core.api import authentication__sessions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)


# Enter a context with an instance of the API client
with collibra_core.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication__sessions_api.AuthenticationSessionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Logout
        api_instance.logout()
    except collibra_core.ApiException as e:
        print("Exception when calling AuthenticationSessionsApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The user was logged out and session closed. |  -  |
**401** | The user is not authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

