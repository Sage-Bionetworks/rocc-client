# coding: utf-8

"""
    Registry of Open Community Challenge API

    The OpenAPI specification implemented by the Challenge Registries. # Introduction TBA   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import roccclient
from roccclient.api.challenge_api import ChallengeApi  # noqa: E501
from roccclient.rest import ApiException


class TestChallengeApi(unittest.TestCase):
    """ChallengeApi unit test stubs"""

    def setUp(self):
        self.api = roccclient.api.challenge_api.ChallengeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_challenge(self):
        """Test case for create_challenge

        Add a challenge  # noqa: E501
        """
        pass

    def test_delete_challenge(self):
        """Test case for delete_challenge

        Delete a challenge  # noqa: E501
        """
        pass

    def test_get_challenge(self):
        """Test case for get_challenge

        Get a challenge  # noqa: E501
        """
        pass

    def test_list_challenges(self):
        """Test case for list_challenges

        List all the challenges  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
