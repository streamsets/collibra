"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from collibra_core.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from collibra_core.model.address import Address
    from collibra_core.model.email import Email
    from collibra_core.model.instant_messaging_account import InstantMessagingAccount
    from collibra_core.model.phone_number import PhoneNumber
    from collibra_core.model.website import Website
    globals()['Address'] = Address
    globals()['Email'] = Email
    globals()['InstantMessagingAccount'] = InstantMessagingAccount
    globals()['PhoneNumber'] = PhoneNumber
    globals()['Website'] = Website


class AddUserRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('gender',): {
            'MALE': "MALE",
            'FEMALE': "FEMALE",
            'UNKNOWN': "UNKNOWN",
        },
        ('license_type',): {
            'CONSUMER': "CONSUMER",
            'AUTHOR': "AUTHOR",
        },
    }

    validations = {
        ('user_name',): {
            'max_length': 2147483647,
            'min_length': 1,
        },
        ('email_address',): {
            'max_length': 2147483647,
            'min_length': 1,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'user_name': (str,),  # noqa: E501
            'email_address': (str,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'gender': (str,),  # noqa: E501
            'language': (str,),  # noqa: E501
            'user_group_ids': ([str],),  # noqa: E501
            'license_type': (str,),  # noqa: E501
            'addresses': ([Address],),  # noqa: E501
            'phones': ([PhoneNumber],),  # noqa: E501
            'additional_email_addresses': ([Email],),  # noqa: E501
            'instant_messaging_accounts': ([InstantMessagingAccount],),  # noqa: E501
            'websites': ([Website],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'user_name': 'userName',  # noqa: E501
        'email_address': 'emailAddress',  # noqa: E501
        'first_name': 'firstName',  # noqa: E501
        'last_name': 'lastName',  # noqa: E501
        'gender': 'gender',  # noqa: E501
        'language': 'language',  # noqa: E501
        'user_group_ids': 'userGroupIds',  # noqa: E501
        'license_type': 'licenseType',  # noqa: E501
        'addresses': 'addresses',  # noqa: E501
        'phones': 'phones',  # noqa: E501
        'additional_email_addresses': 'additionalEmailAddresses',  # noqa: E501
        'instant_messaging_accounts': 'instantMessagingAccounts',  # noqa: E501
        'websites': 'websites',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, user_name, email_address, *args, **kwargs):  # noqa: E501
        """AddUserRequest - a model defined in OpenAPI

        Args:
            user_name (str): The username, which should be unique
            email_address (str): The e-mail address of the new user

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            first_name (str): The first name of the new user. [optional]  # noqa: E501
            last_name (str): The last name of the new user. [optional]  # noqa: E501
            gender (str): The gender of the user. [optional]  # noqa: E501
            language (str): The language for the user. [optional]  # noqa: E501
            user_group_ids ([str]): The groups this newly created user should be added to. [optional]  # noqa: E501
            license_type (str): The license type of the user. LicenseType will be removed in the future.. [optional]  # noqa: E501
            addresses ([Address]): The postal addresses of the user. [optional]  # noqa: E501
            phones ([PhoneNumber]): The phone numbers of the user. [optional]  # noqa: E501
            additional_email_addresses ([Email]): The additional e-mail addresses of the user. [optional]  # noqa: E501
            instant_messaging_accounts ([InstantMessagingAccount]): The instant messaging accounts of the user. [optional]  # noqa: E501
            websites ([Website]): The websites of the user. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.user_name = user_name
        self.email_address = email_address
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)