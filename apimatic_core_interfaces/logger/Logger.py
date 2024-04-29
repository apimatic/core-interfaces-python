from abc import abstractmethod


class Logger(object):

    @abstractmethod
    def log(self, level, message, params):
        """Logs a message with a specified log level and additional parameters.

        Args:
            level (int): The log level of the message.
            message (str): The message to log.
            params (dict): Additional parameters to include in the log message.
        """
        ...