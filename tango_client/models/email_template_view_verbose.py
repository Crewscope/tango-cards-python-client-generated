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


class EmailTemplateViewVerbose(object):
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
        'accent_color': 'str',
        'access_controls': 'list[StandardRewardEmailTemplateAccess]',
        'closing': 'str',
        'customer_service_message': 'str',
        'defaults': 'list[StandardRewardEmailTemplateDefault]',
        'etid': 'str',
        'from_name': 'str',
        'header_image': 'str',
        'header_image_alt_text': 'str',
        'message_body': 'str',
        'name': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'accent_color': 'accentColor',
        'access_controls': 'accessControls',
        'closing': 'closing',
        'customer_service_message': 'customerServiceMessage',
        'defaults': 'defaults',
        'etid': 'etid',
        'from_name': 'fromName',
        'header_image': 'headerImage',
        'header_image_alt_text': 'headerImageAltText',
        'message_body': 'messageBody',
        'name': 'name',
        'subject': 'subject'
    }

    def __init__(self, accent_color=None, access_controls=None, closing=None, customer_service_message=None, defaults=None, etid=None, from_name=None, header_image=None, header_image_alt_text=None, message_body=None, name=None, subject=None, _configuration=None):  # noqa: E501
        """EmailTemplateViewVerbose - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accent_color = None
        self._access_controls = None
        self._closing = None
        self._customer_service_message = None
        self._defaults = None
        self._etid = None
        self._from_name = None
        self._header_image = None
        self._header_image_alt_text = None
        self._message_body = None
        self._name = None
        self._subject = None
        self.discriminator = None

        self.accent_color = accent_color
        if access_controls is not None:
            self.access_controls = access_controls
        self.closing = closing
        if customer_service_message is not None:
            self.customer_service_message = customer_service_message
        if defaults is not None:
            self.defaults = defaults
        self.etid = etid
        self.from_name = from_name
        self.header_image = header_image
        self.header_image_alt_text = header_image_alt_text
        self.message_body = message_body
        self.name = name
        self.subject = subject

    @property
    def accent_color(self):
        """Gets the accent_color of this EmailTemplateViewVerbose.  # noqa: E501

        Accent Color  # noqa: E501

        :return: The accent_color of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._accent_color

    @accent_color.setter
    def accent_color(self, accent_color):
        """Sets the accent_color of this EmailTemplateViewVerbose.

        Accent Color  # noqa: E501

        :param accent_color: The accent_color of this EmailTemplateViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and accent_color is None:
            raise ValueError("Invalid value for `accent_color`, must not be `None`")  # noqa: E501

        self._accent_color = accent_color

    @property
    def access_controls(self):
        """Gets the access_controls of this EmailTemplateViewVerbose.  # noqa: E501

        Access Control  # noqa: E501

        :return: The access_controls of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: list[StandardRewardEmailTemplateAccess]
        """
        return self._access_controls

    @access_controls.setter
    def access_controls(self, access_controls):
        """Sets the access_controls of this EmailTemplateViewVerbose.

        Access Control  # noqa: E501

        :param access_controls: The access_controls of this EmailTemplateViewVerbose.  # noqa: E501
        :type: list[StandardRewardEmailTemplateAccess]
        """

        self._access_controls = access_controls

    @property
    def closing(self):
        """Gets the closing of this EmailTemplateViewVerbose.  # noqa: E501

        Closing Message  # noqa: E501

        :return: The closing of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._closing

    @closing.setter
    def closing(self, closing):
        """Sets the closing of this EmailTemplateViewVerbose.

        Closing Message  # noqa: E501

        :param closing: The closing of this EmailTemplateViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and closing is None:
            raise ValueError("Invalid value for `closing`, must not be `None`")  # noqa: E501

        self._closing = closing

    @property
    def customer_service_message(self):
        """Gets the customer_service_message of this EmailTemplateViewVerbose.  # noqa: E501

        Customer Service Message  # noqa: E501

        :return: The customer_service_message of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._customer_service_message

    @customer_service_message.setter
    def customer_service_message(self, customer_service_message):
        """Sets the customer_service_message of this EmailTemplateViewVerbose.

        Customer Service Message  # noqa: E501

        :param customer_service_message: The customer_service_message of this EmailTemplateViewVerbose.  # noqa: E501
        :type: str
        """

        self._customer_service_message = customer_service_message

    @property
    def defaults(self):
        """Gets the defaults of this EmailTemplateViewVerbose.  # noqa: E501

        Defaults  # noqa: E501

        :return: The defaults of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: list[StandardRewardEmailTemplateDefault]
        """
        return self._defaults

    @defaults.setter
    def defaults(self, defaults):
        """Sets the defaults of this EmailTemplateViewVerbose.

        Defaults  # noqa: E501

        :param defaults: The defaults of this EmailTemplateViewVerbose.  # noqa: E501
        :type: list[StandardRewardEmailTemplateDefault]
        """

        self._defaults = defaults

    @property
    def etid(self):
        """Gets the etid of this EmailTemplateViewVerbose.  # noqa: E501

        Email Template Identifier (ETID)  # noqa: E501

        :return: The etid of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._etid

    @etid.setter
    def etid(self, etid):
        """Sets the etid of this EmailTemplateViewVerbose.

        Email Template Identifier (ETID)  # noqa: E501

        :param etid: The etid of this EmailTemplateViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and etid is None:
            raise ValueError("Invalid value for `etid`, must not be `None`")  # noqa: E501

        self._etid = etid

    @property
    def from_name(self):
        """Gets the from_name of this EmailTemplateViewVerbose.  # noqa: E501

        From Name  # noqa: E501

        :return: The from_name of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this EmailTemplateViewVerbose.

        From Name  # noqa: E501

        :param from_name: The from_name of this EmailTemplateViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and from_name is None:
            raise ValueError("Invalid value for `from_name`, must not be `None`")  # noqa: E501

        self._from_name = from_name

    @property
    def header_image(self):
        """Gets the header_image of this EmailTemplateViewVerbose.  # noqa: E501

        Header Image Url  # noqa: E501

        :return: The header_image of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._header_image

    @header_image.setter
    def header_image(self, header_image):
        """Sets the header_image of this EmailTemplateViewVerbose.

        Header Image Url  # noqa: E501

        :param header_image: The header_image of this EmailTemplateViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and header_image is None:
            raise ValueError("Invalid value for `header_image`, must not be `None`")  # noqa: E501

        self._header_image = header_image

    @property
    def header_image_alt_text(self):
        """Gets the header_image_alt_text of this EmailTemplateViewVerbose.  # noqa: E501

        Header Image - Alt Text  # noqa: E501

        :return: The header_image_alt_text of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._header_image_alt_text

    @header_image_alt_text.setter
    def header_image_alt_text(self, header_image_alt_text):
        """Sets the header_image_alt_text of this EmailTemplateViewVerbose.

        Header Image - Alt Text  # noqa: E501

        :param header_image_alt_text: The header_image_alt_text of this EmailTemplateViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and header_image_alt_text is None:
            raise ValueError("Invalid value for `header_image_alt_text`, must not be `None`")  # noqa: E501

        self._header_image_alt_text = header_image_alt_text

    @property
    def message_body(self):
        """Gets the message_body of this EmailTemplateViewVerbose.  # noqa: E501

        Message Body  # noqa: E501

        :return: The message_body of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._message_body

    @message_body.setter
    def message_body(self, message_body):
        """Sets the message_body of this EmailTemplateViewVerbose.

        Message Body  # noqa: E501

        :param message_body: The message_body of this EmailTemplateViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and message_body is None:
            raise ValueError("Invalid value for `message_body`, must not be `None`")  # noqa: E501

        self._message_body = message_body

    @property
    def name(self):
        """Gets the name of this EmailTemplateViewVerbose.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailTemplateViewVerbose.

        Name  # noqa: E501

        :param name: The name of this EmailTemplateViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def subject(self):
        """Gets the subject of this EmailTemplateViewVerbose.  # noqa: E501

        Subject  # noqa: E501

        :return: The subject of this EmailTemplateViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EmailTemplateViewVerbose.

        Subject  # noqa: E501

        :param subject: The subject of this EmailTemplateViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

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
        if issubclass(EmailTemplateViewVerbose, dict):
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
        if not isinstance(other, EmailTemplateViewVerbose):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailTemplateViewVerbose):
            return True

        return self.to_dict() != other.to_dict()
