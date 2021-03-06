# collibra_core.WorkflowDefinitionsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_type_assignment_rule**](WorkflowDefinitionsApi.md#add_asset_type_assignment_rule) | **POST** /workflowDefinitions/{workflowDefinitionId}/assetTypeAssignmentRules | Add asset type assignment rule.
[**add_domain_type_assignment_rule**](WorkflowDefinitionsApi.md#add_domain_type_assignment_rule) | **POST** /workflowDefinitions/{workflowDefinitionId}/domainTypeAssignmentRules | Add domain type assignment rule.
[**change_asset_type_assignment_rule**](WorkflowDefinitionsApi.md#change_asset_type_assignment_rule) | **PATCH** /workflowDefinitions/{workflowDefinitionId}/assetTypeAssignmentRules/{ruleId} | Change asset type assignment rule.
[**change_domain_type_assignment_rule**](WorkflowDefinitionsApi.md#change_domain_type_assignment_rule) | **PATCH** /workflowDefinitions/{workflowDefinitionId}/domainTypeAssignmentRules/{ruleId} | Change domain type assignment rule.
[**change_workflow_definition**](WorkflowDefinitionsApi.md#change_workflow_definition) | **PATCH** /workflowDefinitions/{workflowDefinitionId} | Change workflow definition.
[**deploy_workflow_definition**](WorkflowDefinitionsApi.md#deploy_workflow_definition) | **POST** /workflowDefinitions | Deploy workflow definition.
[**find_workflow_definitions**](WorkflowDefinitionsApi.md#find_workflow_definitions) | **GET** /workflowDefinitions | Find workflow definitions.
[**get_configuration_start_form_data**](WorkflowDefinitionsApi.md#get_configuration_start_form_data) | **GET** /workflowDefinitions/workflowDefinition/{workflowDefinitionId}/configurationStartFormData | Get configuration start form data.
[**get_possible_start_events**](WorkflowDefinitionsApi.md#get_possible_start_events) | **GET** /workflowDefinitions/startEvents | Get all possible workflow start events
[**get_start_form_data**](WorkflowDefinitionsApi.md#get_start_form_data) | **GET** /workflowDefinitions/workflowDefinition/{workflowDefinitionId}/startFormData | Get start form data.
[**get_workflow_definition**](WorkflowDefinitionsApi.md#get_workflow_definition) | **GET** /workflowDefinitions/{workflowDefinitionId} | Get workflow definition.
[**get_workflow_definition_by_process_id**](WorkflowDefinitionsApi.md#get_workflow_definition_by_process_id) | **GET** /workflowDefinitions/process/{processId} | Get workflow definition.
[**get_workflow_definition_diagram**](WorkflowDefinitionsApi.md#get_workflow_definition_diagram) | **GET** /workflowDefinitions/{workflowDefinitionId}/diagram | Get process diagram.
[**get_workflow_definition_xml**](WorkflowDefinitionsApi.md#get_workflow_definition_xml) | **GET** /workflowDefinitions/{workflowDefinitionId}/xml | Get XML of workflow definition.
[**remove_assignment_rule**](WorkflowDefinitionsApi.md#remove_assignment_rule) | **DELETE** /workflowDefinitions/{workflowDefinitionId}/assignmentRules/{ruleId} | Remove assignment rule.
[**remove_workflow_definition**](WorkflowDefinitionsApi.md#remove_workflow_definition) | **DELETE** /workflowDefinitions/{workflowDefinitionId} | Remove workflow definition.
[**remove_workflow_definitions_in_job**](WorkflowDefinitionsApi.md#remove_workflow_definitions_in_job) | **POST** /workflowDefinitions/removalJobs | Remove multiple workflow definitions.


# **add_asset_type_assignment_rule**
> AssetAssignmentRuleImpl add_asset_type_assignment_rule(workflow_definition_id)

Add asset type assignment rule.

Adds an asset type assignment rule to the workflow definition with the specified ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.add_asset_type_assignment_rule_request import AddAssetTypeAssignmentRuleRequest
from collibra_core.model.asset_assignment_rule_impl import AssetAssignmentRuleImpl
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition.
    add_asset_type_assignment_rule_request = AddAssetTypeAssignmentRuleRequest(
        asset_type_id="asset_type_id_example",
        domain_id="domain_id_example",
        community_id="community_id_example",
        status_id="status_id_example",
    ) # AddAssetTypeAssignmentRuleRequest | The request describing assignment rule to be added. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add asset type assignment rule.
        api_response = api_instance.add_asset_type_assignment_rule(workflow_definition_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->add_asset_type_assignment_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add asset type assignment rule.
        api_response = api_instance.add_asset_type_assignment_rule(workflow_definition_id, add_asset_type_assignment_rule_request=add_asset_type_assignment_rule_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->add_asset_type_assignment_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition. |
 **add_asset_type_assignment_rule_request** | [**AddAssetTypeAssignmentRuleRequest**](AddAssetTypeAssignmentRuleRequest.md)| The request describing assignment rule to be added. | [optional]

### Return type

[**AssetAssignmentRuleImpl**](AssetAssignmentRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset type assignment rule successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_domain_type_assignment_rule**
> AssetAssignmentRuleImpl add_domain_type_assignment_rule(workflow_definition_id)

Add domain type assignment rule.

Adds a domain type assignment rule to the workflow definition with the specified ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.add_domain_type_assignment_rule_request import AddDomainTypeAssignmentRuleRequest
from collibra_core.model.asset_assignment_rule_impl import AssetAssignmentRuleImpl
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition.
    add_domain_type_assignment_rule_request = AddDomainTypeAssignmentRuleRequest(
        domain_type_id="domain_type_id_example",
        community_id="community_id_example",
    ) # AddDomainTypeAssignmentRuleRequest | The request describing assignment rule to be added. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add domain type assignment rule.
        api_response = api_instance.add_domain_type_assignment_rule(workflow_definition_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->add_domain_type_assignment_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add domain type assignment rule.
        api_response = api_instance.add_domain_type_assignment_rule(workflow_definition_id, add_domain_type_assignment_rule_request=add_domain_type_assignment_rule_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->add_domain_type_assignment_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition. |
 **add_domain_type_assignment_rule_request** | [**AddDomainTypeAssignmentRuleRequest**](AddDomainTypeAssignmentRuleRequest.md)| The request describing assignment rule to be added. | [optional]

### Return type

[**AssetAssignmentRuleImpl**](AssetAssignmentRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Domain type assignment rule successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_asset_type_assignment_rule**
> AssetAssignmentRuleImpl change_asset_type_assignment_rule(workflow_definition_id, rule_id)

Change asset type assignment rule.

Modifies the asset type assignment rule with the specified ID of the workflow definition with the specified ID.<p>Only properties that are specified in this request and have not <code>null</code> values are updated.<p>All other properties are ignored.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.change_asset_type_assignment_rule_request import ChangeAssetTypeAssignmentRuleRequest
from collibra_core.model.asset_assignment_rule_impl import AssetAssignmentRuleImpl
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition.
    rule_id = "ruleId_example" # str | The ID of the assignment rule to be changed.
    change_asset_type_assignment_rule_request = ChangeAssetTypeAssignmentRuleRequest(
        asset_type_id="asset_type_id_example",
        domain_id="domain_id_example",
        community_id="community_id_example",
        status_id="status_id_example",
    ) # ChangeAssetTypeAssignmentRuleRequest | Parameters for the assignment rule to be changed. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Change asset type assignment rule.
        api_response = api_instance.change_asset_type_assignment_rule(workflow_definition_id, rule_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->change_asset_type_assignment_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change asset type assignment rule.
        api_response = api_instance.change_asset_type_assignment_rule(workflow_definition_id, rule_id, change_asset_type_assignment_rule_request=change_asset_type_assignment_rule_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->change_asset_type_assignment_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition. |
 **rule_id** | **str**| The ID of the assignment rule to be changed. |
 **change_asset_type_assignment_rule_request** | [**ChangeAssetTypeAssignmentRuleRequest**](ChangeAssetTypeAssignmentRuleRequest.md)| Parameters for the assignment rule to be changed. | [optional]

### Return type

[**AssetAssignmentRuleImpl**](AssetAssignmentRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The asset type assignment rule has been successfully updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_domain_type_assignment_rule**
> AssetAssignmentRuleImpl change_domain_type_assignment_rule(workflow_definition_id, rule_id)

Change domain type assignment rule.

Modifies the domain type assignment rule with the specified ID of the workflow definition with the specified ID.<p>Only properties that are specified in this request and have not <code>null</code> values are updated.<p>All other properties are ignored.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.change_domain_type_assignment_rule_request import ChangeDomainTypeAssignmentRuleRequest
from collibra_core.model.asset_assignment_rule_impl import AssetAssignmentRuleImpl
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition.
    rule_id = "ruleId_example" # str | The ID of the assignment rule to be changed.
    change_domain_type_assignment_rule_request = ChangeDomainTypeAssignmentRuleRequest(
        domain_type_id="domain_type_id_example",
        community_id="community_id_example",
    ) # ChangeDomainTypeAssignmentRuleRequest | Parameters for the assignment rule to be changed. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Change domain type assignment rule.
        api_response = api_instance.change_domain_type_assignment_rule(workflow_definition_id, rule_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->change_domain_type_assignment_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change domain type assignment rule.
        api_response = api_instance.change_domain_type_assignment_rule(workflow_definition_id, rule_id, change_domain_type_assignment_rule_request=change_domain_type_assignment_rule_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->change_domain_type_assignment_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition. |
 **rule_id** | **str**| The ID of the assignment rule to be changed. |
 **change_domain_type_assignment_rule_request** | [**ChangeDomainTypeAssignmentRuleRequest**](ChangeDomainTypeAssignmentRuleRequest.md)| Parameters for the assignment rule to be changed. | [optional]

### Return type

[**AssetAssignmentRuleImpl**](AssetAssignmentRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The domain type assignment rule has been successfully updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_workflow_definition**
> WorkflowDefinitionImpl change_workflow_definition(workflow_definition_id)

Change workflow definition.

Modifies the workflow definition with the specified ID.<p>Only properties that are specified in this request and have not <code>null</code> values are updated.<p>All other properties are ignored.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.change_workflow_definition_request import ChangeWorkflowDefinitionRequest
from collibra_core.model.workflow_definition_impl import WorkflowDefinitionImpl
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition.
    change_workflow_definition_request = ChangeWorkflowDefinitionRequest(
        name="name_example",
        description="description_example",
        configuration_variables={
            "key": "key_example",
        },
        start_events=[
            "ASSET_ADDED",
        ],
        business_item_resource_type="ASSET",
        exclusivity="RESOURCE_EXCLUSIVITY",
        guest_user_accessible=True,
        registered_user_accessible=True,
        candidate_user_check_disabled=True,
        candidate_user_check_enabled=True,
        global_create=True,
        enable=True,
        start_label="start_label_example",
        start_role_ids=[
            "start_role_ids_example",
        ],
        stop_role_ids=[
            "stop_role_ids_example",
        ],
        reassign_role_ids=[
            "reassign_role_ids_example",
        ],
    ) # ChangeWorkflowDefinitionRequest | Parameters for the workflow definition to be changed. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Change workflow definition.
        api_response = api_instance.change_workflow_definition(workflow_definition_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->change_workflow_definition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change workflow definition.
        api_response = api_instance.change_workflow_definition(workflow_definition_id, change_workflow_definition_request=change_workflow_definition_request)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->change_workflow_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition. |
 **change_workflow_definition_request** | [**ChangeWorkflowDefinitionRequest**](ChangeWorkflowDefinitionRequest.md)| Parameters for the workflow definition to be changed. | [optional]

### Return type

[**WorkflowDefinitionImpl**](WorkflowDefinitionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workflow definition has been successfully updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_workflow_definition**
> WorkflowDefinitionImpl deploy_workflow_definition()

Deploy workflow definition.

Deploys workflow definition (the business process and resources) using the specified request.<p> The input stream can represent a single file(e.g: .bpmn20.xml or .bpmn) or an archive file (e.g: .zip or .bar). It is not allowed to deploy a resource containing more than one process definition.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.workflow_definition_impl import WorkflowDefinitionImpl
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    file = open('/path/to/file', 'rb') # file_type | The file with described workflow definition. (optional)
    file_name = "file_name_example" # str | The name of the file. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deploy workflow definition.
        api_response = api_instance.deploy_workflow_definition(file=file, file_name=file_name)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->deploy_workflow_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**| The file with described workflow definition. | [optional]
 **file_name** | **str**| The name of the file. | [optional]

### Return type

[**WorkflowDefinitionImpl**](WorkflowDefinitionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workflow definition has been deployed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_workflow_definitions**
> WorkflowDefinitionPagedResponse find_workflow_definitions()

Find workflow definitions.

Finds the workflow definitions matching the criteria described in the request object. By default, the result contains up to 1000 workflow definitions.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.workflow_definition_paged_response import WorkflowDefinitionPagedResponse
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) if omitted the server will use the default value of 0
    limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) if omitted the server will use the default value of 0
    asset_id = [
        "assetId_example",
    ] # [str] | The list of the IDs of business items (assets) for which the workflow definitions should be found. (optional)
    domain_id = [
        "domainId_example",
    ] # [str] | The list of the IDs of business items (domains) for which the workflow definitions should be found. (optional)
    community_id = [
        "communityId_example",
    ] # [str] | The list of the IDs of business items (communities) for which the workflow definitions should be found. (optional)
    enabled = True # bool | Whether the found workflow definitions should be enabled. (optional)
    _global = True # bool | Whether the found workflow definitions should be global. (optional)
    name = "name_example" # str | The name (could be partial) of the workflow definition to search for. (optional)
    sort_order = "ASC" # str | The sorting order. (optional) if omitted the server will use the default value of "ASC"
    description = "description_example" # str | The description (could be partial) of the workflow definition to search for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find workflow definitions.
        api_response = api_instance.find_workflow_definitions(offset=offset, limit=limit, asset_id=asset_id, domain_id=domain_id, community_id=community_id, enabled=enabled, _global=_global, name=name, sort_order=sort_order, description=description)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->find_workflow_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] if omitted the server will use the default value of 0
 **asset_id** | **[str]**| The list of the IDs of business items (assets) for which the workflow definitions should be found. | [optional]
 **domain_id** | **[str]**| The list of the IDs of business items (domains) for which the workflow definitions should be found. | [optional]
 **community_id** | **[str]**| The list of the IDs of business items (communities) for which the workflow definitions should be found. | [optional]
 **enabled** | **bool**| Whether the found workflow definitions should be enabled. | [optional]
 **_global** | **bool**| Whether the found workflow definitions should be global. | [optional]
 **name** | **str**| The name (could be partial) of the workflow definition to search for. | [optional]
 **sort_order** | **str**| The sorting order. | [optional] if omitted the server will use the default value of "ASC"
 **description** | **str**| The description (could be partial) of the workflow definition to search for. | [optional]

### Return type

[**WorkflowDefinitionPagedResponse**](WorkflowDefinitionPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response with found workflow definitions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_start_form_data**
> StartFormDataImpl get_configuration_start_form_data(workflow_definition_id)

Get configuration start form data.

Returns the task configuration start form data of the workflow definition with the specified ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.start_form_data_impl import StartFormDataImpl
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition that should be used for the form data retrieval.
    form_property_type = "formPropertyType_example" # str | The form type to be returned. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get configuration start form data.
        api_response = api_instance.get_configuration_start_form_data(workflow_definition_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->get_configuration_start_form_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get configuration start form data.
        api_response = api_instance.get_configuration_start_form_data(workflow_definition_id, form_property_type=form_property_type)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->get_configuration_start_form_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition that should be used for the form data retrieval. |
 **form_property_type** | **str**| The form type to be returned. | [optional]

### Return type

[**StartFormDataImpl**](StartFormDataImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration start form data for workflow definition. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_possible_start_events**
> [NamedDescribedWorkflowStartEventType] get_possible_start_events()

Get all possible workflow start events

Returns all possible workflow start events, including event name and description

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.named_described_workflow_start_event_type import NamedDescribedWorkflowStartEventType
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all possible workflow start events
        api_response = api_instance.get_possible_start_events()
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->get_possible_start_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[NamedDescribedWorkflowStartEventType]**](NamedDescribedWorkflowStartEventType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All possible workflow start events with name and description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_start_form_data**
> StartFormDataImpl get_start_form_data(workflow_definition_id)

Get start form data.

Returns the task start form data of the workflow definition with the specified ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.start_form_data_impl import StartFormDataImpl
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition that should be used for the form data retrieval.
    form_property_type = "formPropertyType_example" # str | The form type to be returned. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get start form data.
        api_response = api_instance.get_start_form_data(workflow_definition_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->get_start_form_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get start form data.
        api_response = api_instance.get_start_form_data(workflow_definition_id, form_property_type=form_property_type)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->get_start_form_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition that should be used for the form data retrieval. |
 **form_property_type** | **str**| The form type to be returned. | [optional]

### Return type

[**StartFormDataImpl**](StartFormDataImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The start form data for workflow definition. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_definition**
> WorkflowDefinitionImpl get_workflow_definition(workflow_definition_id)

Get workflow definition.

Returns the workflow definition with the specified ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.workflow_definition_impl import WorkflowDefinitionImpl
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition.

    # example passing only required values which don't have defaults set
    try:
        # Get workflow definition.
        api_response = api_instance.get_workflow_definition(workflow_definition_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->get_workflow_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition. |

### Return type

[**WorkflowDefinitionImpl**](WorkflowDefinitionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workflow definition successfully found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_definition_by_process_id**
> WorkflowDefinitionImpl get_workflow_definition_by_process_id(process_id)

Get workflow definition.

Returns the workflow definition with the specified process ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
from collibra_core.model.workflow_definition_impl import WorkflowDefinitionImpl
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    process_id = "processId_example" # str | The process ID of the workflow definition.

    # example passing only required values which don't have defaults set
    try:
        # Get workflow definition.
        api_response = api_instance.get_workflow_definition_by_process_id(process_id)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->get_workflow_definition_by_process_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The process ID of the workflow definition. |

### Return type

[**WorkflowDefinitionImpl**](WorkflowDefinitionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workflow definition successfully found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_definition_diagram**
> get_workflow_definition_diagram(workflow_definition_id)

Get process diagram.

Returns the process diagram of the workflow definition with the specified ID. The diagram input stream returned can be null as deployed workflow definitions without graphical notation included do not have a diagram.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition.

    # example passing only required values which don't have defaults set
    try:
        # Get process diagram.
        api_instance.get_workflow_definition_diagram(workflow_definition_id)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->get_workflow_definition_diagram: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition. |

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
**200** | The workflow definition diagram successfully found. |  -  |
**204** | No diagram has been found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_definition_xml**
> get_workflow_definition_xml(workflow_definition_id)

Get XML of workflow definition.

Returns the XML source of the workflow definition with the specified ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition.

    # example passing only required values which don't have defaults set
    try:
        # Get XML of workflow definition.
        api_instance.get_workflow_definition_xml(workflow_definition_id)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->get_workflow_definition_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workflow definition XML successfully found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_assignment_rule**
> remove_assignment_rule(workflow_definition_id, rule_id)

Remove assignment rule.

Removes the assignment rule with the specified ID from the workflow definition with the specified ID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition.
    rule_id = "ruleId_example" # str | The ID of the assignment rule.

    # example passing only required values which don't have defaults set
    try:
        # Remove assignment rule.
        api_instance.remove_assignment_rule(workflow_definition_id, rule_id)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->remove_assignment_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition. |
 **rule_id** | **str**| The ID of the assignment rule. |

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
**200** | Assignment rule has been removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_workflow_definition**
> remove_workflow_definition(workflow_definition_id)

Remove workflow definition.

Removes the workflow definition with the specified ID. The workflow definition will be completely removed from the application, including any history.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    workflow_definition_id = "workflowDefinitionId_example" # str | The ID of the workflow definition.

    # example passing only required values which don't have defaults set
    try:
        # Remove workflow definition.
        api_instance.remove_workflow_definition(workflow_definition_id)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->remove_workflow_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| The ID of the workflow definition. |

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
**204** | The workflow definition has been successfully removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_workflow_definitions_in_job**
> Job remove_workflow_definitions_in_job()

Remove multiple workflow definitions.

Removes multiple workflow definitions asynchronously. The workflow definition(s) will be completely removed from the application, including any history.

### Example

* Basic Authentication (basicAuth):
```python
import time
import collibra_core
from collibra_core.api import workflow_definitions_api
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
    api_instance = workflow_definitions_api.WorkflowDefinitionsApi(api_client)
    request_body = [
        "request_body_example",
    ] # [str] | The list of IDs of the workflow definitions to remove. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove multiple workflow definitions.
        api_response = api_instance.remove_workflow_definitions_in_job(request_body=request_body)
        pprint(api_response)
    except collibra_core.ApiException as e:
        print("Exception when calling WorkflowDefinitionsApi->remove_workflow_definitions_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[str]**| The list of IDs of the workflow definitions to remove. | [optional]

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The job for removal workflow definitions has been created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

