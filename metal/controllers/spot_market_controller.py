from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.spot_market_prices_list import SpotMarketPricesList
from metal.types.spot_market_prices_per_metro_list import SpotMarketPricesPerMetroList
from metal.types.spot_market_request import SpotMarketRequest
from metal.types.spot_market_request_create_input import SpotMarketRequestCreateInput
from metal.types.spot_market_request_list import SpotMarketRequestList
from metal.types.spot_prices_history_report import SpotPricesHistoryReport
from metal import util


async def create_spot_market_request(request: web.Request, id, body) -> web.Response:
    """Create a spot market request

    Creates a new spot market request.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have. For example, if you require a server with a TPM chip, you may specify &#x60;{ \&quot;features\&quot;: { \&quot;tpm\&quot;: \&quot;required\&quot; } }&#x60; (or &#x60;{ \&quot;features\&quot;: [\&quot;tpm\&quot;] }&#x60; in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param body: Spot Market Request to create
    :type body: dict | bytes

    """
    body = SpotMarketRequestCreateInput.from_dict(body)
    return web.Response(status=200)


async def delete_spot_market_request(request: web.Request, id, force_termination=None) -> web.Response:
    """Delete the spot market request

    Deletes the spot market request.

    :param id: SpotMarketRequest UUID
    :type id: str
    :type id: str
    :param force_termination: Terminate associated spot instances
    :type force_termination: bool

    """
    return web.Response(status=200)


async def find_metro_spot_market_prices(request: web.Request, metro=None, plan=None) -> web.Response:
    """Get current spot market prices for metros

    Get Equinix Metal current spot market prices for all metros.

    :param metro: Metro to filter spot market prices
    :type metro: str
    :param plan: Plan to filter spot market prices
    :type plan: str

    """
    return web.Response(status=200)


async def find_spot_market_prices(request: web.Request, facility=None, plan=None) -> web.Response:
    """Get current spot market prices

    Get Equinix Metal current spot market prices.

    :param facility: Facility to check spot market prices
    :type facility: str
    :param plan: Plan to check spot market prices
    :type plan: str

    """
    return web.Response(status=200)


async def find_spot_market_prices_history(request: web.Request, facility, plan, _from, until, metro=None) -> web.Response:
    """Get spot market prices for a given period of time

    Get spot market prices for a given plan and facility in a fixed period of time  *Note: In the &#x60;200&#x60; response, the property &#x60;datapoints&#x60; contains arrays of &#x60;[float, integer]&#x60;.*

    :param facility: Facility to check spot market prices
    :type facility: str
    :param plan: Plan to check spot market prices
    :type plan: str
    :param _from: Timestamp from range
    :type _from: str
    :param until: Timestamp to range
    :type until: str
    :param metro: Metro to check spot market price history
    :type metro: str

    """
    return web.Response(status=200)


async def find_spot_market_request_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a spot market request

    Returns a single spot market request

    :param id: SpotMarketRequest UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def list_spot_market_requests(request: web.Request, id) -> web.Response:
    """List spot market requests

    View all spot market requests for a given project.

    :param id: Project UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
