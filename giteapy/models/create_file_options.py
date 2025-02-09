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


class CreateFileOptions(object):
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
        'author': 'Identity',
        'branch': 'str',
        'committer': 'Identity',
        'content': 'str',
        'dates': 'CommitDateOptions',
        'message': 'str',
        'new_branch': 'str',
        'signoff': 'bool'
    }

    attribute_map = {
        'author': 'author',
        'branch': 'branch',
        'committer': 'committer',
        'content': 'content',
        'dates': 'dates',
        'message': 'message',
        'new_branch': 'new_branch',
        'signoff': 'signoff'
    }

    def __init__(self, author=None, branch=None, committer=None, content=None, dates=None, message=None, new_branch=None, signoff=None, _configuration=None):  # noqa: E501
        """CreateFileOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._author = None
        self._branch = None
        self._committer = None
        self._content = None
        self._dates = None
        self._message = None
        self._new_branch = None
        self._signoff = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if branch is not None:
            self.branch = branch
        if committer is not None:
            self.committer = committer
        self.content = content
        if dates is not None:
            self.dates = dates
        if message is not None:
            self.message = message
        if new_branch is not None:
            self.new_branch = new_branch
        if signoff is not None:
            self.signoff = signoff

    @property
    def author(self):
        """Gets the author of this CreateFileOptions.  # noqa: E501


        :return: The author of this CreateFileOptions.  # noqa: E501
        :rtype: Identity
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this CreateFileOptions.


        :param author: The author of this CreateFileOptions.  # noqa: E501
        :type: Identity
        """

        self._author = author

    @property
    def branch(self):
        """Gets the branch of this CreateFileOptions.  # noqa: E501

        branch (optional) to base this file from. if not given, the default branch is used  # noqa: E501

        :return: The branch of this CreateFileOptions.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this CreateFileOptions.

        branch (optional) to base this file from. if not given, the default branch is used  # noqa: E501

        :param branch: The branch of this CreateFileOptions.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def committer(self):
        """Gets the committer of this CreateFileOptions.  # noqa: E501


        :return: The committer of this CreateFileOptions.  # noqa: E501
        :rtype: Identity
        """
        return self._committer

    @committer.setter
    def committer(self, committer):
        """Sets the committer of this CreateFileOptions.


        :param committer: The committer of this CreateFileOptions.  # noqa: E501
        :type: Identity
        """

        self._committer = committer

    @property
    def content(self):
        """Gets the content of this CreateFileOptions.  # noqa: E501

        content must be base64 encoded  # noqa: E501

        :return: The content of this CreateFileOptions.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateFileOptions.

        content must be base64 encoded  # noqa: E501

        :param content: The content of this CreateFileOptions.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def dates(self):
        """Gets the dates of this CreateFileOptions.  # noqa: E501


        :return: The dates of this CreateFileOptions.  # noqa: E501
        :rtype: CommitDateOptions
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this CreateFileOptions.


        :param dates: The dates of this CreateFileOptions.  # noqa: E501
        :type: CommitDateOptions
        """

        self._dates = dates

    @property
    def message(self):
        """Gets the message of this CreateFileOptions.  # noqa: E501

        message (optional) for the commit of this file. if not supplied, a default message will be used  # noqa: E501

        :return: The message of this CreateFileOptions.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateFileOptions.

        message (optional) for the commit of this file. if not supplied, a default message will be used  # noqa: E501

        :param message: The message of this CreateFileOptions.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def new_branch(self):
        """Gets the new_branch of this CreateFileOptions.  # noqa: E501

        new_branch (optional) will make a new branch from `branch` before creating the file  # noqa: E501

        :return: The new_branch of this CreateFileOptions.  # noqa: E501
        :rtype: str
        """
        return self._new_branch

    @new_branch.setter
    def new_branch(self, new_branch):
        """Sets the new_branch of this CreateFileOptions.

        new_branch (optional) will make a new branch from `branch` before creating the file  # noqa: E501

        :param new_branch: The new_branch of this CreateFileOptions.  # noqa: E501
        :type: str
        """

        self._new_branch = new_branch

    @property
    def signoff(self):
        """Gets the signoff of this CreateFileOptions.  # noqa: E501

        Add a Signed-off-by trailer by the committer at the end of the commit log message.  # noqa: E501

        :return: The signoff of this CreateFileOptions.  # noqa: E501
        :rtype: bool
        """
        return self._signoff

    @signoff.setter
    def signoff(self, signoff):
        """Sets the signoff of this CreateFileOptions.

        Add a Signed-off-by trailer by the committer at the end of the commit log message.  # noqa: E501

        :param signoff: The signoff of this CreateFileOptions.  # noqa: E501
        :type: bool
        """

        self._signoff = signoff

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
        if issubclass(CreateFileOptions, dict):
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
        if not isinstance(other, CreateFileOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateFileOptions):
            return True

        return self.to_dict() != other.to_dict()
