from abc import abstractmethod

from typing import Any, Dict

from pydantic import validate_call


class Logger:
    """An interface for the generic logger facade.

    This class should not be instantiated but should be used as a base class
    for Logger classes."""

    @abstractmethod
    @validate_call
    def log(self, level: int, message: str, params: Dict[str, Any]):
        """Logs a message with a specified log level and additional parameters.

        Args:
            level (int): The log level of the message.
            message (str): The message to log.
            params (dict): Additional parameters to include in the log message.
        """
        ...