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

from pynifi_client.models.bundle_dto import BundleDTO  # noqa: F401,E501
from pynifi_client.models.controller_service_api_dto import ControllerServiceApiDTO  # noqa: F401,E501
from pynifi_client.models.controller_service_referencing_component_entity import ControllerServiceReferencingComponentEntity  # noqa: F401,E501
from pynifi_client.models.position_dto import PositionDTO  # noqa: F401,E501
from pynifi_client.models.property_descriptor_dto import PropertyDescriptorDTO  # noqa: F401,E501


class ControllerServiceDTO(object):
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
        'id': 'str',
        'parent_group_id': 'str',
        'position': 'PositionDTO',
        'name': 'str',
        'type': 'str',
        'bundle': 'BundleDTO',
        'controller_service_apis': 'list[ControllerServiceApiDTO]',
        'comments': 'str',
        'state': 'str',
        'persists_state': 'bool',
        'restricted': 'bool',
        'deprecated': 'bool',
        'multiple_versions_available': 'bool',
        'properties': 'dict(str, str)',
        'descriptors': 'dict(str, PropertyDescriptorDTO)',
        'custom_ui_url': 'str',
        'annotation_data': 'str',
        'referencing_components': 'list[ControllerServiceReferencingComponentEntity]',
        'validation_errors': 'list[str]',
        'extension_missing': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'name': 'name',
        'type': 'type',
        'bundle': 'bundle',
        'controller_service_apis': 'controllerServiceApis',
        'comments': 'comments',
        'state': 'state',
        'persists_state': 'persistsState',
        'restricted': 'restricted',
        'deprecated': 'deprecated',
        'multiple_versions_available': 'multipleVersionsAvailable',
        'properties': 'properties',
        'descriptors': 'descriptors',
        'custom_ui_url': 'customUiUrl',
        'annotation_data': 'annotationData',
        'referencing_components': 'referencingComponents',
        'validation_errors': 'validationErrors',
        'extension_missing': 'extensionMissing'
    }

    def __init__(self, id=None, parent_group_id=None, position=None, name=None, type=None, bundle=None, controller_service_apis=None, comments=None, state=None, persists_state=False, restricted=False, deprecated=False, multiple_versions_available=False, properties=None, descriptors=None, custom_ui_url=None, annotation_data=None, referencing_components=None, validation_errors=None, extension_missing=False):  # noqa: E501
        """ControllerServiceDTO - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._parent_group_id = None
        self._position = None
        self._name = None
        self._type = None
        self._bundle = None
        self._controller_service_apis = None
        self._comments = None
        self._state = None
        self._persists_state = None
        self._restricted = None
        self._deprecated = None
        self._multiple_versions_available = None
        self._properties = None
        self._descriptors = None
        self._custom_ui_url = None
        self._annotation_data = None
        self._referencing_components = None
        self._validation_errors = None
        self._extension_missing = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_group_id is not None:
            self.parent_group_id = parent_group_id
        if position is not None:
            self.position = position
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if bundle is not None:
            self.bundle = bundle
        if controller_service_apis is not None:
            self.controller_service_apis = controller_service_apis
        if comments is not None:
            self.comments = comments
        if state is not None:
            self.state = state
        if persists_state is not None:
            self.persists_state = persists_state
        if restricted is not None:
            self.restricted = restricted
        if deprecated is not None:
            self.deprecated = deprecated
        if multiple_versions_available is not None:
            self.multiple_versions_available = multiple_versions_available
        if properties is not None:
            self.properties = properties
        if descriptors is not None:
            self.descriptors = descriptors
        if custom_ui_url is not None:
            self.custom_ui_url = custom_ui_url
        if annotation_data is not None:
            self.annotation_data = annotation_data
        if referencing_components is not None:
            self.referencing_components = referencing_components
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if extension_missing is not None:
            self.extension_missing = extension_missing

    @property
    def id(self):
        """Gets the id of this ControllerServiceDTO.  # noqa: E501

        The id of the component.  # noqa: E501

        :return: The id of this ControllerServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ControllerServiceDTO.

        The id of the component.  # noqa: E501

        :param id: The id of this ControllerServiceDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parent_group_id(self):
        """Gets the parent_group_id of this ControllerServiceDTO.  # noqa: E501

        The id of parent process group of this component if applicable.  # noqa: E501

        :return: The parent_group_id of this ControllerServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """Sets the parent_group_id of this ControllerServiceDTO.

        The id of parent process group of this component if applicable.  # noqa: E501

        :param parent_group_id: The parent_group_id of this ControllerServiceDTO.  # noqa: E501
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """Gets the position of this ControllerServiceDTO.  # noqa: E501

        The position of this component in the UI if applicable.  # noqa: E501

        :return: The position of this ControllerServiceDTO.  # noqa: E501
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ControllerServiceDTO.

        The position of this component in the UI if applicable.  # noqa: E501

        :param position: The position of this ControllerServiceDTO.  # noqa: E501
        :type: PositionDTO
        """

        self._position = position

    @property
    def name(self):
        """Gets the name of this ControllerServiceDTO.  # noqa: E501

        The name of the controller service.  # noqa: E501

        :return: The name of this ControllerServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ControllerServiceDTO.

        The name of the controller service.  # noqa: E501

        :param name: The name of this ControllerServiceDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ControllerServiceDTO.  # noqa: E501

        The type of the controller service.  # noqa: E501

        :return: The type of this ControllerServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ControllerServiceDTO.

        The type of the controller service.  # noqa: E501

        :param type: The type of this ControllerServiceDTO.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def bundle(self):
        """Gets the bundle of this ControllerServiceDTO.  # noqa: E501

        The details of the artifact that bundled this processor type.  # noqa: E501

        :return: The bundle of this ControllerServiceDTO.  # noqa: E501
        :rtype: BundleDTO
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle):
        """Sets the bundle of this ControllerServiceDTO.

        The details of the artifact that bundled this processor type.  # noqa: E501

        :param bundle: The bundle of this ControllerServiceDTO.  # noqa: E501
        :type: BundleDTO
        """

        self._bundle = bundle

    @property
    def controller_service_apis(self):
        """Gets the controller_service_apis of this ControllerServiceDTO.  # noqa: E501

        Lists the APIs this Controller Service implements.  # noqa: E501

        :return: The controller_service_apis of this ControllerServiceDTO.  # noqa: E501
        :rtype: list[ControllerServiceApiDTO]
        """
        return self._controller_service_apis

    @controller_service_apis.setter
    def controller_service_apis(self, controller_service_apis):
        """Sets the controller_service_apis of this ControllerServiceDTO.

        Lists the APIs this Controller Service implements.  # noqa: E501

        :param controller_service_apis: The controller_service_apis of this ControllerServiceDTO.  # noqa: E501
        :type: list[ControllerServiceApiDTO]
        """

        self._controller_service_apis = controller_service_apis

    @property
    def comments(self):
        """Gets the comments of this ControllerServiceDTO.  # noqa: E501

        The comments for the controller service.  # noqa: E501

        :return: The comments of this ControllerServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ControllerServiceDTO.

        The comments for the controller service.  # noqa: E501

        :param comments: The comments of this ControllerServiceDTO.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def state(self):
        """Gets the state of this ControllerServiceDTO.  # noqa: E501

        The state of the controller service.  # noqa: E501

        :return: The state of this ControllerServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ControllerServiceDTO.

        The state of the controller service.  # noqa: E501

        :param state: The state of this ControllerServiceDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENABLED", "ENABLING", "DISABLED", "DISABLING"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def persists_state(self):
        """Gets the persists_state of this ControllerServiceDTO.  # noqa: E501

        Whether the controller service persists state.  # noqa: E501

        :return: The persists_state of this ControllerServiceDTO.  # noqa: E501
        :rtype: bool
        """
        return self._persists_state

    @persists_state.setter
    def persists_state(self, persists_state):
        """Sets the persists_state of this ControllerServiceDTO.

        Whether the controller service persists state.  # noqa: E501

        :param persists_state: The persists_state of this ControllerServiceDTO.  # noqa: E501
        :type: bool
        """

        self._persists_state = persists_state

    @property
    def restricted(self):
        """Gets the restricted of this ControllerServiceDTO.  # noqa: E501

        Whether the controller service requires elevated privileges.  # noqa: E501

        :return: The restricted of this ControllerServiceDTO.  # noqa: E501
        :rtype: bool
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """Sets the restricted of this ControllerServiceDTO.

        Whether the controller service requires elevated privileges.  # noqa: E501

        :param restricted: The restricted of this ControllerServiceDTO.  # noqa: E501
        :type: bool
        """

        self._restricted = restricted

    @property
    def deprecated(self):
        """Gets the deprecated of this ControllerServiceDTO.  # noqa: E501

        Whether the ontroller service has been deprecated.  # noqa: E501

        :return: The deprecated of this ControllerServiceDTO.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this ControllerServiceDTO.

        Whether the ontroller service has been deprecated.  # noqa: E501

        :param deprecated: The deprecated of this ControllerServiceDTO.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def multiple_versions_available(self):
        """Gets the multiple_versions_available of this ControllerServiceDTO.  # noqa: E501

        Whether the controller service has multiple versions available.  # noqa: E501

        :return: The multiple_versions_available of this ControllerServiceDTO.  # noqa: E501
        :rtype: bool
        """
        return self._multiple_versions_available

    @multiple_versions_available.setter
    def multiple_versions_available(self, multiple_versions_available):
        """Sets the multiple_versions_available of this ControllerServiceDTO.

        Whether the controller service has multiple versions available.  # noqa: E501

        :param multiple_versions_available: The multiple_versions_available of this ControllerServiceDTO.  # noqa: E501
        :type: bool
        """

        self._multiple_versions_available = multiple_versions_available

    @property
    def properties(self):
        """Gets the properties of this ControllerServiceDTO.  # noqa: E501

        The properties of the controller service.  # noqa: E501

        :return: The properties of this ControllerServiceDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ControllerServiceDTO.

        The properties of the controller service.  # noqa: E501

        :param properties: The properties of this ControllerServiceDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def descriptors(self):
        """Gets the descriptors of this ControllerServiceDTO.  # noqa: E501

        The descriptors for the controller service properties.  # noqa: E501

        :return: The descriptors of this ControllerServiceDTO.  # noqa: E501
        :rtype: dict(str, PropertyDescriptorDTO)
        """
        return self._descriptors

    @descriptors.setter
    def descriptors(self, descriptors):
        """Sets the descriptors of this ControllerServiceDTO.

        The descriptors for the controller service properties.  # noqa: E501

        :param descriptors: The descriptors of this ControllerServiceDTO.  # noqa: E501
        :type: dict(str, PropertyDescriptorDTO)
        """

        self._descriptors = descriptors

    @property
    def custom_ui_url(self):
        """Gets the custom_ui_url of this ControllerServiceDTO.  # noqa: E501

        The URL for the controller services custom configuration UI if applicable.  # noqa: E501

        :return: The custom_ui_url of this ControllerServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._custom_ui_url

    @custom_ui_url.setter
    def custom_ui_url(self, custom_ui_url):
        """Sets the custom_ui_url of this ControllerServiceDTO.

        The URL for the controller services custom configuration UI if applicable.  # noqa: E501

        :param custom_ui_url: The custom_ui_url of this ControllerServiceDTO.  # noqa: E501
        :type: str
        """

        self._custom_ui_url = custom_ui_url

    @property
    def annotation_data(self):
        """Gets the annotation_data of this ControllerServiceDTO.  # noqa: E501

        The annotation for the controller service. This is how the custom UI relays configuration to the controller service.  # noqa: E501

        :return: The annotation_data of this ControllerServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._annotation_data

    @annotation_data.setter
    def annotation_data(self, annotation_data):
        """Sets the annotation_data of this ControllerServiceDTO.

        The annotation for the controller service. This is how the custom UI relays configuration to the controller service.  # noqa: E501

        :param annotation_data: The annotation_data of this ControllerServiceDTO.  # noqa: E501
        :type: str
        """

        self._annotation_data = annotation_data

    @property
    def referencing_components(self):
        """Gets the referencing_components of this ControllerServiceDTO.  # noqa: E501

        All components referencing this controller service.  # noqa: E501

        :return: The referencing_components of this ControllerServiceDTO.  # noqa: E501
        :rtype: list[ControllerServiceReferencingComponentEntity]
        """
        return self._referencing_components

    @referencing_components.setter
    def referencing_components(self, referencing_components):
        """Sets the referencing_components of this ControllerServiceDTO.

        All components referencing this controller service.  # noqa: E501

        :param referencing_components: The referencing_components of this ControllerServiceDTO.  # noqa: E501
        :type: list[ControllerServiceReferencingComponentEntity]
        """

        self._referencing_components = referencing_components

    @property
    def validation_errors(self):
        """Gets the validation_errors of this ControllerServiceDTO.  # noqa: E501

        The validation errors from the controller service. These validation errors represent the problems with the controller service that must be resolved before it can be enabled.  # noqa: E501

        :return: The validation_errors of this ControllerServiceDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this ControllerServiceDTO.

        The validation errors from the controller service. These validation errors represent the problems with the controller service that must be resolved before it can be enabled.  # noqa: E501

        :param validation_errors: The validation_errors of this ControllerServiceDTO.  # noqa: E501
        :type: list[str]
        """

        self._validation_errors = validation_errors

    @property
    def extension_missing(self):
        """Gets the extension_missing of this ControllerServiceDTO.  # noqa: E501

        Whether the underlying extension is missing.  # noqa: E501

        :return: The extension_missing of this ControllerServiceDTO.  # noqa: E501
        :rtype: bool
        """
        return self._extension_missing

    @extension_missing.setter
    def extension_missing(self, extension_missing):
        """Sets the extension_missing of this ControllerServiceDTO.

        Whether the underlying extension is missing.  # noqa: E501

        :param extension_missing: The extension_missing of this ControllerServiceDTO.  # noqa: E501
        :type: bool
        """

        self._extension_missing = extension_missing

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
        if not isinstance(other, ControllerServiceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
