# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class PaginationDataManager(ABC):
    """An interface for managing pagination in API responses.

    This class should not be instantiated directly but should be subclassed
    to provide specific pagination management logic for paginated API responses.
    """

    @abstractmethod
    def is_valid(self, paginated_data):
        """Checks if the given paginated data contains a valid next page.

        Args:
            paginated_data: The paginated response data to check.

        Returns:
            bool: True if the paginated data is valid and has a next page, False otherwise.
        """
        ...

    @abstractmethod
    def get_next_request_builder(self, paginated_data):
        """Builds the HTTP request for fetching the next page of data.

        Args:
            paginated_data: The current paginated response data.

        Returns:
            HttpRequest.Builder: A builder instance configured to request the next page.
        """
        ...
