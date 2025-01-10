from abc import abstractmethod

from pydantic import validate_call

from apimatic_core_interfaces.types.http_request import HttpRequest
from apimatic_core_interfaces.types.http_response import HttpResponse


class ApiLogger:
    """An interface for logging API requests and responses.

    This class should not be instantiated but should be used as a base class
    for API Logger classes."""

    @abstractmethod
    @validate_call
    def log_request(self, http_request: HttpRequest):
        """Logs the given HTTP request.

        Args:
            http_request (HttpRequest): The HTTP request to log.
        """
        ...

    @abstractmethod
    @validate_call
    def log_response(self, http_response: HttpResponse):
        """Logs the given HTTP response.

        Args:
            http_response (HttpRequest): The HTTP request to log.
        """
        ...