"""Asynchronous Python client providing Open Data information of Dresden."""
from __future__ import annotations

import asyncio
import socket
from dataclasses import dataclass
from importlib import metadata
from typing import Any

import aiohttp
import async_timeout
from aiohttp import hdrs
from yarl import URL

from .exceptions import ODPDresdenConnectionError, ODPDresdenError
from .models import DisabledParking


@dataclass
class ODPDresden:
    """Main class for handling data fetchting from Open Data Platform of Dresden."""

    request_timeout: float = 10.0
    session: aiohttp.client.ClientSession | None = None

    _close_session: bool = False

    async def _request(
        self,
        uri: str,
        *,
        method: str = hdrs.METH_GET,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Handle a request to the Open Data Platform API of Dresden.

        Args:
            uri: Request URI, without '/', for example, 'status'
            method: HTTP method to use, for example, 'GET'
            params: Extra options to improve or limit the response.

        Returns:
            A Python dictionary (text) with the response from
            the Open Data Platform API of Dresden.

        Raises:
            ODPDresdenConnectionError: Timeout occurred while
                connecting to the Open Data Platform API.
            ODPDresdenError: If the data is not valid.
        """
        version = metadata.version(__package__)
        url = URL.build(
            scheme="https",
            host="kommisdd.dresden.de",
            path="/net4/public/ogcapi/collections/",
        ).join(URL(uri))

        headers = {
            "Accept": "application/geo+json",
            "User-Agent": f"PythonODPDresden/{version}",
        }

        if self.session is None:
            self.session = aiohttp.ClientSession()
            self._close_session = True

        try:
            async with async_timeout.timeout(self.request_timeout):
                response = await self.session.request(
                    method,
                    url,
                    params=params,
                    headers=headers,
                    ssl=True,
                )
                response.raise_for_status()
        except asyncio.TimeoutError as exception:
            raise ODPDresdenConnectionError(
                "Timeout occurred while connecting to the Open Data Platform API."
            ) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            raise ODPDresdenConnectionError(
                "Error occurred while communicating with Open Data Platform API."
            ) from exception

        content_type = response.headers.get("Content-Type", "")
        if "application/geo+json" not in content_type:
            text = await response.text()
            raise ODPDresdenError(
                "Unexpected content type response from the Open Data Platform API",
                {"Content-Type": content_type, "Response": text},
            )

        return await response.json()

    async def disabled_parkings(self, limit: int = 10) -> list[DisabledParking]:
        """Get list of disabled parkings.

        Args:
            limit: Maximum number of disabled parkings to return.

        Returns:
            A list of disabled parking objects.
        """
        results: list[DisabledParking] = []
        locations = await self._request(
            "L1113/items",
            params={
                "limit": limit,
            },
        )

        for item in locations["features"]:
            results.append(DisabledParking.from_dict(item))
        return results

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> ODPDresden:
        """Async enter.

        Returns:
            The Open Data Platform Dresden object.
        """
        return self

    async def __aexit__(self, *_exc_info: Any) -> None:
        """Async exit.

        Args:
            _exc_info: Exec type.
        """
        await self.close()
