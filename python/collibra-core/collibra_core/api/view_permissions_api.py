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
from collibra_core.model.add_view_permission_request import AddViewPermissionRequest
from collibra_core.model.paged_response_view_permission import PagedResponseViewPermission
from collibra_core.model.view_permission_impl import ViewPermissionImpl


class ViewPermissionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __add_view_permission(
            self,
            **kwargs
        ):
            """Adds a view permission.  # noqa: E501

            Adds a view permission.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.add_view_permission(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                add_view_permission_request (AddViewPermissionRequest): Properties of the new view permission.. [optional]
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
                ViewPermissionImpl
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

        self.add_view_permission = Endpoint(
            settings={
                'response_type': (ViewPermissionImpl,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/viewPermissions',
                'operation_id': 'add_view_permission',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'add_view_permission_request',
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
                    'add_view_permission_request':
                        (AddViewPermissionRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'add_view_permission_request': 'body',
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
            callable=__add_view_permission
        )

        def __find_view_permissions(
            self,
            **kwargs
        ):
            """Finds view permissions with given criteria.  # noqa: E501

            Finds view permissions with given criteria.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.find_view_permissions(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                offset (int): The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.. [optional] if omitted the server will use the default value of 0
                limit (int): The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.. [optional] if omitted the server will use the default value of 0
                user_id (str): The ID of the user for whom the view permission applies.. [optional]
                user_group_id (str): The ID of the user group for whose members the view permission applies.. [optional]
                resource_id (str): The ID of the resource to which the view permission applies.. [optional]
                resource_type (str): The type of resource addressed by the view permission.. [optional]
                include_inherited (bool): Whether to include inherited permissions in search results.. [optional]
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
                PagedResponseViewPermission
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

        self.find_view_permissions = Endpoint(
            settings={
                'response_type': (PagedResponseViewPermission,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/viewPermissions',
                'operation_id': 'find_view_permissions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'offset',
                    'limit',
                    'user_id',
                    'user_group_id',
                    'resource_id',
                    'resource_type',
                    'include_inherited',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'resource_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('resource_type',): {

                        "VIEW": "View",
                        "ASSET": "Asset",
                        "COMMUNITY": "Community",
                        "DOMAIN": "Domain",
                        "ASSETTYPE": "AssetType",
                        "DOMAINTYPE": "DomainType",
                        "STATUS": "Status",
                        "USER": "User",
                        "CLASSIFICATIONMATCH": "ClassificationMatch",
                        "USERGROUP": "UserGroup",
                        "ATTRIBUTE": "Attribute",
                        "STRINGATTRIBUTE": "StringAttribute",
                        "SCRIPTATTRIBUTE": "ScriptAttribute",
                        "BOOLEANATTRIBUTE": "BooleanAttribute",
                        "DATEATTRIBUTE": "DateAttribute",
                        "NUMERICATTRIBUTE": "NumericAttribute",
                        "SINGLEVALUELISTATTRIBUTE": "SingleValueListAttribute",
                        "MULTIVALUELISTATTRIBUTE": "MultiValueListAttribute",
                        "COMMENT": "Comment",
                        "ATTACHMENT": "Attachment",
                        "RESPONSIBILITY": "Responsibility",
                        "WORKFLOW": "Workflow",
                        "JOB": "Job",
                        "RELATION": "Relation",
                        "RELATIONTYPE": "RelationType",
                        "COMPLEXRELATION": "ComplexRelation",
                        "COMPLEXRELATIONTYPE": "ComplexRelationType",
                        "ARTICULATIONRULE": "ArticulationRule",
                        "ASSIGNMENT": "Assignment",
                        "SCOPE": "Scope",
                        "RELATIONTRACE": "RelationTrace",
                        "VALIDATIONRULE": "ValidationRule",
                        "DATAQUALITYRULE": "DataQualityRule",
                        "DATAQUALITYMETRIC": "DataQualityMetric",
                        "ADDRESS": "Address",
                        "INSTANTMESSAGINGACCOUNT": "InstantMessagingAccount",
                        "EMAIL": "Email",
                        "PHONENUMBER": "PhoneNumber",
                        "WEBSITE": "Website",
                        "ACTIVITY": "Activity",
                        "FORMPROPERTY": "FormProperty",
                        "WORKFLOWTASK": "WorkflowTask",
                        "ACTIVITYCHANGE": "ActivityChange",
                        "WORKFLOWINSTANCE": "WorkflowInstance",
                        "ROLE": "Role",
                        "ATTRIBUTETYPE": "AttributeType",
                        "BOOLEANATTRIBUTETYPE": "BooleanAttributeType",
                        "DATEATTRIBUTETYPE": "DateAttributeType",
                        "DATETIMEATTRIBUTETYPE": "DateTimeAttributeType",
                        "MULTIVALUELISTATTRIBUTETYPE": "MultiValueListAttributeType",
                        "NUMERICATTRIBUTETYPE": "NumericAttributeType",
                        "SCRIPTATTRIBUTETYPE": "ScriptAttributeType",
                        "SINGLEVALUELISTATTRIBUTETYPE": "SingleValueListAttributeType",
                        "STRINGATTRIBUTETYPE": "StringAttributeType",
                        "VIEWSHARINGRULE": "ViewSharingRule",
                        "VIEWASSIGNMENTRULE": "ViewAssignmentRule",
                        "JDBCDRIVERFILE": "JdbcDriverFile",
                        "JDBCDRIVER": "JdbcDriver",
                        "JDBCINGESTIONPROPERTIES": "JdbcIngestionProperties",
                        "CSVINGESTIONPROPERTIES": "CsvIngestionProperties",
                        "EXCELINGESTIONPROPERTIES": "ExcelIngestionProperties",
                        "CONNECTIONSTRINGPARAMETER": "ConnectionStringParameter",
                        "ASSIGNEDCHARACTERISTICTYPE": "AssignedCharacteristicType",
                        "NOTIFICATION": "Notification",
                        "TAG": "Tag",
                        "COMPLEXRELATIONLEGTYPE": "ComplexRelationLegType",
                        "COMPLEXRELATIONATTRIBUTETYPE": "ComplexRelationAttributeType",
                        "COMPLEXRELATIONLEG": "ComplexRelationLeg",
                        "BASEDATATYPE": "BaseDataType",
                        "ADVANCEDDATATYPE": "AdvancedDataType",
                        "DIAGRAMPICTURE": "DiagramPicture",
                        "DIAGRAMPICTURESHARINGRULE": "DiagramPictureSharingRule",
                        "DIAGRAMPICTUREASSIGNMENTRULE": "DiagramPictureAssignmentRule",
                        "RATING": "Rating",
                        "CLASSIFICATION": "Classification"
                    },
                },
                'openapi_types': {
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                    'user_id':
                        (str,),
                    'user_group_id':
                        (str,),
                    'resource_id':
                        (str,),
                    'resource_type':
                        (str,),
                    'include_inherited':
                        (bool,),
                },
                'attribute_map': {
                    'offset': 'offset',
                    'limit': 'limit',
                    'user_id': 'userId',
                    'user_group_id': 'userGroupId',
                    'resource_id': 'resourceId',
                    'resource_type': 'resourceType',
                    'include_inherited': 'includeInherited',
                },
                'location_map': {
                    'offset': 'query',
                    'limit': 'query',
                    'user_id': 'query',
                    'user_group_id': 'query',
                    'resource_id': 'query',
                    'resource_type': 'query',
                    'include_inherited': 'query',
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
            callable=__find_view_permissions
        )

        def __get_view_permission(
            self,
            view_permission_id,
            **kwargs
        ):
            """Retrieves a view permission.  # noqa: E501

            Retrieves a view permission.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_view_permission(view_permission_id, async_req=True)
            >>> result = thread.get()

            Args:
                view_permission_id (str): Identifier of the view permission to retrieve.

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
                ViewPermissionImpl
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
            kwargs['view_permission_id'] = \
                view_permission_id
            return self.call_with_http_info(**kwargs)

        self.get_view_permission = Endpoint(
            settings={
                'response_type': (ViewPermissionImpl,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/viewPermissions/{viewPermissionId}',
                'operation_id': 'get_view_permission',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'view_permission_id',
                ],
                'required': [
                    'view_permission_id',
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
                    'view_permission_id':
                        (str,),
                },
                'attribute_map': {
                    'view_permission_id': 'viewPermissionId',
                },
                'location_map': {
                    'view_permission_id': 'path',
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
            callable=__get_view_permission
        )

        def __remove_view_permission(
            self,
            view_permission_id,
            **kwargs
        ):
            """Removes a view permission.  # noqa: E501

            Removes a view permission.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.remove_view_permission(view_permission_id, async_req=True)
            >>> result = thread.get()

            Args:
                view_permission_id (str): Identifier of the view permission to remove.

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
            kwargs['view_permission_id'] = \
                view_permission_id
            return self.call_with_http_info(**kwargs)

        self.remove_view_permission = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/viewPermissions/{viewPermissionId}',
                'operation_id': 'remove_view_permission',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'view_permission_id',
                ],
                'required': [
                    'view_permission_id',
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
                    'view_permission_id':
                        (str,),
                },
                'attribute_map': {
                    'view_permission_id': 'viewPermissionId',
                },
                'location_map': {
                    'view_permission_id': 'path',
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
            callable=__remove_view_permission
        )
