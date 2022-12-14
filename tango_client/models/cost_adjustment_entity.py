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


class CostAdjustmentEntity(object):
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
        'type': 'str',
        'value': 'float'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, type=None, value=None, _configuration=None):  # noqa: E501
        """CostAdjustmentEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._value = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def type(self):
        """Gets the type of this CostAdjustmentEntity.  # noqa: E501


        :return: The type of this CostAdjustmentEntity.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CostAdjustmentEntity.


        :param type: The type of this CostAdjustmentEntity.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this CostAdjustmentEntity.  # noqa: E501


        :return: The value of this CostAdjustmentEntity.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CostAdjustmentEntity.


        :param value: The value of this CostAdjustmentEntity.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if issubclass(CostAdjustmentEntity, dict):
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
        if not isinstance(other, CostAdjustmentEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CostAdjustmentEntity):
            return True

        return self.to_dict() != other.to_dict()
