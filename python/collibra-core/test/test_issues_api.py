"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import collibra_core
from collibra_core.api.issues_api import IssuesApi  # noqa: E501


class TestIssuesApi(unittest.TestCase):
    """IssuesApi unit test stubs"""

    def setUp(self):
        self.api = IssuesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_issue(self):
        """Test case for add_issue

        Adds a new issue.  # noqa: E501
        """
        pass

    def test_find_issues(self):
        """Test case for find_issues

        Returns issues matching the given search criteria.  # noqa: E501
        """
        pass

    def test_move_issue(self):
        """Test case for move_issue

        Moves an issue to another community.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
