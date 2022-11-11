# coding: utf-8

"""
    Tango Card RaaS API

    <p>Welcome to the RaaS&reg; API – with this RESTful API you can integrate a global reward or incentive program into your app or platform.<br /><br /> This console works in our Sandbox environment. To receive your own credentials or to ask questions, please contact us at <a href=\"mailto:devsupport@tangocard.com\">devsupport@tangocard.com</a>.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from tango_client.configuration import Configuration


class BrandRequirements(object):
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
        'always_show_disclaimer': 'bool',
        'disclaimer_instructions': 'str',
        'display_instructions': 'str',
        'terms_and_conditions_instructions': 'str'
    }

    attribute_map = {
        'always_show_disclaimer': 'alwaysShowDisclaimer',
        'disclaimer_instructions': 'disclaimerInstructions',
        'display_instructions': 'displayInstructions',
        'terms_and_conditions_instructions': 'termsAndConditionsInstructions'
    }

    def __init__(self, always_show_disclaimer=None, disclaimer_instructions=None, display_instructions=None, terms_and_conditions_instructions=None, _configuration=None):  # noqa: E501
        """BrandRequirements - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._always_show_disclaimer = None
        self._disclaimer_instructions = None
        self._display_instructions = None
        self._terms_and_conditions_instructions = None
        self.discriminator = None

        self.always_show_disclaimer = always_show_disclaimer
        self.disclaimer_instructions = disclaimer_instructions
        self.display_instructions = display_instructions
        self.terms_and_conditions_instructions = terms_and_conditions_instructions

    @property
    def always_show_disclaimer(self):
        """Gets the always_show_disclaimer of this BrandRequirements.  # noqa: E501

        Always Show Disclaimer  # noqa: E501

        :return: The always_show_disclaimer of this BrandRequirements.  # noqa: E501
        :rtype: bool
        """
        return self._always_show_disclaimer

    @always_show_disclaimer.setter
    def always_show_disclaimer(self, always_show_disclaimer):
        """Sets the always_show_disclaimer of this BrandRequirements.

        Always Show Disclaimer  # noqa: E501

        :param always_show_disclaimer: The always_show_disclaimer of this BrandRequirements.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and always_show_disclaimer is None:
            raise ValueError("Invalid value for `always_show_disclaimer`, must not be `None`")  # noqa: E501

        self._always_show_disclaimer = always_show_disclaimer

    @property
    def disclaimer_instructions(self):
        """Gets the disclaimer_instructions of this BrandRequirements.  # noqa: E501

        Disclaimer Instructions  # noqa: E501

        :return: The disclaimer_instructions of this BrandRequirements.  # noqa: E501
        :rtype: str
        """
        return self._disclaimer_instructions

    @disclaimer_instructions.setter
    def disclaimer_instructions(self, disclaimer_instructions):
        """Sets the disclaimer_instructions of this BrandRequirements.

        Disclaimer Instructions  # noqa: E501

        :param disclaimer_instructions: The disclaimer_instructions of this BrandRequirements.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and disclaimer_instructions is None:
            raise ValueError("Invalid value for `disclaimer_instructions`, must not be `None`")  # noqa: E501

        self._disclaimer_instructions = disclaimer_instructions

    @property
    def display_instructions(self):
        """Gets the display_instructions of this BrandRequirements.  # noqa: E501

        Display Instructions  # noqa: E501

        :return: The display_instructions of this BrandRequirements.  # noqa: E501
        :rtype: str
        """
        return self._display_instructions

    @display_instructions.setter
    def display_instructions(self, display_instructions):
        """Sets the display_instructions of this BrandRequirements.

        Display Instructions  # noqa: E501

        :param display_instructions: The display_instructions of this BrandRequirements.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and display_instructions is None:
            raise ValueError("Invalid value for `display_instructions`, must not be `None`")  # noqa: E501

        self._display_instructions = display_instructions

    @property
    def terms_and_conditions_instructions(self):
        """Gets the terms_and_conditions_instructions of this BrandRequirements.  # noqa: E501

        Terms and Conditions Instructions  # noqa: E501

        :return: The terms_and_conditions_instructions of this BrandRequirements.  # noqa: E501
        :rtype: str
        """
        return self._terms_and_conditions_instructions

    @terms_and_conditions_instructions.setter
    def terms_and_conditions_instructions(self, terms_and_conditions_instructions):
        """Sets the terms_and_conditions_instructions of this BrandRequirements.

        Terms and Conditions Instructions  # noqa: E501

        :param terms_and_conditions_instructions: The terms_and_conditions_instructions of this BrandRequirements.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and terms_and_conditions_instructions is None:
            raise ValueError("Invalid value for `terms_and_conditions_instructions`, must not be `None`")  # noqa: E501

        self._terms_and_conditions_instructions = terms_and_conditions_instructions

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
        if issubclass(BrandRequirements, dict):
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
        if not isinstance(other, BrandRequirements):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BrandRequirements):
            return True

        return self.to_dict() != other.to_dict()
