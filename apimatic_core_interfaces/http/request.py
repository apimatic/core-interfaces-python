from typing import Mapping, Optional, Union, Iterable, Any, Dict

Headers = Mapping[str, str]
Cookies = Mapping[str, str]
QueryParams = Mapping[str, Union[str, Iterable[str]]]
FormData = Mapping[str, Union[str, Iterable[str]]]
Files = Mapping[str, Any]  # framework-agnostic placeholder (e.g., Starlette UploadFile)


class Request:
    """
    Framework-agnostic HTTP request snapshot used by verifiers and the webhook manager.

    This class captures all important parts of an HTTP request in a way that does not depend
    on any specific web framework. It is particularly useful for signature verification and
    webhook processing.

    Notes:
        - `body` contains the decoded textual representation of the body (e.g., a JSON string).
          This should be kept exactly as received.
        - `raw_body` contains the raw byte stream if available. Use this for cryptographic
          verification when signatures depend on raw payloads.
        - Header names should be treated case-insensitively when accessed.
    """

    # Required fields
    headers: Optional[Headers] = None
    method: Optional[str] = None
    path: Optional[str] = None
    body: Optional[str] = None

    # Common metadata
    url: Optional[str] = None
    query: Optional[QueryParams] = None
    cookies: Optional[Cookies] = None

    # Optional request bodies
    raw_body: Optional[bytes] = None
    form: Optional[FormData] = None
    files: Optional[Files] = None

    # Arbitrary extensions
    extensions: Optional[Dict[str, Any]] = None

    def __init__(
        self,
        method: Optional[str] = None,
        path: Optional[str] = None,
        headers: Optional[Headers] = None,
        body: Optional[str] = None,
        url: Optional[str] = None,
        query: Optional[QueryParams] = None,
        cookies: Optional[Cookies] = None,
        raw_body: Optional[bytes] = None,
        form: Optional[FormData] = None,
        files: Optional[Files] = None,
        extensions: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize a new request snapshot.

        Args:
            method: HTTP method of the request (e.g., "GET", "POST").
            path: URL path of the request, excluding query parameters.
            headers: Mapping of header keys to values (case-insensitive).
            body: Decoded body content as a string, such as a JSON or XML string.
            url: Full request URL if available.
            query: Mapping of query parameter keys to single or multiple values.
            cookies: Mapping of cookie keys to values.
            raw_body: Raw bytes of the request body, for signature verification.
            form: Parsed form data, if the request contains form fields.
            files: Uploaded files associated with the request.
            extensions: Arbitrary framework-specific or user-defined metadata.
        """
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body
        self.url = url
        self.query = query
        self.cookies = cookies
        self.raw_body = raw_body
        self.form = form
        self.files = files
        self.extensions = extensions
