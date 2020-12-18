# coding: utf-8

"""
    Registry of Open Community Challenge API

    The OpenAPI specification implemented by the Challenge Registries. # Introduction TBA   # noqa: E501

    The version of the OpenAPI document: 0.1.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from roccclient.configuration import Configuration


class ChallengeFilter(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'status': 'ChallengeStatus',
        'organizer': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'organizer': 'organizer',
        'tag': 'tag'
    }

    def __init__(self, name=None, status=None, organizer=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """ChallengeFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._status = None
        self._organizer = None
        self._tag = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if organizer is not None:
            self.organizer = organizer
        if tag is not None:
            self.tag = tag

    @property
    def name(self):
        """Gets the name of this ChallengeFilter.  # noqa: E501

        Keep the challenges whose name include this term  # noqa: E501

        :return: The name of this ChallengeFilter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChallengeFilter.

        Keep the challenges whose name include this term  # noqa: E501

        :param name: The name of this ChallengeFilter.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this ChallengeFilter.  # noqa: E501


        :return: The status of this ChallengeFilter.  # noqa: E501
        :rtype: ChallengeStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChallengeFilter.


        :param status: The status of this ChallengeFilter.  # noqa: E501
        :type status: ChallengeStatus
        """

        self._status = status

    @property
    def organizer(self):
        """Gets the organizer of this ChallengeFilter.  # noqa: E501

        Keep the challenges organized by this person  # noqa: E501

        :return: The organizer of this ChallengeFilter.  # noqa: E501
        :rtype: str
        """
        return self._organizer

    @organizer.setter
    def organizer(self, organizer):
        """Sets the organizer of this ChallengeFilter.

        Keep the challenges organized by this person  # noqa: E501

        :param organizer: The organizer of this ChallengeFilter.  # noqa: E501
        :type organizer: str
        """

        self._organizer = organizer

    @property
    def tag(self):
        """Gets the tag of this ChallengeFilter.  # noqa: E501

        Keep the challenges associated to this tag  # noqa: E501

        :return: The tag of this ChallengeFilter.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ChallengeFilter.

        Keep the challenges associated to this tag  # noqa: E501

        :param tag: The tag of this ChallengeFilter.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChallengeFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChallengeFilter):
            return True

        return self.to_dict() != other.to_dict()
