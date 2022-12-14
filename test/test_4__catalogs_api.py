# coding: utf-8

"""
    Tango Card RaaS API

    <p>Welcome to the RaaS&reg; API – with this RESTful API you can integrate a global reward or incentive program into your app or platform.<br /><br /> This console works in our Sandbox environment. To receive your own credentials or to ask questions, please contact us at <a href=\"mailto:devsupport@tangocard.com\">devsupport@tangocard.com</a>.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import tango_client
from tango_client.api.4__catalogs_api import 4CatalogsApi  # noqa: E501
from tango_client.rest import ApiException


class Test4CatalogsApi(unittest.TestCase):
    """4CatalogsApi unit test stubs"""

    def setUp(self):
        self.api = tango_client.api.4__catalogs_api.4CatalogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_catalog(self):
        """Test case for get_catalog

        Get all items in the Platform's Catalog.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
