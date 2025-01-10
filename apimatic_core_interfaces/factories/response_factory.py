from abc import ABC, abstractmethod

from typing import Dict

from apimatic_core_interfaces.http.http_request import HttpRequest


class ResponseFactory(ABC):

    @abstractmethod
    def create(self, status_code: int, reason: str, headers: Dict[str, str], body: str, request: HttpRequest):
        ...
