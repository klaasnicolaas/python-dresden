"""Fixture for the ODP Dresden tests."""

from collections.abc import AsyncGenerator

import pytest
from aiohttp import ClientSession

from dresden import ODPDresden


@pytest.fixture(name="odp_dresden_client")
async def client() -> AsyncGenerator[ODPDresden, None]:
    """Return an ODP Dresden client."""
    async with (
        ClientSession() as session,
        ODPDresden(session=session) as odp_dresden_client,
    ):
        yield odp_dresden_client
