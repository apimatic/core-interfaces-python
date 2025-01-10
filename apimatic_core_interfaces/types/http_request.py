from apimatic_core_interfaces.types.http_method_enum import HttpMethodEnum
from pydantic import BaseModel
from typing import Optional, Dict, List, Any, Tuple


class HttpRequest(BaseModel):
    """Information about an HTTP Request including its method, headers,
        parameters, URL, and Basic Auth details

    Attributes:
        http_method (HttpMethodEnum): The HTTP Method that this request should
            perform when called.
        headers (dict): A dictionary of headers (key : value) that should be
            sent along with the request.
        query_url (string): The URL that the request should be sent to.
        parameters (dict): A dictionary of parameters that are to be sent along
            with the request in the form body of the request

    """

    http_method: str
    query_url: str
    headers: Optional[Dict[str, str]] = None
    query_parameters: Optional[Dict[str, Any]] = None
    parameters: Optional[List[Tuple[str, Any]]] = None
    files: Optional[Dict[str, Any]] = None