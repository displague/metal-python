from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.recovery_code_list import RecoveryCodeList
from metal import util


async def find_ensure_otp(request: web.Request, otp) -> web.Response:
    """Verify user by providing an OTP

    It verifies the user once a valid OTP is provided. It gives back a session token, essentially logging in the user.

    :param otp: OTP
    :type otp: str

    """
    return web.Response(status=200)


async def find_recovery_codes(request: web.Request, ) -> web.Response:
    """Retrieve my recovery codes

    Returns my recovery codes.


    """
    return web.Response(status=200)


async def receive_codes(request: web.Request, ) -> web.Response:
    """Receive an OTP per sms

    Sends an OTP to the user&#39;s mobile phone.


    """
    return web.Response(status=200)


async def regenerate_codes(request: web.Request, ) -> web.Response:
    """Generate new recovery codes

    Generate a new set of recovery codes.


    """
    return web.Response(status=200)
