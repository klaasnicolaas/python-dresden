"""Models for Open Data Platform of Dresden."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

import pytz


@dataclass
class DisabledParking:
    """Object representing a DisabledParking."""

    entry_id: int
    number: int
    usage_time: str
    photo: str
    created_at: datetime | None
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls: type[DisabledParking], data: dict[str, Any]) -> DisabledParking:
        """Return a DisabledParking object from a dictionary.

        Args:
        ----
            data: The data from the API.

        Returns:
        -------
            A DisabledParking object.

        """
        attr = data["properties"]
        geo = data["geometry"]["coordinates"]
        return cls(
            entry_id=int(data["id"]),
            number=attr.get("stellplatzanzahl"),
            usage_time=attr.get("nutzungszeit"),
            photo=attr.get("url_www"),
            created_at=datetime.strptime(
                attr.get("kks_mdd"), "%d.%m.%Y %H:%M:%S"
            ).replace(tzinfo=pytz.timezone("Europe/Berlin"))
            if attr.get("kks_mdd")
            else None,
            longitude=geo[0],
            latitude=geo[1],
        )
