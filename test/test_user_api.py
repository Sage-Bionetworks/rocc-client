# coding: utf-8

"""
    Registry of Open Community Challenge API

    The OpenAPI specification implemented by the Challenge Registries. # Introduction TBA   # noqa: E501

    The version of the OpenAPI document: 0.1.4
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import roccclient
from roccclient.api.user_api import UserApi  # noqa: E501
from roccclient.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = roccclient.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a user  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete a user  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get a user  # noqa: E501
        """
        pass

    def test_list_users(self):
        """Test case for list_users

        Get all users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
