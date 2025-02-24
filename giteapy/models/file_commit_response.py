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


class FileCommitResponse(object):
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
        'author': 'CommitUser',
        'committer': 'CommitUser',
        'created': 'datetime',
        'html_url': 'str',
        'message': 'str',
        'parents': 'list[CommitMeta]',
        'sha': 'str',
        'tree': 'CommitMeta',
        'url': 'str'
    }

    attribute_map = {
        'author': 'author',
        'committer': 'committer',
        'created': 'created',
        'html_url': 'html_url',
        'message': 'message',
        'parents': 'parents',
        'sha': 'sha',
        'tree': 'tree',
        'url': 'url'
    }

    def __init__(self, author=None, committer=None, created=None, html_url=None, message=None, parents=None, sha=None, tree=None, url=None, _configuration=None):  # noqa: E501
        """FileCommitResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._author = None
        self._committer = None
        self._created = None
        self._html_url = None
        self._message = None
        self._parents = None
        self._sha = None
        self._tree = None
        self._url = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if committer is not None:
            self.committer = committer
        if created is not None:
            self.created = created
        if html_url is not None:
            self.html_url = html_url
        if message is not None:
            self.message = message
        if parents is not None:
            self.parents = parents
        if sha is not None:
            self.sha = sha
        if tree is not None:
            self.tree = tree
        if url is not None:
            self.url = url

    @property
    def author(self):
        """Gets the author of this FileCommitResponse.  # noqa: E501


        :return: The author of this FileCommitResponse.  # noqa: E501
        :rtype: CommitUser
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this FileCommitResponse.


        :param author: The author of this FileCommitResponse.  # noqa: E501
        :type: CommitUser
        """

        self._author = author

    @property
    def committer(self):
        """Gets the committer of this FileCommitResponse.  # noqa: E501


        :return: The committer of this FileCommitResponse.  # noqa: E501
        :rtype: CommitUser
        """
        return self._committer

    @committer.setter
    def committer(self, committer):
        """Sets the committer of this FileCommitResponse.


        :param committer: The committer of this FileCommitResponse.  # noqa: E501
        :type: CommitUser
        """

        self._committer = committer

    @property
    def created(self):
        """Gets the created of this FileCommitResponse.  # noqa: E501


        :return: The created of this FileCommitResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FileCommitResponse.


        :param created: The created of this FileCommitResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def html_url(self):
        """Gets the html_url of this FileCommitResponse.  # noqa: E501


        :return: The html_url of this FileCommitResponse.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this FileCommitResponse.


        :param html_url: The html_url of this FileCommitResponse.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def message(self):
        """Gets the message of this FileCommitResponse.  # noqa: E501


        :return: The message of this FileCommitResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FileCommitResponse.


        :param message: The message of this FileCommitResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def parents(self):
        """Gets the parents of this FileCommitResponse.  # noqa: E501


        :return: The parents of this FileCommitResponse.  # noqa: E501
        :rtype: list[CommitMeta]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this FileCommitResponse.


        :param parents: The parents of this FileCommitResponse.  # noqa: E501
        :type: list[CommitMeta]
        """

        self._parents = parents

    @property
    def sha(self):
        """Gets the sha of this FileCommitResponse.  # noqa: E501


        :return: The sha of this FileCommitResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this FileCommitResponse.


        :param sha: The sha of this FileCommitResponse.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def tree(self):
        """Gets the tree of this FileCommitResponse.  # noqa: E501


        :return: The tree of this FileCommitResponse.  # noqa: E501
        :rtype: CommitMeta
        """
        return self._tree

    @tree.setter
    def tree(self, tree):
        """Sets the tree of this FileCommitResponse.


        :param tree: The tree of this FileCommitResponse.  # noqa: E501
        :type: CommitMeta
        """

        self._tree = tree

    @property
    def url(self):
        """Gets the url of this FileCommitResponse.  # noqa: E501


        :return: The url of this FileCommitResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FileCommitResponse.


        :param url: The url of this FileCommitResponse.  # noqa: E501
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
        if issubclass(FileCommitResponse, dict):
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
        if not isinstance(other, FileCommitResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileCommitResponse):
            return True

        return self.to_dict() != other.to_dict()
