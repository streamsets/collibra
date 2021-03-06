"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from collibra_core.api_client import ApiClient, Endpoint
from collibra_core.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from collibra_core.model.complete_workflow_tasks_request import CompleteWorkflowTasksRequest
from collibra_core.model.task_form_data import TaskFormData
from collibra_core.model.workflow_task import WorkflowTask
from collibra_core.model.workflow_task_paged_response import WorkflowTaskPagedResponse


class WorkflowTasksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __cancel_workflow_task(
            self,
            workflow_task_id,
            **kwargs
        ):
            """Cancel workflow task.  # noqa: E501

            Cancels the workflow task with the specified ID with a reason. If the given workflow is a subprocess, this method makes sure everything is cancelled from the root process instance. If the given task is not found, this method will assume it already was cancelled without throwing any error.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.cancel_workflow_task(workflow_task_id, async_req=True)
            >>> result = thread.get()

            Args:
                workflow_task_id (str): The ID of the workflow task.

            Keyword Args:
                body (str): The reason for the cancellation of the workflow task.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['workflow_task_id'] = \
                workflow_task_id
            return self.call_with_http_info(**kwargs)

        self.cancel_workflow_task = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowTasks/{workflowTaskId}/canceled',
                'operation_id': 'cancel_workflow_task',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workflow_task_id',
                    'body',
                ],
                'required': [
                    'workflow_task_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workflow_task_id':
                        (str,),
                    'body':
                        (str,),
                },
                'attribute_map': {
                    'workflow_task_id': 'workflowTaskId',
                },
                'location_map': {
                    'workflow_task_id': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__cancel_workflow_task
        )

        def __complete_workflow_tasks(
            self,
            **kwargs
        ):
            """Complete workflow tasks.  # noqa: E501

            Completes tasks based on the provided request and returns the following tasks, if the same user is assigned to them.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.complete_workflow_tasks(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                complete_workflow_tasks_request (CompleteWorkflowTasksRequest): Request to complete the workflow tasks.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [WorkflowTask]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.complete_workflow_tasks = Endpoint(
            settings={
                'response_type': ([WorkflowTask],),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowTasks/completed',
                'operation_id': 'complete_workflow_tasks',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'complete_workflow_tasks_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'complete_workflow_tasks_request':
                        (CompleteWorkflowTasksRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'complete_workflow_tasks_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__complete_workflow_tasks
        )

        def __find_workflow_tasks(
            self,
            **kwargs
        ):
            """Find workflow tasks.  # noqa: E501

            Returns the workflow tasks matching given search criteria.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.find_workflow_tasks(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                offset (int): The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.. [optional] if omitted the server will use the default value of 0
                limit (int): The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.. [optional] if omitted the server will use the default value of 0
                business_item_id (str): The ID of the business item. [optional]
                business_item_type (str): The type of the business item. [optional]
                workflow_task_user_relation (str): The type of relation between user and searched tasks. This could be either set to search for all the tasks the user is permitted to view or just those assigned to the user.. [optional] if omitted the server will use the default value of "ALL"
                business_item_name (str): The part of the name of the business item.. [optional]
                description (str): The part of the task description.. [optional]
                user_id (str): The ID of the user for which the tasks need to be returned. If empty, the current logged in user will be used. [optional]
                create_date (int): The creation date of the task. It is the timestamp (in UTC time standard). [optional]
                due_date (int): The due date of the task. It is the timestamp (in UTC time standard). [optional]
                title (str): The title/name of the task.. [optional]
                type (str): The task type.. [optional]
                sort_field (str): The field on which the results are sorted. On due date by default.. [optional] if omitted the server will use the default value of "DUE_DATE"
                sort_order (str): The sorting order.. [optional] if omitted the server will use the default value of "DESC"
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                WorkflowTaskPagedResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.find_workflow_tasks = Endpoint(
            settings={
                'response_type': (WorkflowTaskPagedResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowTasks',
                'operation_id': 'find_workflow_tasks',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'offset',
                    'limit',
                    'business_item_id',
                    'business_item_type',
                    'workflow_task_user_relation',
                    'business_item_name',
                    'description',
                    'user_id',
                    'create_date',
                    'due_date',
                    'title',
                    'type',
                    'sort_field',
                    'sort_order',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'business_item_type',
                    'workflow_task_user_relation',
                    'sort_field',
                    'sort_order',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('business_item_type',): {

                        "ASSET": "ASSET",
                        "DOMAIN": "DOMAIN",
                        "COMMUNITY": "COMMUNITY"
                    },
                    ('workflow_task_user_relation',): {

                        "ALL": "ALL",
                        "ASSIGNED": "ASSIGNED",
                        "MY_OVERDUE": "MY_OVERDUE"
                    },
                    ('sort_field',): {

                        "DUE_DATE": "DUE_DATE",
                        "CREATION_DATE": "CREATION_DATE",
                        "TITLE": "TITLE",
                        "ITEM": "ITEM",
                        "DESCRIPTION": "DESCRIPTION"
                    },
                    ('sort_order',): {

                        "ASC": "ASC",
                        "DESC": "DESC"
                    },
                },
                'openapi_types': {
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                    'business_item_id':
                        (str,),
                    'business_item_type':
                        (str,),
                    'workflow_task_user_relation':
                        (str,),
                    'business_item_name':
                        (str,),
                    'description':
                        (str,),
                    'user_id':
                        (str,),
                    'create_date':
                        (int,),
                    'due_date':
                        (int,),
                    'title':
                        (str,),
                    'type':
                        (str,),
                    'sort_field':
                        (str,),
                    'sort_order':
                        (str,),
                },
                'attribute_map': {
                    'offset': 'offset',
                    'limit': 'limit',
                    'business_item_id': 'businessItemId',
                    'business_item_type': 'businessItemType',
                    'workflow_task_user_relation': 'workflowTaskUserRelation',
                    'business_item_name': 'businessItemName',
                    'description': 'description',
                    'user_id': 'userId',
                    'create_date': 'createDate',
                    'due_date': 'dueDate',
                    'title': 'title',
                    'type': 'type',
                    'sort_field': 'sortField',
                    'sort_order': 'sortOrder',
                },
                'location_map': {
                    'offset': 'query',
                    'limit': 'query',
                    'business_item_id': 'query',
                    'business_item_type': 'query',
                    'workflow_task_user_relation': 'query',
                    'business_item_name': 'query',
                    'description': 'query',
                    'user_id': 'query',
                    'create_date': 'query',
                    'due_date': 'query',
                    'title': 'query',
                    'type': 'query',
                    'sort_field': 'query',
                    'sort_order': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__find_workflow_tasks
        )

        def __get_task_form_data(
            self,
            workflow_task_id,
            **kwargs
        ):
            """Get task form data.  # noqa: E501

            Returns the task form data of the workflow task with the specified ID and form property type.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_task_form_data(workflow_task_id, async_req=True)
            >>> result = thread.get()

            Args:
                workflow_task_id (str): Workflow task ID.

            Keyword Args:
                form_property_type (str): Form property type.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                TaskFormData
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['workflow_task_id'] = \
                workflow_task_id
            return self.call_with_http_info(**kwargs)

        self.get_task_form_data = Endpoint(
            settings={
                'response_type': (TaskFormData,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowTasks/{workflowTaskId}/taskFormData',
                'operation_id': 'get_task_form_data',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workflow_task_id',
                    'form_property_type',
                ],
                'required': [
                    'workflow_task_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workflow_task_id':
                        (str,),
                    'form_property_type':
                        (str,),
                },
                'attribute_map': {
                    'workflow_task_id': 'workflowTaskId',
                    'form_property_type': 'formPropertyType',
                },
                'location_map': {
                    'workflow_task_id': 'path',
                    'form_property_type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_task_form_data
        )

        def __get_workflow_task(
            self,
            workflow_task_id,
            **kwargs
        ):
            """Get workflow task.  # noqa: E501

            Returns the workflow task with the specified ID. A task will only be returned when the user has the correct permission to view it.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_workflow_task(workflow_task_id, async_req=True)
            >>> result = thread.get()

            Args:
                workflow_task_id (str): The ID of the workflow task to return.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                WorkflowTask
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['workflow_task_id'] = \
                workflow_task_id
            return self.call_with_http_info(**kwargs)

        self.get_workflow_task = Endpoint(
            settings={
                'response_type': (WorkflowTask,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowTasks/{workflowTaskId}',
                'operation_id': 'get_workflow_task',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workflow_task_id',
                ],
                'required': [
                    'workflow_task_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workflow_task_id':
                        (str,),
                },
                'attribute_map': {
                    'workflow_task_id': 'workflowTaskId',
                },
                'location_map': {
                    'workflow_task_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_workflow_task
        )

        def __reassign_task(
            self,
            workflow_task_id,
            **kwargs
        ):
            """Reassign task.  # noqa: E501

            Reassigns the task with the specified ID to one or more users, groups or roles. Caller needs to provide at least one of the value list for users, groups or roles. If roles are provided then the same number of communities needs to be provided also.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.reassign_task(workflow_task_id, async_req=True)
            >>> result = thread.get()

            Args:
                workflow_task_id (str): The ID of the workflow task.

            Keyword Args:
                users ([str]): The user IDs to reassign to.. [optional]
                groups ([str]): The group IDs to reassign to.. [optional]
                roles ([str]): The role IDs to reassign to.. [optional]
                communities ([str]): The Community IDs of the specified roles to reassign to.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['workflow_task_id'] = \
                workflow_task_id
            return self.call_with_http_info(**kwargs)

        self.reassign_task = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowTasks/{workflowTaskId}/reassign',
                'operation_id': 'reassign_task',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workflow_task_id',
                    'users',
                    'groups',
                    'roles',
                    'communities',
                ],
                'required': [
                    'workflow_task_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workflow_task_id':
                        (str,),
                    'users':
                        ([str],),
                    'groups':
                        ([str],),
                    'roles':
                        ([str],),
                    'communities':
                        ([str],),
                },
                'attribute_map': {
                    'workflow_task_id': 'workflowTaskId',
                    'users': 'users',
                    'groups': 'groups',
                    'roles': 'roles',
                    'communities': 'communities',
                },
                'location_map': {
                    'workflow_task_id': 'path',
                    'users': 'query',
                    'groups': 'query',
                    'roles': 'query',
                    'communities': 'query',
                },
                'collection_format_map': {
                    'users': 'multi',
                    'groups': 'multi',
                    'roles': 'multi',
                    'communities': 'multi',
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__reassign_task
        )
