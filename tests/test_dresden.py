"""Basic tests for the Urban Data Platform API of Dresden."""
# pylint: disable=protected-access
import asyncio
from unittest.mock import patch

import pytest
from aiohttp import ClientError, ClientResponse, ClientSession
from aresponses import Response, ResponsesMockServer

from dresden import ODPDresden
from dresden.exceptions import ODPDresdenConnectionError, ODPDresdenError

from . import load_fixtures


async def test_json_request(aresponses: ResponsesMockServer) -> None:
    """Test JSON response is handled correctly."""
    aresponses.add(
        "kommisdd.dresden.de",
        "/net4/public/ogcapi/collections/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/geo+json"},
            text=load_fixtures("disabled_parking.geojson"),
        ),
    )
    async with ClientSession() as session:
        client = ODPDresden(session=session)
        response = await client._request("test")
        assert response is not None
        await client.close()


async def test_internal_session(aresponses: ResponsesMockServer) -> None:
    """Test internal session is handled correctly."""
    aresponses.add(
        "kommisdd.dresden.de",
        "/net4/public/ogcapi/collections/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/geo+json"},
            text=load_fixtures("disabled_parking.geojson"),
        ),
    )
    async with ODPDresden() as client:
        await client._request("test")


async def test_timeout(aresponses: ResponsesMockServer) -> None:
    """Test request timeout from the Urban Data Platform API of Dresden."""

    # Faking a timeout by sleeping
    async def response_handler(_: ClientResponse) -> Response:
        await asyncio.sleep(0.2)
        return aresponses.Response(
            body="Goodmorning!",
            text=load_fixtures("disabled_parking.geojson"),
        )

    aresponses.add(
        "kommisdd.dresden.de",
        "/net4/public/ogcapi/collections/test",
        "GET",
        response_handler,
    )

    async with ClientSession() as session:
        client = ODPDresden(
            session=session,
            request_timeout=0.1,
        )
        with pytest.raises(ODPDresdenConnectionError):
            assert await client._request("test")


async def test_content_type(aresponses: ResponsesMockServer) -> None:
    """Test request content type error from Urban Data Platform API of Dresden."""
    aresponses.add(
        "kommisdd.dresden.de",
        "/net4/public/ogcapi/collections/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "blabla/blabla"},
        ),
    )

    async with ClientSession() as session:
        client = ODPDresden(session=session)
        with pytest.raises(ODPDresdenError):
            assert await client._request("test")


async def test_client_error() -> None:
    """Test request client error from the Urban Data Platform API of Dresden."""
    async with ClientSession() as session:
        client = ODPDresden(session=session)
        with patch.object(
            session,
            "request",
            side_effect=ClientError,
        ), pytest.raises(ODPDresdenConnectionError):
            assert await client._request("test")
