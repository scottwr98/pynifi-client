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

from swagger_client.models.variable_entity import VariableEntity  # noqa: F401,E501


class VariableRegistryDTO(object):
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
        'variables': 'list[VariableEntity]',
        'process_group_id': 'str'
    }

    attribute_map = {
        'variables': 'variables',
        'process_group_id': 'processGroupId'
    }

    def __init__(self, variables=None, process_group_id=None):  # noqa: E501
        """VariableRegistryDTO - a model defined in Swagger"""  # noqa: E501

        self._variables = None
        self._process_group_id = None
        self.discriminator = None

        if variables is not None:
            self.variables = variables
        if process_group_id is not None:
            self.process_group_id = process_group_id

    @property
    def variables(self):
        """Gets the variables of this VariableRegistryDTO.  # noqa: E501

        The variables that are available in this Variable Registry  # noqa: E501

        :return: The variables of this VariableRegistryDTO.  # noqa: E501
        :rtype: list[VariableEntity]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this VariableRegistryDTO.

        The variables that are available in this Variable Registry  # noqa: E501

        :param variables: The variables of this VariableRegistryDTO.  # noqa: E501
        :type: list[VariableEntity]
        """

        self._variables = variables

    @property
    def process_group_id(self):
        """Gets the process_group_id of this VariableRegistryDTO.  # noqa: E501

        The UUID of the Process Group that this Variable Registry belongs to  # noqa: E501

        :return: The process_group_id of this VariableRegistryDTO.  # noqa: E501
        :rtype: str
        """
        return self._process_group_id

    @process_group_id.setter
    def process_group_id(self, process_group_id):
        """Sets the process_group_id of this VariableRegistryDTO.

        The UUID of the Process Group that this Variable Registry belongs to  # noqa: E501

        :param process_group_id: The process_group_id of this VariableRegistryDTO.  # noqa: E501
        :type: str
        """

        self._process_group_id = process_group_id

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
        if not isinstance(other, VariableRegistryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
