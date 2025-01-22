from abc import ABC, abstractmethod
from typing import Dict

from apimatic_core_interfaces.http.http_request import HttpRequest


class Authentication(ABC):

    @property
    @abstractmethod
    def error_message(self) -> str:
        ...

    @abstractmethod
    def is_valid(self):
        ...

    @abstractmethod
    def with_auth_managers(self, auth_managers: Dict[str, 'Authentication']):
        ...

    @abstractmethod
    def apply(self, http_request: HttpRequest):
        ...
