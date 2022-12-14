# coding: utf-8

"""
    Tango Card RaaS API

    <5. Ordersp>Welcome to the RaaS&reg; API – with this RESTful API you can integrate a global reward or incentive program into your app or platform.<br /><br /> This console works in our Sandbox environment. To receive your own credentials or to ask questions, please contact us at <a href=\"mailto:devsupport@tangocard.com\">devsupport@tangocard.com</a>.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from tango_client.configuration import Configuration


class EmailTemplateListView(object):
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
        'email_templates': 'list[EmailTemplateViewVerbose]',
        'page': 'PageView'
    }

    attribute_map = {
        'email_templates': 'emailTemplates',
        'page': 'page'
    }

    def __init__(self, email_templates=None, page=None, _configuration=None):  # noqa: E501
        """EmailTemplateListView - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email_templates = None
        self._page = None
        self.discriminator = None

        self.email_templates = email_templates
        self.page = page

    @property
    def email_templates(self):
        """Gets the email_templates of this EmailTemplateListView.  # noqa: E501

        Email Template elements for the current page  # noqa: E501

        :return: The email_templates of this EmailTemplateListView.  # noqa: E501
        :rtype: list[EmailTemplateViewVerbose]
        """
        return self._email_templates

    @email_templates.setter
    def email_templates(self, email_templates):
        """Sets the email_templates of this EmailTemplateListView.

        Email Template elements for the current page  # noqa: E501

        :param email_templates: The email_templates of this EmailTemplateListView.  # noqa: E501
        :type: list[EmailTemplateViewVerbose]
        """
        if self._configuration.client_side_validation and email_templates is None:
            raise ValueError("Invalid value for `email_templates`, must not be `None`")  # noqa: E501

        self._email_templates = email_templates

    @property
    def page(self):
        """Gets the page of this EmailTemplateListView.  # noqa: E501

        Page data for email templates  # noqa: E501

        :return: The page of this EmailTemplateListView.  # noqa: E501
        :rtype: PageView
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this EmailTemplateListView.

        Page data for email templates  # noqa: E501

        :param page: The page of this EmailTemplateListView.  # noqa: E501
        :type: PageView
        """
        if self._configuration.client_side_validation and page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

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
        if issubclass(EmailTemplateListView, dict):
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
        if not isinstance(other, EmailTemplateListView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailTemplateListView):
            return True

        return self.to_dict() != other.to_dict()
