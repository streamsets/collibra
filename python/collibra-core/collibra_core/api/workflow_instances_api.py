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
from collibra_core.model.job import Job
from collibra_core.model.message_event_received_request import MessageEventReceivedRequest
from collibra_core.model.paged_response import PagedResponse
from collibra_core.model.start_workflow_instances_request import StartWorkflowInstancesRequest
from collibra_core.model.workflow_instance import WorkflowInstance


class WorkflowInstancesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __cancel_workflow_instances(
            self,
            workflow_instance_id,
            **kwargs
        ):
            """Cancel workflow instance.  # noqa: E501

            Cancels the workflow instance with the specified ID with a reason. Canceling the workflow instance also cancels the workflow sub-processes.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.cancel_workflow_instances(workflow_instance_id, async_req=True)
            >>> result = thread.get()

            Args:
                workflow_instance_id (str): The identifier of the workflow instance to be cancelled.

            Keyword Args:
                body (str): The reason for the cancellation of the workflow instance.. [optional]
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
            kwargs['workflow_instance_id'] = \
                workflow_instance_id
            return self.call_with_http_info(**kwargs)

        self.cancel_workflow_instances = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowInstances/{workflowInstanceId}/canceled',
                'operation_id': 'cancel_workflow_instances',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workflow_instance_id',
                    'body',
                ],
                'required': [
                    'workflow_instance_id',
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
                    'workflow_instance_id':
                        (str,),
                    'body':
                        (str,),
                },
                'attribute_map': {
                    'workflow_instance_id': 'workflowInstanceId',
                },
                'location_map': {
                    'workflow_instance_id': 'path',
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
            callable=__cancel_workflow_instances
        )

        def __find_workflow_instances(
            self,
            **kwargs
        ):
            """Find workflow instances.  # noqa: E501

            Returns workflow instances matching given search criteria.<p>Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned workflow instances satisfy all constraints that are specified in this search criteria.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.find_workflow_instances(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                offset (int): The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.. [optional] if omitted the server will use the default value of 0
                limit (int): The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.. [optional] if omitted the server will use the default value of 0
                business_item_name (str): The display name of the business item that should be contained by the searched workflows.. [optional]
                business_item_id (str): The ID of the business item that should be contained by the searched workflows.. [optional]
                workflow_definition_id (str): The ID of the workflow definition.. [optional]
                sort_field (str): The field on which the results are sorted.. [optional] if omitted the server will use the default value of "START_DATE"
                sort_order (str): The sorting order.. [optional] if omitted the server will use the default value of "DESC"
                parent_workflow_instance_id (str): The ID of the parent workflow instance.. [optional]
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
                PagedResponse
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

        self.find_workflow_instances = Endpoint(
            settings={
                'response_type': (PagedResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowInstances',
                'operation_id': 'find_workflow_instances',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'offset',
                    'limit',
                    'business_item_name',
                    'business_item_id',
                    'workflow_definition_id',
                    'sort_field',
                    'sort_order',
                    'parent_workflow_instance_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
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
                    ('sort_field',): {

                        "START_DATE": "START_DATE"
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
                    'business_item_name':
                        (str,),
                    'business_item_id':
                        (str,),
                    'workflow_definition_id':
                        (str,),
                    'sort_field':
                        (str,),
                    'sort_order':
                        (str,),
                    'parent_workflow_instance_id':
                        (str,),
                },
                'attribute_map': {
                    'offset': 'offset',
                    'limit': 'limit',
                    'business_item_name': 'businessItemName',
                    'business_item_id': 'businessItemId',
                    'workflow_definition_id': 'workflowDefinitionId',
                    'sort_field': 'sortField',
                    'sort_order': 'sortOrder',
                    'parent_workflow_instance_id': 'parentWorkflowInstanceId',
                },
                'location_map': {
                    'offset': 'query',
                    'limit': 'query',
                    'business_item_name': 'query',
                    'business_item_id': 'query',
                    'workflow_definition_id': 'query',
                    'sort_field': 'query',
                    'sort_order': 'query',
                    'parent_workflow_instance_id': 'query',
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
            callable=__find_workflow_instances
        )

        def __get_workflow_instance_diagram(
            self,
            workflow_instance_id,
            **kwargs
        ):
            """Returns the file representing the diagram of workflow instance identified by the given ID.  # noqa: E501

            Returns the file representing the diagram of workflow instance identified by the given ID. The diagram input stream returned can be null as deployed workflow defintions without graphical notation included don't have a diagram  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_workflow_instance_diagram(workflow_instance_id, async_req=True)
            >>> result = thread.get()

            Args:
                workflow_instance_id (str): The ID of the workflow instance to return the diagram for.

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
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
            kwargs['workflow_instance_id'] = \
                workflow_instance_id
            return self.call_with_http_info(**kwargs)

        self.get_workflow_instance_diagram = Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowInstances/{workflowInstanceId}/diagram',
                'operation_id': 'get_workflow_instance_diagram',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workflow_instance_id',
                ],
                'required': [
                    'workflow_instance_id',
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
                    'workflow_instance_id':
                        (str,),
                },
                'attribute_map': {
                    'workflow_instance_id': 'workflowInstanceId',
                },
                'location_map': {
                    'workflow_instance_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'image/png'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_workflow_instance_diagram
        )

        def __message_event_received(
            self,
            process_instance_id,
            message_name,
            **kwargs
        ):
            """Pass message event to workflow engine.  # noqa: E501

            Passes the message event to the workflow engine. It will pass on this specific event to the engine with the given name, process instance and variables.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.message_event_received(process_instance_id, message_name, async_req=True)
            >>> result = thread.get()

            Args:
                process_instance_id (str): The ID of an instance of a process. Given process instance should have only one execution running at the time. Otherwise this method will fail.
                message_name (str): The name of the message to trigger.

            Keyword Args:
                message_event_received_request (MessageEventReceivedRequest): The properties of the message event to be received.. [optional]
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
            kwargs['process_instance_id'] = \
                process_instance_id
            kwargs['message_name'] = \
                message_name
            return self.call_with_http_info(**kwargs)

        self.message_event_received = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowInstances/{processInstanceId}/messageEvents/{messageName}',
                'operation_id': 'message_event_received',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'process_instance_id',
                    'message_name',
                    'message_event_received_request',
                ],
                'required': [
                    'process_instance_id',
                    'message_name',
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
                    'process_instance_id':
                        (str,),
                    'message_name':
                        (str,),
                    'message_event_received_request':
                        (MessageEventReceivedRequest,),
                },
                'attribute_map': {
                    'process_instance_id': 'processInstanceId',
                    'message_name': 'messageName',
                },
                'location_map': {
                    'process_instance_id': 'path',
                    'message_name': 'path',
                    'message_event_received_request': 'body',
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
            callable=__message_event_received
        )

        def __start_workflow_instances(
            self,
            **kwargs
        ):
            """Start workflow instances.  # noqa: E501

            Starts multiple workflow instances based on the provided request.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.start_workflow_instances(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                start_workflow_instances_request (StartWorkflowInstancesRequest): The properties of the workflow to be started.. [optional]
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
                [WorkflowInstance]
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

        self.start_workflow_instances = Endpoint(
            settings={
                'response_type': ([WorkflowInstance],),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowInstances',
                'operation_id': 'start_workflow_instances',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'start_workflow_instances_request',
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
                    'start_workflow_instances_request':
                        (StartWorkflowInstancesRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'start_workflow_instances_request': 'body',
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
            callable=__start_workflow_instances
        )

        def __start_workflow_instances_in_job(
            self,
            **kwargs
        ):
            """Start workflow instances.  # noqa: E501

            Starts multiple workflow instances asynchronously based on the provided request.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.start_workflow_instances_in_job(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                start_workflow_instances_request (StartWorkflowInstancesRequest): Properties of the workflow to be started.. [optional]
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
                Job
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

        self.start_workflow_instances_in_job = Endpoint(
            settings={
                'response_type': (Job,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/workflowInstances/startJobs',
                'operation_id': 'start_workflow_instances_in_job',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'start_workflow_instances_request',
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
                    'start_workflow_instances_request':
                        (StartWorkflowInstancesRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'start_workflow_instances_request': 'body',
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
            callable=__start_workflow_instances_in_job
        )
