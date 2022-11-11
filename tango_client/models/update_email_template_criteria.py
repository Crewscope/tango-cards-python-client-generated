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


class UpdateEmailTemplateCriteria(object):
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
        'access_control': 'list[StandardRewardEmailTemplateAccess]',
        'closing': 'str',
        'customer_service_message': 'str',
        'defaults': 'list[StandardRewardEmailTemplateDefault]',
        'from_name': 'str',
        'header_image': 'str',
        'header_image_alt_text': 'str',
        'message_body': 'str',
        'name': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'accent_color': 'accentColor',
        'access_control': 'accessControl',
        'closing': 'closing',
        'customer_service_message': 'customerServiceMessage',
        'defaults': 'defaults',
        'from_name': 'fromName',
        'header_image': 'headerImage',
        'header_image_alt_text': 'headerImageAltText',
        'message_body': 'messageBody',
        'name': 'name',
        'subject': 'subject'
    }

    def __init__(self, accent_color=None, access_control=None, closing=None, customer_service_message=None, defaults=None, from_name=None, header_image=None, header_image_alt_text=None, message_body=None, name=None, subject=None, _configuration=None):  # noqa: E501
        """UpdateEmailTemplateCriteria - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accent_color = None
        self._access_control = None
        self._closing = None
        self._customer_service_message = None
        self._defaults = None
        self._from_name = None
        self._header_image = None
        self._header_image_alt_text = None
        self._message_body = None
        self._name = None
        self._subject = None
        self.discriminator = None

        if accent_color is not None:
            self.accent_color = accent_color
        if access_control is not None:
            self.access_control = access_control
        if closing is not None:
            self.closing = closing
        if customer_service_message is not None:
            self.customer_service_message = customer_service_message
        if defaults is not None:
            self.defaults = defaults
        if from_name is not None:
            self.from_name = from_name
        if header_image is not None:
            self.header_image = header_image
        if header_image_alt_text is not None:
            self.header_image_alt_text = header_image_alt_text
        if message_body is not None:
            self.message_body = message_body
        if name is not None:
            self.name = name
        if subject is not None:
            self.subject = subject

    @property
    def accent_color(self):
        """Gets the accent_color of this UpdateEmailTemplateCriteria.  # noqa: E501

        Accent Color  # noqa: E501

        :return: The accent_color of this UpdateEmailTemplateCriteria.  # noqa: E501
        :rtype: str
        """
        return self._accent_color

    @accent_color.setter
    def accent_color(self, accent_color):
        """Sets the accent_color of this UpdateEmailTemplateCriteria.

        Accent Color  # noqa: E501

        :param accent_color: The accent_color of this UpdateEmailTemplateCriteria.  # noqa: E501
        :type: str
        """

        self._accent_color = accent_color

    @property
    def access_control(self):
        """Gets the access_control of this UpdateEmailTemplateCriteria.  # noqa: E501

        Access Control  # noqa: E501

        :return: The access_control of this UpdateEmailTemplateCriteria.  # noqa: E501
        :rtype: list[StandardRewardEmailTemplateAccess]
        """
        return self._access_control

    @access_control.setter
    def access_control(self, access_control):
        """Sets the access_control of this UpdateEmailTemplateCriteria.

        Access Control  # noqa: E501

        :param access_control: The access_control of this UpdateEmailTemplateCriteria.  # noqa: E501
        :type: list[StandardRewardEmailTemplateAccess]
        """

        self._access_control = access_control

    @property
    def closing(self):
        """Gets the closing of this UpdateEmailTemplateCriteria.  # noqa: E501

        Closing Message  # noqa: E501

        :return: The closing of this UpdateEmailTemplateCriteria.  # noqa: E501
        :rtype: str
        """
        return self._closing

    @closing.setter
    def closing(self, closing):
        """Sets the closing of this UpdateEmailTemplateCriteria.

        Closing Message  # noqa: E501

        :param closing: The closing of this UpdateEmailTemplateCriteria.  # noqa: E501
        :type: str
        """

        self._closing = closing

    @property
    def customer_service_message(self):
        """Gets the customer_service_message of this UpdateEmailTemplateCriteria.  # noqa: E501

        Customer Service Message  # noqa: E501

        :return: The customer_service_message of this UpdateEmailTemplateCriteria.  # noqa: E501
        :rtype: str
        """
        return self._customer_service_message

    @customer_service_message.setter
    def customer_service_message(self, customer_service_message):
        """Sets the customer_service_message of this UpdateEmailTemplateCriteria.

        Customer Service Message  # noqa: E501

        :param customer_service_message: The customer_service_message of this UpdateEmailTemplateCriteria.  # noqa: E501
        :type: str
        """

        self._customer_service_message = customer_service_message

    @property
    def defaults(self):
        """Gets the defaults of this UpdateEmailTemplateCriteria.  # noqa: E501

        Defaults  # noqa: E501

        :return: The defaults of this UpdateEmailTemplateCriteria.  # noqa: E501
        :rtype: list[StandardRewardEmailTemplateDefault]
        """
        return self._defaults

    @defaults.setter
    def defaults(self, defaults):
        """Sets the defaults of this UpdateEmailTemplateCriteria.

        Defaults  # noqa: E501

        :param defaults: The defaults of this UpdateEmailTemplateCriteria.  # noqa: E501
        :type: list[StandardRewardEmailTemplateDefault]
        """

        self._defaults = defaults

    @property
    def from_name(self):
        """Gets the from_name of this UpdateEmailTemplateCriteria.  # noqa: E501

        From Name  # noqa: E501

        :return: The from_name of this UpdateEmailTemplateCriteria.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this UpdateEmailTemplateCriteria.

        From Name  # noqa: E501

        :param from_name: The from_name of this UpdateEmailTemplateCriteria.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def header_image(self):
        """Gets the header_image of this UpdateEmailTemplateCriteria.  # noqa: E501

        Header Image (Base 64 Encoded)  # noqa: E501

        :return: The header_image of this UpdateEmailTemplateCriteria.  # noqa: E501
        :rtype: str
        """
        return self._header_image

    @header_image.setter
    def header_image(self, header_image):
        """Sets the header_image of this UpdateEmailTemplateCriteria.

        Header Image (Base 64 Encoded)  # noqa: E501

        :param header_image: The header_image of this UpdateEmailTemplateCriteria.  # noqa: E501
        :type: str
        """

        self._header_image = header_image

    @property
    def header_image_alt_text(self):
        """Gets the header_image_alt_text of this UpdateEmailTemplateCriteria.  # noqa: E501

        Header Image - Alt Text  # noqa: E501

        :return: The header_image_alt_text of this UpdateEmailTemplateCriteria.  # noqa: E501
        :rtype: str
        """
        return self._header_image_alt_text

    @header_image_alt_text.setter
    def header_image_alt_text(self, header_image_alt_text):
        """Sets the header_image_alt_text of this UpdateEmailTemplateCriteria.

        Header Image - Alt Text  # noqa: E501

        :param header_image_alt_text: The header_image_alt_text of this UpdateEmailTemplateCriteria.  # noqa: E501
        :type: str
        """

        self._header_image_alt_text = header_image_alt_text

    @property
    def message_body(self):
        """Gets the message_body of this UpdateEmailTemplateCriteria.  # noqa: E501

        Message Body  # noqa: E501

        :return: The message_body of this UpdateEmailTemplateCriteria.  # noqa: E501
        :rtype: str
        """
        return self._message_body

    @message_body.setter
    def message_body(self, message_body):
        """Sets the message_body of this UpdateEmailTemplateCriteria.

        Message Body  # noqa: E501

        :param message_body: The message_body of this UpdateEmailTemplateCriteria.  # noqa: E501
        :type: str
        """

        self._message_body = message_body

    @property
    def name(self):
        """Gets the name of this UpdateEmailTemplateCriteria.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this UpdateEmailTemplateCriteria.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateEmailTemplateCriteria.

        Name  # noqa: E501

        :param name: The name of this UpdateEmailTemplateCriteria.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def subject(self):
        """Gets the subject of this UpdateEmailTemplateCriteria.  # noqa: E501

        Subject  # noqa: E501

        :return: The subject of this UpdateEmailTemplateCriteria.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this UpdateEmailTemplateCriteria.

        Subject  # noqa: E501

        :param subject: The subject of this UpdateEmailTemplateCriteria.  # noqa: E501
        :type: str
        """

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
        if issubclass(UpdateEmailTemplateCriteria, dict):
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
        if not isinstance(other, UpdateEmailTemplateCriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateEmailTemplateCriteria):
            return True

        return self.to_dict() != other.to_dict()
