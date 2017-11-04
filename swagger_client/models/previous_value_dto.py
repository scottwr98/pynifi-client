# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.  # noqa: E501

    OpenAPI spec version: 1.4.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PreviousValueDTO(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'previous_value': 'str',
        'timestamp': 'str',
        'user_identity': 'str'
    }

    attribute_map = {
        'previous_value': 'previousValue',
        'timestamp': 'timestamp',
        'user_identity': 'userIdentity'
    }

    def __init__(self, previous_value=None, timestamp=None, user_identity=None):  # noqa: E501
        """PreviousValueDTO - a model defined in Swagger"""  # noqa: E501

        self._previous_value = None
        self._timestamp = None
        self._user_identity = None
        self.discriminator = None

        if previous_value is not None:
            self.previous_value = previous_value
        if timestamp is not None:
            self.timestamp = timestamp
        if user_identity is not None:
            self.user_identity = user_identity

    @property
    def previous_value(self):
        """Gets the previous_value of this PreviousValueDTO.  # noqa: E501

        The previous value.  # noqa: E501

        :return: The previous_value of this PreviousValueDTO.  # noqa: E501
        :rtype: str
        """
        return self._previous_value

    @previous_value.setter
    def previous_value(self, previous_value):
        """Sets the previous_value of this PreviousValueDTO.

        The previous value.  # noqa: E501

        :param previous_value: The previous_value of this PreviousValueDTO.  # noqa: E501
        :type: str
        """

        self._previous_value = previous_value

    @property
    def timestamp(self):
        """Gets the timestamp of this PreviousValueDTO.  # noqa: E501

        The timestamp when the value was modified.  # noqa: E501

        :return: The timestamp of this PreviousValueDTO.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PreviousValueDTO.

        The timestamp when the value was modified.  # noqa: E501

        :param timestamp: The timestamp of this PreviousValueDTO.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def user_identity(self):
        """Gets the user_identity of this PreviousValueDTO.  # noqa: E501

        The user who changed the previous value.  # noqa: E501

        :return: The user_identity of this PreviousValueDTO.  # noqa: E501
        :rtype: str
        """
        return self._user_identity

    @user_identity.setter
    def user_identity(self, user_identity):
        """Sets the user_identity of this PreviousValueDTO.

        The user who changed the previous value.  # noqa: E501

        :param user_identity: The user_identity of this PreviousValueDTO.  # noqa: E501
        :type: str
        """

        self._user_identity = user_identity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, PreviousValueDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
