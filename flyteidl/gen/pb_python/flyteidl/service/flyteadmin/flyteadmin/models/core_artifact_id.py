# coding: utf-8

"""
    flyteidl/service/admin.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flyteadmin.models.core_artifact_key import CoreArtifactKey  # noqa: F401,E501
from flyteadmin.models.core_partitions import CorePartitions  # noqa: F401,E501


class CoreArtifactID(object):
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
        'artifact_key': 'CoreArtifactKey',
        'version': 'str',
        'partitions': 'CorePartitions'
    }

    attribute_map = {
        'artifact_key': 'artifact_key',
        'version': 'version',
        'partitions': 'partitions'
    }

    def __init__(self, artifact_key=None, version=None, partitions=None):  # noqa: E501
        """CoreArtifactID - a model defined in Swagger"""  # noqa: E501

        self._artifact_key = None
        self._version = None
        self._partitions = None
        self.discriminator = None

        if artifact_key is not None:
            self.artifact_key = artifact_key
        if version is not None:
            self.version = version
        if partitions is not None:
            self.partitions = partitions

    @property
    def artifact_key(self):
        """Gets the artifact_key of this CoreArtifactID.  # noqa: E501


        :return: The artifact_key of this CoreArtifactID.  # noqa: E501
        :rtype: CoreArtifactKey
        """
        return self._artifact_key

    @artifact_key.setter
    def artifact_key(self, artifact_key):
        """Sets the artifact_key of this CoreArtifactID.


        :param artifact_key: The artifact_key of this CoreArtifactID.  # noqa: E501
        :type: CoreArtifactKey
        """

        self._artifact_key = artifact_key

    @property
    def version(self):
        """Gets the version of this CoreArtifactID.  # noqa: E501


        :return: The version of this CoreArtifactID.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CoreArtifactID.


        :param version: The version of this CoreArtifactID.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def partitions(self):
        """Gets the partitions of this CoreArtifactID.  # noqa: E501


        :return: The partitions of this CoreArtifactID.  # noqa: E501
        :rtype: CorePartitions
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this CoreArtifactID.


        :param partitions: The partitions of this CoreArtifactID.  # noqa: E501
        :type: CorePartitions
        """

        self._partitions = partitions

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
        if issubclass(CoreArtifactID, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CoreArtifactID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
