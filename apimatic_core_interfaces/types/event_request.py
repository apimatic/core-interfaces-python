from typing import Mapping, Optional


class EventRequest:
    """Lightweight request wrapper for webhook event parsing.

    This wrapper keeps the library independent of any specific web framework.
    Callers should populate it from their framework's request object.

    Attributes:
        headers: Mapping of HTTP header names to values. Header names are
            treated case-insensitively by verifiers.
        body: Raw request body as a JSON string.
        method: Optional HTTP method (e.g., "POST"), if useful for diagnostics.
        path: Optional URL path (e.g., "/orders"), if useful for diagnostics.
    """
    headers: Mapping[str, str]
    body: str
    method: Optional[str] = None
    path: Optional[str] = None

    def __init__(self, headers: Mapping[str, str], body: str, method: Optional[str] = None,
                 path: Optional[str] = None) -> None:
        self.headers = headers
        self.body = body
        self.method = method
        self.path = path