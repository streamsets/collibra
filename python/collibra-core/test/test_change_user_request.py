"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import collibra_core
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
from collibra_core.model.change_user_request import ChangeUserRequest


class TestChangeUserRequest(unittest.TestCase):
    """ChangeUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChangeUserRequest(self):
        """Test ChangeUserRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ChangeUserRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
