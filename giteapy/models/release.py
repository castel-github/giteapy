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


class Release(object):
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
        'assets': 'list[Attachment]',
        'author': 'User',
        'body': 'str',
        'created_at': 'datetime',
        'draft': 'bool',
        'html_url': 'str',
        'id': 'int',
        'name': 'str',
        'prerelease': 'bool',
        'published_at': 'datetime',
        'tag_name': 'str',
        'tarball_url': 'str',
        'target_commitish': 'str',
        'upload_url': 'str',
        'url': 'str',
        'zipball_url': 'str'
    }

    attribute_map = {
        'assets': 'assets',
        'author': 'author',
        'body': 'body',
        'created_at': 'created_at',
        'draft': 'draft',
        'html_url': 'html_url',
        'id': 'id',
        'name': 'name',
        'prerelease': 'prerelease',
        'published_at': 'published_at',
        'tag_name': 'tag_name',
        'tarball_url': 'tarball_url',
        'target_commitish': 'target_commitish',
        'upload_url': 'upload_url',
        'url': 'url',
        'zipball_url': 'zipball_url'
    }

    def __init__(self, assets=None, author=None, body=None, created_at=None, draft=None, html_url=None, id=None, name=None, prerelease=None, published_at=None, tag_name=None, tarball_url=None, target_commitish=None, upload_url=None, url=None, zipball_url=None, _configuration=None):  # noqa: E501
        """Release - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assets = None
        self._author = None
        self._body = None
        self._created_at = None
        self._draft = None
        self._html_url = None
        self._id = None
        self._name = None
        self._prerelease = None
        self._published_at = None
        self._tag_name = None
        self._tarball_url = None
        self._target_commitish = None
        self._upload_url = None
        self._url = None
        self._zipball_url = None
        self.discriminator = None

        if assets is not None:
            self.assets = assets
        if author is not None:
            self.author = author
        if body is not None:
            self.body = body
        if created_at is not None:
            self.created_at = created_at
        if draft is not None:
            self.draft = draft
        if html_url is not None:
            self.html_url = html_url
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if prerelease is not None:
            self.prerelease = prerelease
        if published_at is not None:
            self.published_at = published_at
        if tag_name is not None:
            self.tag_name = tag_name
        if tarball_url is not None:
            self.tarball_url = tarball_url
        if target_commitish is not None:
            self.target_commitish = target_commitish
        if upload_url is not None:
            self.upload_url = upload_url
        if url is not None:
            self.url = url
        if zipball_url is not None:
            self.zipball_url = zipball_url

    @property
    def assets(self):
        """Gets the assets of this Release.  # noqa: E501


        :return: The assets of this Release.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this Release.


        :param assets: The assets of this Release.  # noqa: E501
        :type: list[Attachment]
        """

        self._assets = assets

    @property
    def author(self):
        """Gets the author of this Release.  # noqa: E501


        :return: The author of this Release.  # noqa: E501
        :rtype: User
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Release.


        :param author: The author of this Release.  # noqa: E501
        :type: User
        """

        self._author = author

    @property
    def body(self):
        """Gets the body of this Release.  # noqa: E501


        :return: The body of this Release.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Release.


        :param body: The body of this Release.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def created_at(self):
        """Gets the created_at of this Release.  # noqa: E501


        :return: The created_at of this Release.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Release.


        :param created_at: The created_at of this Release.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def draft(self):
        """Gets the draft of this Release.  # noqa: E501


        :return: The draft of this Release.  # noqa: E501
        :rtype: bool
        """
        return self._draft

    @draft.setter
    def draft(self, draft):
        """Sets the draft of this Release.


        :param draft: The draft of this Release.  # noqa: E501
        :type: bool
        """

        self._draft = draft

    @property
    def html_url(self):
        """Gets the html_url of this Release.  # noqa: E501


        :return: The html_url of this Release.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this Release.


        :param html_url: The html_url of this Release.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def id(self):
        """Gets the id of this Release.  # noqa: E501


        :return: The id of this Release.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Release.


        :param id: The id of this Release.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Release.  # noqa: E501


        :return: The name of this Release.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Release.


        :param name: The name of this Release.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def prerelease(self):
        """Gets the prerelease of this Release.  # noqa: E501


        :return: The prerelease of this Release.  # noqa: E501
        :rtype: bool
        """
        return self._prerelease

    @prerelease.setter
    def prerelease(self, prerelease):
        """Sets the prerelease of this Release.


        :param prerelease: The prerelease of this Release.  # noqa: E501
        :type: bool
        """

        self._prerelease = prerelease

    @property
    def published_at(self):
        """Gets the published_at of this Release.  # noqa: E501


        :return: The published_at of this Release.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """Sets the published_at of this Release.


        :param published_at: The published_at of this Release.  # noqa: E501
        :type: datetime
        """

        self._published_at = published_at

    @property
    def tag_name(self):
        """Gets the tag_name of this Release.  # noqa: E501


        :return: The tag_name of this Release.  # noqa: E501
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this Release.


        :param tag_name: The tag_name of this Release.  # noqa: E501
        :type: str
        """

        self._tag_name = tag_name

    @property
    def tarball_url(self):
        """Gets the tarball_url of this Release.  # noqa: E501


        :return: The tarball_url of this Release.  # noqa: E501
        :rtype: str
        """
        return self._tarball_url

    @tarball_url.setter
    def tarball_url(self, tarball_url):
        """Sets the tarball_url of this Release.


        :param tarball_url: The tarball_url of this Release.  # noqa: E501
        :type: str
        """

        self._tarball_url = tarball_url

    @property
    def target_commitish(self):
        """Gets the target_commitish of this Release.  # noqa: E501


        :return: The target_commitish of this Release.  # noqa: E501
        :rtype: str
        """
        return self._target_commitish

    @target_commitish.setter
    def target_commitish(self, target_commitish):
        """Sets the target_commitish of this Release.


        :param target_commitish: The target_commitish of this Release.  # noqa: E501
        :type: str
        """

        self._target_commitish = target_commitish

    @property
    def upload_url(self):
        """Gets the upload_url of this Release.  # noqa: E501


        :return: The upload_url of this Release.  # noqa: E501
        :rtype: str
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        """Sets the upload_url of this Release.


        :param upload_url: The upload_url of this Release.  # noqa: E501
        :type: str
        """

        self._upload_url = upload_url

    @property
    def url(self):
        """Gets the url of this Release.  # noqa: E501


        :return: The url of this Release.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Release.


        :param url: The url of this Release.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def zipball_url(self):
        """Gets the zipball_url of this Release.  # noqa: E501


        :return: The zipball_url of this Release.  # noqa: E501
        :rtype: str
        """
        return self._zipball_url

    @zipball_url.setter
    def zipball_url(self, zipball_url):
        """Sets the zipball_url of this Release.


        :param zipball_url: The zipball_url of this Release.  # noqa: E501
        :type: str
        """

        self._zipball_url = zipball_url

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
        if issubclass(Release, dict):
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
        if not isinstance(other, Release):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Release):
            return True

        return self.to_dict() != other.to_dict()
