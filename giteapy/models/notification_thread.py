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


class NotificationThread(object):
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
        'id': 'int',
        'pinned': 'bool',
        'repository': 'Repository',
        'subject': 'NotificationSubject',
        'unread': 'bool',
        'updated_at': 'datetime',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'pinned': 'pinned',
        'repository': 'repository',
        'subject': 'subject',
        'unread': 'unread',
        'updated_at': 'updated_at',
        'url': 'url'
    }

    def __init__(self, id=None, pinned=None, repository=None, subject=None, unread=None, updated_at=None, url=None, _configuration=None):  # noqa: E501
        """NotificationThread - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._pinned = None
        self._repository = None
        self._subject = None
        self._unread = None
        self._updated_at = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if pinned is not None:
            self.pinned = pinned
        if repository is not None:
            self.repository = repository
        if subject is not None:
            self.subject = subject
        if unread is not None:
            self.unread = unread
        if updated_at is not None:
            self.updated_at = updated_at
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this NotificationThread.  # noqa: E501


        :return: The id of this NotificationThread.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationThread.


        :param id: The id of this NotificationThread.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def pinned(self):
        """Gets the pinned of this NotificationThread.  # noqa: E501


        :return: The pinned of this NotificationThread.  # noqa: E501
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this NotificationThread.


        :param pinned: The pinned of this NotificationThread.  # noqa: E501
        :type: bool
        """

        self._pinned = pinned

    @property
    def repository(self):
        """Gets the repository of this NotificationThread.  # noqa: E501


        :return: The repository of this NotificationThread.  # noqa: E501
        :rtype: Repository
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this NotificationThread.


        :param repository: The repository of this NotificationThread.  # noqa: E501
        :type: Repository
        """

        self._repository = repository

    @property
    def subject(self):
        """Gets the subject of this NotificationThread.  # noqa: E501


        :return: The subject of this NotificationThread.  # noqa: E501
        :rtype: NotificationSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this NotificationThread.


        :param subject: The subject of this NotificationThread.  # noqa: E501
        :type: NotificationSubject
        """

        self._subject = subject

    @property
    def unread(self):
        """Gets the unread of this NotificationThread.  # noqa: E501


        :return: The unread of this NotificationThread.  # noqa: E501
        :rtype: bool
        """
        return self._unread

    @unread.setter
    def unread(self, unread):
        """Sets the unread of this NotificationThread.


        :param unread: The unread of this NotificationThread.  # noqa: E501
        :type: bool
        """

        self._unread = unread

    @property
    def updated_at(self):
        """Gets the updated_at of this NotificationThread.  # noqa: E501


        :return: The updated_at of this NotificationThread.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NotificationThread.


        :param updated_at: The updated_at of this NotificationThread.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def url(self):
        """Gets the url of this NotificationThread.  # noqa: E501


        :return: The url of this NotificationThread.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NotificationThread.


        :param url: The url of this NotificationThread.  # noqa: E501
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
        if issubclass(NotificationThread, dict):
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
        if not isinstance(other, NotificationThread):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationThread):
            return True

        return self.to_dict() != other.to_dict()
