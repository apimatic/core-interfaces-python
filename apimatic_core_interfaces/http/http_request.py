from apimatic_core_interfaces.http.http_method_enum import HttpMethodEnum
from pydantic import BaseModel, validate_call, Field
from typing import Optional, Dict, List, Any, Tuple, Union


class HttpRequest(BaseModel):
    """Information about an HTTP Request including its method, headers,
        parameters, URL, and Basic Auth details

    Attributes:
        http_method (HttpMethodEnum): The HTTP Method that this request should
            perform when called.
        query_url (string): The URL that the request should be sent to.
        headers (dict): A dictionary of headers (key : value) that should be
            sent along with the request.
        query_parameters (dict): A dictionary of request query parameters.
        parameters (dict): A dictionary of parameters that are to be sent along
            with the request in the body of the request
        files (dict): A dictionary of files that are to be sent in the multipart requests.

    """

    http_method: HttpMethodEnum
    query_url: str
    headers: Dict[str, Any] = Field(default_factory=dict)
    query_parameters: Dict[str, Any] = Field(default_factory=dict)
    parameters: Any = None
    files: Any = None

    @validate_call
    def add_header(self, name: str, value: str):
        """ Add a header to the HttpRequest.

        Args:
            name (string): The name of the header.
            value (string): The value of the header.

        """
        self.headers[name] = value

    def __repr__(self) -> str:
        return str(self.__dict__)