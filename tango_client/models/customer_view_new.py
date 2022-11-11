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


class CustomerViewNew(object):
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
        'created_at': 'str',
        'customer_identifier': 'str',
        'display_name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'customer_identifier': 'customerIdentifier',
        'display_name': 'displayName',
        'status': 'status'
    }

    def __init__(self, created_at=None, customer_identifier=None, display_name=None, status=None, _configuration=None):  # noqa: E501
        """CustomerViewNew - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._customer_identifier = None
        self._display_name = None
        self._status = None
        self.discriminator = None

        self.created_at = created_at
        self.customer_identifier = customer_identifier
        self.display_name = display_name
        self.status = status

    @property
    def created_at(self):
        """Gets the created_at of this CustomerViewNew.  # noqa: E501

        Created Date  # noqa: E501

        :return: The created_at of this CustomerViewNew.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CustomerViewNew.

        Created Date  # noqa: E501

        :param created_at: The created_at of this CustomerViewNew.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def customer_identifier(self):
        """Gets the customer_identifier of this CustomerViewNew.  # noqa: E501

        Customer Identifier  # noqa: E501

        :return: The customer_identifier of this CustomerViewNew.  # noqa: E501
        :rtype: str
        """
        return self._customer_identifier

    @customer_identifier.setter
    def customer_identifier(self, customer_identifier):
        """Sets the customer_identifier of this CustomerViewNew.

        Customer Identifier  # noqa: E501

        :param customer_identifier: The customer_identifier of this CustomerViewNew.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_identifier is None:
            raise ValueError("Invalid value for `customer_identifier`, must not be `None`")  # noqa: E501

        self._customer_identifier = customer_identifier

    @property
    def display_name(self):
        """Gets the display_name of this CustomerViewNew.  # noqa: E501

        Customer Display Name  # noqa: E501

        :return: The display_name of this CustomerViewNew.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CustomerViewNew.

        Customer Display Name  # noqa: E501

        :param display_name: The display_name of this CustomerViewNew.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def status(self):
        """Gets the status of this CustomerViewNew.  # noqa: E501

        Customer Status  # noqa: E501

        :return: The status of this CustomerViewNew.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CustomerViewNew.

        Customer Status  # noqa: E501

        :param status: The status of this CustomerViewNew.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(CustomerViewNew, dict):
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
        if not isinstance(other, CustomerViewNew):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerViewNew):
            return True

        return self.to_dict() != other.to_dict()
