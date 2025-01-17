# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.23.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class CombinedStatus(object):
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
        'commit_url': 'str',
        'repository': 'Repository',
        'sha': 'str',
        'state': 'CommitStatusState',
        'statuses': 'list[CommitStatus]',
        'total_count': 'int',
        'url': 'str'
    }

    attribute_map = {
        'commit_url': 'commit_url',
        'repository': 'repository',
        'sha': 'sha',
        'state': 'state',
        'statuses': 'statuses',
        'total_count': 'total_count',
        'url': 'url'
    }

    def __init__(self, commit_url=None, repository=None, sha=None, state=None, statuses=None, total_count=None, url=None, _configuration=None):  # noqa: E501
        """CombinedStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._commit_url = None
        self._repository = None
        self._sha = None
        self._state = None
        self._statuses = None
        self._total_count = None
        self._url = None
        self.discriminator = None

        if commit_url is not None:
            self.commit_url = commit_url
        if repository is not None:
            self.repository = repository
        if sha is not None:
            self.sha = sha
        if state is not None:
            self.state = state
        if statuses is not None:
            self.statuses = statuses
        if total_count is not None:
            self.total_count = total_count
        if url is not None:
            self.url = url

    @property
    def commit_url(self):
        """Gets the commit_url of this CombinedStatus.  # noqa: E501


        :return: The commit_url of this CombinedStatus.  # noqa: E501
        :rtype: str
        """
        return self._commit_url

    @commit_url.setter
    def commit_url(self, commit_url):
        """Sets the commit_url of this CombinedStatus.


        :param commit_url: The commit_url of this CombinedStatus.  # noqa: E501
        :type: str
        """

        self._commit_url = commit_url

    @property
    def repository(self):
        """Gets the repository of this CombinedStatus.  # noqa: E501


        :return: The repository of this CombinedStatus.  # noqa: E501
        :rtype: Repository
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this CombinedStatus.


        :param repository: The repository of this CombinedStatus.  # noqa: E501
        :type: Repository
        """

        self._repository = repository

    @property
    def sha(self):
        """Gets the sha of this CombinedStatus.  # noqa: E501


        :return: The sha of this CombinedStatus.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this CombinedStatus.


        :param sha: The sha of this CombinedStatus.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def state(self):
        """Gets the state of this CombinedStatus.  # noqa: E501


        :return: The state of this CombinedStatus.  # noqa: E501
        :rtype: CommitStatusState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CombinedStatus.


        :param state: The state of this CombinedStatus.  # noqa: E501
        :type: CommitStatusState
        """

        self._state = state

    @property
    def statuses(self):
        """Gets the statuses of this CombinedStatus.  # noqa: E501


        :return: The statuses of this CombinedStatus.  # noqa: E501
        :rtype: list[CommitStatus]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this CombinedStatus.


        :param statuses: The statuses of this CombinedStatus.  # noqa: E501
        :type: list[CommitStatus]
        """

        self._statuses = statuses

    @property
    def total_count(self):
        """Gets the total_count of this CombinedStatus.  # noqa: E501


        :return: The total_count of this CombinedStatus.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this CombinedStatus.


        :param total_count: The total_count of this CombinedStatus.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def url(self):
        """Gets the url of this CombinedStatus.  # noqa: E501


        :return: The url of this CombinedStatus.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CombinedStatus.


        :param url: The url of this CombinedStatus.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(CombinedStatus, dict):
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
        if not isinstance(other, CombinedStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CombinedStatus):
            return True

        return self.to_dict() != other.to_dict()
