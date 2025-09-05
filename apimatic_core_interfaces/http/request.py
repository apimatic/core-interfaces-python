from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class Request:
    """
    Compact, framework-agnostic HTTP request snapshot (files excluded).

    Fields:
      - method, path, url
      - headers: Dict[str, str]            (copied; later mutations on the original won't leak)
      - raw_body: bytes                    (wire bytes; frameworks cache safely)
      - query/form: Dict[str, List[str]>   (multi-value safe)
      - cookies: Dict[str, str]
    """
    method: str
    path: str
    url: Optional[str]
    headers: Dict[str, str]
    raw_body: bytes
    query: Dict[str, List[str]] = field(default_factory=dict)
    cookies: Dict[str, str] = field(default_factory=dict)
    form: Dict[str, List[str]] = field(default_factory=dict)

    # ---------- helpers ----------

    @staticmethod
    def _as_listdict(obj: Any) -> Dict[str, List[str]]:
        """MultiDict/QueryDict → Dict[str, List[str]]; Mapping[str,str] → {k:[v]}."""
        if not obj:
            return {}
        getlist = getattr(obj, "getlist", None)
        if callable(getlist):
            return {k: list(getlist(k)) for k in obj.keys()}
        return {k: [obj[k]] for k in obj.keys()}

    # ---------- factories (non-destructive) ----------

    @staticmethod
    async def from_fastapi_request(request) -> "Request":
        """
        Build from fastapi.Request / starlette.requests.Request.

        - raw body via await req.body() (Starlette caches; non-destructive)
        - parse form *only text fields* when content-type is form-like
        - **file parts are ignored by design**
        - copy mappings so later mutations on the original request won't leak
        """
        headers = dict(request.headers)
        raw = await request.body()
        query = Request._as_listdict(request.query_params)
        cookies = dict(request.cookies)
        url_str = str(request.url)
        path = request.url.path

        ct = (headers.get("content-type") or headers.get("Content-Type") or "").lower()
        parse_form = ct.startswith(("multipart/form-data", "application/x-www-form-urlencoded"))

        form: Dict[str, List[str]] = {}
        if parse_form:
            formdata = await request.form()
            # Only text fields; ignore UploadFile instances
            for k in formdata.keys():
                values = formdata.getlist(k)
                for v in values:
                    is_upload = hasattr(v, "filename") and hasattr(v, "read")
                    if not is_upload:
                        form.setdefault(k, []).append(str(v))

        return Request(
            method=request.method,
            path=path,
            url=url_str,
            headers=headers,
            raw_body=raw,
            query=query,
            cookies=cookies,
            form=form,
        )

    @staticmethod
    def from_django_request(request) -> "Request":
        """
        Build from django.http.HttpRequest.

        - uses req.body (cached bytes; non-destructive)
        - text fields from req.POST
        - **req.FILES is ignored by design**
        - copies mappings to avoid leaking later mutations
        """
        headers = dict(getattr(request, "headers", {}) or {})
        url_str = request.build_absolute_uri()
        path = request.path
        raw = bytes(getattr(request, "body", b"") or b"")
        query = Request._as_listdict(getattr(request, "GET", {}))
        cookies = dict(getattr(request, "COOKIES", {}) or {})
        form = Request._as_listdict(getattr(request, "POST", {}))

        return Request(
            method=request.method,
            path=path,
            url=url_str,
            headers=headers,
            raw_body=raw,
            query=query,
            cookies=cookies,
            form=form,
        )

    @staticmethod
    def from_flask_request(request) -> "Request":
        """
        Build from flask.Request (Werkzeug).

        - uses req.get_data(cache=True) (non-destructive)
        - text fields from req.form
        - **req.files is ignored by design**
        - copies mappings to avoid leaking later mutations
        """
        headers = dict(request.headers)
        url_str = getattr(request, "url", None)
        path = request.path
        raw = request.get_data(cache=True)
        query = Request._as_listdict(request.args)
        cookies = dict(request.cookies)
        form = Request._as_listdict(request.form)

        return Request(
            method=request.method,
            path=path,
            url=url_str,
            headers=headers,
            raw_body=raw,
            query=query,
            cookies=cookies,
            form=form,
        )