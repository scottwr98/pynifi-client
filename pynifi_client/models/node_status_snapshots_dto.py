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

from pynifi_client.models.status_snapshot_dto import StatusSnapshotDTO  # noqa: F401,E501


class NodeStatusSnapshotsDTO(object):
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
        'node_id': 'str',
        'address': 'str',
        'api_port': 'int',
        'status_snapshots': 'list[StatusSnapshotDTO]'
    }

    attribute_map = {
        'node_id': 'nodeId',
        'address': 'address',
        'api_port': 'apiPort',
        'status_snapshots': 'statusSnapshots'
    }

    def __init__(self, node_id=None, address=None, api_port=None, status_snapshots=None):  # noqa: E501
        """NodeStatusSnapshotsDTO - a model defined in Swagger"""  # noqa: E501

        self._node_id = None
        self._address = None
        self._api_port = None
        self._status_snapshots = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if address is not None:
            self.address = address
        if api_port is not None:
            self.api_port = api_port
        if status_snapshots is not None:
            self.status_snapshots = status_snapshots

    @property
    def node_id(self):
        """Gets the node_id of this NodeStatusSnapshotsDTO.  # noqa: E501

        The id of the node.  # noqa: E501

        :return: The node_id of this NodeStatusSnapshotsDTO.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this NodeStatusSnapshotsDTO.

        The id of the node.  # noqa: E501

        :param node_id: The node_id of this NodeStatusSnapshotsDTO.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def address(self):
        """Gets the address of this NodeStatusSnapshotsDTO.  # noqa: E501

        The node's host/ip address.  # noqa: E501

        :return: The address of this NodeStatusSnapshotsDTO.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this NodeStatusSnapshotsDTO.

        The node's host/ip address.  # noqa: E501

        :param address: The address of this NodeStatusSnapshotsDTO.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def api_port(self):
        """Gets the api_port of this NodeStatusSnapshotsDTO.  # noqa: E501

        The port the node is listening for API requests.  # noqa: E501

        :return: The api_port of this NodeStatusSnapshotsDTO.  # noqa: E501
        :rtype: int
        """
        return self._api_port

    @api_port.setter
    def api_port(self, api_port):
        """Sets the api_port of this NodeStatusSnapshotsDTO.

        The port the node is listening for API requests.  # noqa: E501

        :param api_port: The api_port of this NodeStatusSnapshotsDTO.  # noqa: E501
        :type: int
        """

        self._api_port = api_port

    @property
    def status_snapshots(self):
        """Gets the status_snapshots of this NodeStatusSnapshotsDTO.  # noqa: E501

        A list of StatusSnapshotDTO objects that provide the actual metric values for the component for this node.  # noqa: E501

        :return: The status_snapshots of this NodeStatusSnapshotsDTO.  # noqa: E501
        :rtype: list[StatusSnapshotDTO]
        """
        return self._status_snapshots

    @status_snapshots.setter
    def status_snapshots(self, status_snapshots):
        """Sets the status_snapshots of this NodeStatusSnapshotsDTO.

        A list of StatusSnapshotDTO objects that provide the actual metric values for the component for this node.  # noqa: E501

        :param status_snapshots: The status_snapshots of this NodeStatusSnapshotsDTO.  # noqa: E501
        :type: list[StatusSnapshotDTO]
        """

        self._status_snapshots = status_snapshots

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
        if not isinstance(other, NodeStatusSnapshotsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other