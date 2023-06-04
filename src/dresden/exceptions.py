"""Asynchronous Python client providing Open Data information of Dresden."""


class ODPDresdenError(Exception):
    """Generic Open Data Platform Dresden exception."""


class ODPDresdenConnectionError(ODPDresdenError):
    """Open Data Platform Dresden - connection error."""
