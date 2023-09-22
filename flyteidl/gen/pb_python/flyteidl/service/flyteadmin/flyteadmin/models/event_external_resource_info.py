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

from flyteadmin.models.core_catalog_cache_status import CoreCatalogCacheStatus  # noqa: F401,E501
from flyteadmin.models.core_task_execution_phase import CoreTaskExecutionPhase  # noqa: F401,E501
from flyteadmin.models.core_task_log import CoreTaskLog  # noqa: F401,E501


class EventExternalResourceInfo(object):
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
        'external_id': 'str',
        'index': 'int',
        'retry_attempt': 'int',
        'phase': 'CoreTaskExecutionPhase',
        'cache_status': 'CoreCatalogCacheStatus',
        'logs': 'list[CoreTaskLog]'
    }

    attribute_map = {
        'external_id': 'external_id',
        'index': 'index',
        'retry_attempt': 'retry_attempt',
        'phase': 'phase',
        'cache_status': 'cache_status',
        'logs': 'logs'
    }

    def __init__(self, external_id=None, index=None, retry_attempt=None, phase=None, cache_status=None, logs=None):  # noqa: E501
        """EventExternalResourceInfo - a model defined in Swagger"""  # noqa: E501

        self._external_id = None
        self._index = None
        self._retry_attempt = None
        self._phase = None
        self._cache_status = None
        self._logs = None
        self.discriminator = None

        if external_id is not None:
            self.external_id = external_id
        if index is not None:
            self.index = index
        if retry_attempt is not None:
            self.retry_attempt = retry_attempt
        if phase is not None:
            self.phase = phase
        if cache_status is not None:
            self.cache_status = cache_status
        if logs is not None:
            self.logs = logs

    @property
    def external_id(self):
        """Gets the external_id of this EventExternalResourceInfo.  # noqa: E501

        Identifier for an external resource created by this task execution, for example Qubole query ID or presto query ids.  # noqa: E501

        :return: The external_id of this EventExternalResourceInfo.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this EventExternalResourceInfo.

        Identifier for an external resource created by this task execution, for example Qubole query ID or presto query ids.  # noqa: E501

        :param external_id: The external_id of this EventExternalResourceInfo.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def index(self):
        """Gets the index of this EventExternalResourceInfo.  # noqa: E501

        A unique index for the external resource with respect to all external resources for this task. Although the identifier may change between task reporting events or retries, this will remain the same to enable aggregating information from multiple reports.  # noqa: E501

        :return: The index of this EventExternalResourceInfo.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this EventExternalResourceInfo.

        A unique index for the external resource with respect to all external resources for this task. Although the identifier may change between task reporting events or retries, this will remain the same to enable aggregating information from multiple reports.  # noqa: E501

        :param index: The index of this EventExternalResourceInfo.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def retry_attempt(self):
        """Gets the retry_attempt of this EventExternalResourceInfo.  # noqa: E501


        :return: The retry_attempt of this EventExternalResourceInfo.  # noqa: E501
        :rtype: int
        """
        return self._retry_attempt

    @retry_attempt.setter
    def retry_attempt(self, retry_attempt):
        """Sets the retry_attempt of this EventExternalResourceInfo.


        :param retry_attempt: The retry_attempt of this EventExternalResourceInfo.  # noqa: E501
        :type: int
        """

        self._retry_attempt = retry_attempt

    @property
    def phase(self):
        """Gets the phase of this EventExternalResourceInfo.  # noqa: E501


        :return: The phase of this EventExternalResourceInfo.  # noqa: E501
        :rtype: CoreTaskExecutionPhase
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this EventExternalResourceInfo.


        :param phase: The phase of this EventExternalResourceInfo.  # noqa: E501
        :type: CoreTaskExecutionPhase
        """

        self._phase = phase

    @property
    def cache_status(self):
        """Gets the cache_status of this EventExternalResourceInfo.  # noqa: E501

        Captures the status of caching for this external resource execution.  # noqa: E501

        :return: The cache_status of this EventExternalResourceInfo.  # noqa: E501
        :rtype: CoreCatalogCacheStatus
        """
        return self._cache_status

    @cache_status.setter
    def cache_status(self, cache_status):
        """Sets the cache_status of this EventExternalResourceInfo.

        Captures the status of caching for this external resource execution.  # noqa: E501

        :param cache_status: The cache_status of this EventExternalResourceInfo.  # noqa: E501
        :type: CoreCatalogCacheStatus
        """

        self._cache_status = cache_status

    @property
    def logs(self):
        """Gets the logs of this EventExternalResourceInfo.  # noqa: E501


        :return: The logs of this EventExternalResourceInfo.  # noqa: E501
        :rtype: list[CoreTaskLog]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this EventExternalResourceInfo.


        :param logs: The logs of this EventExternalResourceInfo.  # noqa: E501
        :type: list[CoreTaskLog]
        """

        self._logs = logs

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
        if issubclass(EventExternalResourceInfo, dict):
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
        if not isinstance(other, EventExternalResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other