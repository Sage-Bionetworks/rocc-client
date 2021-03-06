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
import datetime

import roccclient
from roccclient.models.person_create_request import PersonCreateRequest  # noqa: E501
from roccclient.rest import ApiException

class TestPersonCreateRequest(unittest.TestCase):
    """PersonCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PersonCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = roccclient.models.person_create_request.PersonCreateRequest()  # noqa: E501
        if include_optional :
            return PersonCreateRequest(
                first_name = '0', 
                last_name = '0', 
                email = 'john.smith@example.com', 
                organizations = [
                    'awesome-organization'
                    ]
            )
        else :
            return PersonCreateRequest(
                first_name = '0',
                last_name = '0',
                email = 'john.smith@example.com',
        )

    def testPersonCreateRequest(self):
        """Test PersonCreateRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
