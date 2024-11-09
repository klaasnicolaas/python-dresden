"""Test the models."""

from __future__ import annotations

from aresponses import ResponsesMockServer

from dresden import DisabledParking, ODPDresden

from . import load_fixtures


async def test_all_parking_spaces(
    aresponses: ResponsesMockServer, odp_dresden_client: ODPDresden
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
    assert spaces is not None
    for item in spaces:
        assert isinstance(item, DisabledParking)
        assert item.entry_id is not None
        assert isinstance(item.entry_id, int)
        assert item.number is None or item.number >= 1
        assert item.longitude is not None
        assert isinstance(item.longitude, float)
        assert item.latitude is not None
        assert isinstance(item.latitude, float)
