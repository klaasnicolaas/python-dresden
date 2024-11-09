"""Test the models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from . import load_fixtures

if TYPE_CHECKING:
    from dresden import DisabledParking, ODPDresden


async def test_all_parking_spaces(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    odp_dresden_client: ODPDresden,
) -> None:
    """Test all parking spaces function."""
    aresponses.add(
        "kommisdd.dresden.de",
        "/net4/public/ogcapi/collections/L1113/items",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/geo+json"},
            text=load_fixtures("disabled_parking.geojson"),
        ),
    )
    spaces: list[DisabledParking] = await odp_dresden_client.disabled_parkings()
    assert spaces == snapshot
