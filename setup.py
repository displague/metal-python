# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "metal"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="Metal API",
    author_email="support@equinixmetal.com",
    url="",
    keywords=["OpenAPI", "Metal API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['metal=metal.__main__:main']},
    long_description="""\
    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at &lt;https://api.equinix.com/metal/v1&gt;. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at &lt;https://metal.equinix.com/developers/api&gt;.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the &#x60;page&#x60; and &#x60;per_page&#x60; query parameters.  The &#x60;page&#x60; parameter is used to specify the page number. The first page is &#x60;1&#x60;. The &#x60;per_page&#x60; parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the &#x60;sort_by&#x60; query parameter with the root level field name as the value. The &#x60;sort_direction&#x60; parameter is used to specify the sort direction, either either &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the &#x60;type&#x60; field, as in the following request:  &#x60;&#x60;&#x60;sh curl -H &#39;X-Auth-Token: my_authentication_token&#39; \\   https://api.equinix.com/metal/v1/projects/id/ips?type&#x3D;public_ipv4 &#x60;&#x60;&#x60;  Only IP addresses with the &#x60;type&#x60; field set to &#x60;public_ipv4&#x60; will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. The fields available for search differ by resource, as does the search strategy.  To search resources you can use the &#x60;search&#x60; query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns &#x60;href&#x60; values (API links) to the associated resource.  &#x60;&#x60;&#x60;json {   ...   \&quot;project\&quot;: {     \&quot;href\&quot;: \&quot;/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\&quot;   } } &#x60;&#x60;&#x60;  If you&#39;re going need the project details, you can avoid a second API request.  Specify the contained &#x60;href&#x60; resources and collections that you&#39;d like to have included in the response using the &#x60;include&#x60; query parameter.  For example:  &#x60;&#x60;&#x60;sh curl -H &#39;X-Auth-Token: my_authentication_token&#39; \\   https://api.equinix.com/metal/v1/user?include&#x3D;projects &#x60;&#x60;&#x60;  The &#x60;include&#x60; parameter is generally accepted in &#x60;GET&#x60;, &#x60;POST&#x60;, &#x60;PUT&#x60;, and &#x60;PATCH&#x60; requests where &#x60;href&#x60; resources are presented.  To have multiple resources include, use a comma-separated list (e.g. &#x60;?include&#x3D;emails,projects,memberships&#x60;).  &#x60;&#x60;&#x60;sh curl -H &#39;X-Auth-Token: my_authentication_token&#39; \\   https://api.equinix.com/metal/v1/user?include&#x3D;emails,projects,memberships &#x60;&#x60;&#x60;  You may also include nested associations up to three levels deep using dot notation (&#x60;?include&#x3D;memberships.projects&#x60;):  &#x60;&#x60;&#x60;sh curl -H &#39;X-Auth-Token: my_authentication_token&#39; \\   https://api.equinix.com/metal/v1/user?include&#x3D;memberships.projects &#x60;&#x60;&#x60;  To exclude resources, and optimize response delivery, use the &#x60;exclude&#x60; query parameter. The &#x60;exclude&#x60; parameter is generally accepted in &#x60;GET&#x60;, &#x60;POST&#x60;, &#x60;PUT&#x60;, and &#x60;PATCH&#x60; requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an &#x60;href&#x60; field. 
    """
)

