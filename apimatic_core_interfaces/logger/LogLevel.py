class LogLevel:
  """Defines constants for common log levels."""

  TRACE = 10
  DEBUG = 20
  INFO = 30
  WARNING = 40
  ERROR = 50

  # Define string representations for convenience
  LEVEL_NAMES = {
      TRACE: "TRACE",
      DEBUG: "DEBUG",
      INFO: "INFO",
      WARNING: "WARNING",
      ERROR: "ERROR"
  }

  @classmethod
  def name(cls, level):
    """Returns the string representation of a log level.

    Args:
      level: The integer value of the log level.

    Returns:
      The string representation of the log level, or None if not found.
    """

    return cls.LEVEL_NAMES.get(level)