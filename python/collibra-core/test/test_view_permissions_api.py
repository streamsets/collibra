"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import collibra_core
from collibra_core.api.view_permissions_api import ViewPermissionsApi  # noqa: E501


class TestViewPermissionsApi(unittest.TestCase):
    """ViewPermissionsApi unit test stubs"""

    def setUp(self):
        self.api = ViewPermissionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_view_permission(self):
        """Test case for add_view_permission

        Adds a view permission.  # noqa: E501
        """
        pass

    def test_find_view_permissions(self):
        """Test case for find_view_permissions

        Finds view permissions with given criteria.  # noqa: E501
        """
        pass

    def test_get_view_permission(self):
        """Test case for get_view_permission

        Retrieves a view permission.  # noqa: E501
        """
        pass

    def test_remove_view_permission(self):
        """Test case for remove_view_permission

        Removes a view permission.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
