from abc import abstractmethod

class ApiLogger:

    @abstractmethod
    def log_request(self, http_request):
        """Logs the given HTTP request.

        Args:
            http_request (HttpRequest): The HTTP request to log.
        """
        ...

    @abstractmethod
    def log_response(self, http_response):
        """Logs the given HTTP response.

        Args:
            http_response (HttpRequest): The HTTP request to log.
        """
        ...