# coding: utf-8

"""
    Tango Card RaaS API

    <5. Ordersp>Welcome to the RaaS&reg; API – with this RESTful API you can integrate a global reward or incentive program into your app or platform.<br /><br /> This console works in our Sandbox environment. To receive your own credentials or to ask questions, please contact us at <a href=\"mailto:devsupport@tangocard.com\">devsupport@tangocard.com</a>.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "tango-client"
VERSION = "2.1.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Tango Card RaaS API",
    author_email="",
    url="",
    keywords=["Swagger", "Tango Card RaaS API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    &lt;5. Ordersp&gt;Welcome to the RaaS&amp;reg; API – with this RESTful API you can integrate a global reward or incentive program into your app or platform.&lt;br /&gt;&lt;br /&gt; This console works in our Sandbox environment. To receive your own credentials or to ask questions, please contact us at &lt;a href&#x3D;\&quot;mailto:devsupport@tangocard.com\&quot;&gt;devsupport@tangocard.com&lt;/a&gt;.  # noqa: E501
    """
)
