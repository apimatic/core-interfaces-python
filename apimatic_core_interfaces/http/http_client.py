from abc import ABC, abstractmethod

from pydantic import validate_call

from apimatic_core_interfaces.configuration.endpoint_configuration import EndpointConfiguration
from apimatic_core_interfaces.http.http_request import HttpRequest
from apimatic_core_interfaces.http.http_response import HttpResponse


class HttpClient(ABC):
    """An interface for the methods that an HTTP Client must implement

    This class should not be instantiated but should be used as a base class
    for HTTP Client classes.

    """

    @abstractmethod
    @validate_call
    def execute(self, request: HttpRequest, endpoint_configuration: EndpointConfiguration):
        """Execute a given CoreHttpRequest to get a string response back

        Args:
            request (HttpRequest): The given HttpRequest to execute.
            endpoint_configuration (EndpointConfiguration): The endpoint configurations to use.

        Returns:
            HttpResponse: The response of the CoreHttpRequest.

        """
        ...

    @abstractmethod
    @validate_call
    def convert_response(self, response: HttpResponse, contains_binary_response: bool, request: HttpRequest):
        """Converts the Response object of the HttpClient into an
        HttpResponse object.

        Args:
            response (dynamic): The original response object.
            contains_binary_response (bool): The flag to check if the response is of binary type.
            request (HttpRequest): The original HttpRequest object.

        Returns:
            HttpResponse: The converted HttpResponse object.

        """
        ...
