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

from swagger_client.models.provenance_searchable_field_dto import ProvenanceSearchableFieldDTO  # noqa: F401,E501


class ProvenanceOptionsDTO(object):
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
        'searchable_fields': 'list[ProvenanceSearchableFieldDTO]'
    }

    attribute_map = {
        'searchable_fields': 'searchableFields'
    }

    def __init__(self, searchable_fields=None):  # noqa: E501
        """ProvenanceOptionsDTO - a model defined in Swagger"""  # noqa: E501

        self._searchable_fields = None
        self.discriminator = None

        if searchable_fields is not None:
            self.searchable_fields = searchable_fields

    @property
    def searchable_fields(self):
        """Gets the searchable_fields of this ProvenanceOptionsDTO.  # noqa: E501

        The available searchable field for the NiFi.  # noqa: E501

        :return: The searchable_fields of this ProvenanceOptionsDTO.  # noqa: E501
        :rtype: list[ProvenanceSearchableFieldDTO]
        """
        return self._searchable_fields

    @searchable_fields.setter
    def searchable_fields(self, searchable_fields):
        """Sets the searchable_fields of this ProvenanceOptionsDTO.

        The available searchable field for the NiFi.  # noqa: E501

        :param searchable_fields: The searchable_fields of this ProvenanceOptionsDTO.  # noqa: E501
        :type: list[ProvenanceSearchableFieldDTO]
        """

        self._searchable_fields = searchable_fields

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
        if not isinstance(other, ProvenanceOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other