from abc import abstractmethod

from apimatic_core_interfaces.logger.LogLevel import LogLevel


class Logger(object):

    @abstractmethod
    def log(self, level, message, params):
        """Logs a message with a specified log level and additional parameters.

        Args:
            level (LogLevel): The log level of the message.
            message (str): The message to log.
            params (dict): Additional parameters to include in the log message.
        """
        ...