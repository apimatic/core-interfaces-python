from abc import ABC, abstractmethod

from pydantic import validate_call

from apimatic_core_interfaces.http.http_request import HttpRequest


class Authentication(ABC):

    @abstractmethod
    def is_valid(self):
        ...

    @abstractmethod
    @validate_call
    def apply(self, http_request: HttpRequest):
        ...
