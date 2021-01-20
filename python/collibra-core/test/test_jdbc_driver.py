"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import collibra_core
from collibra_core.model.connection_string_parameter import ConnectionStringParameter
from collibra_core.model.jdbc_driver_file import JdbcDriverFile
globals()['ConnectionStringParameter'] = ConnectionStringParameter
globals()['JdbcDriverFile'] = JdbcDriverFile
from collibra_core.model.jdbc_driver import JdbcDriver


class TestJdbcDriver(unittest.TestCase):
    """JdbcDriver unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJdbcDriver(self):
        """Test JdbcDriver"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JdbcDriver()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()