# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Dresden."""

import asyncio

from dresden import ODPDresden


async def main() -> None:
    """Show example on using the Dresden API client."""
    async with ODPDresden() as client:
        disabled_parkings = await client.disabled_parkings(limit=500)

        count: int = len(disabled_parkings)
        for item in disabled_parkings:
            print(item)

        # Count unique id's in disabled_parkings
        unique_values = [str(item.entry_id) for item in disabled_parkings]
        num_values = len(set(unique_values))

        print("__________________________")
        print(f"Total locations found: {count}")
        print(f"Unique ID values: {num_values}")


if __name__ == "__main__":
    asyncio.run(main())
