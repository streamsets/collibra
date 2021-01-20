"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import collibra_core
from collibra_core.api.jobs_api import JobsApi  # noqa: E501


class TestJobsApi(unittest.TestCase):
    """JobsApi unit test stubs"""

    def setUp(self):
        self.api = JobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_job(self):
        """Test case for cancel_job

        Cancels given Job.  # noqa: E501
        """
        pass

    def test_get_job(self):
        """Test case for get_job

        Returns the Job identified by the given UUID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
