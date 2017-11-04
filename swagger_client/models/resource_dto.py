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


class ResourceDTO(object):
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
        'identifier': 'str',
        'name': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name'
    }

    def __init__(self, identifier=None, name=None):  # noqa: E501
        """ResourceDTO - a model defined in Swagger"""  # noqa: E501

        self._identifier = None
        self._name = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if name is not None:
            self.name = name

    @property
    def identifier(self):
        """Gets the identifier of this ResourceDTO.  # noqa: E501

        The identifier of the resource.  # noqa: E501

        :return: The identifier of this ResourceDTO.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ResourceDTO.

        The identifier of the resource.  # noqa: E501

        :param identifier: The identifier of this ResourceDTO.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this ResourceDTO.  # noqa: E501

        The name of the resource.  # noqa: E501

        :return: The name of this ResourceDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceDTO.

        The name of the resource.  # noqa: E501

        :param name: The name of this ResourceDTO.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, ResourceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
