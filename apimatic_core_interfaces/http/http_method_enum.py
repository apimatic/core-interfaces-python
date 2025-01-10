from pydantic import validate_call


class HttpMethodEnum(object):
    """Enumeration of an HTTP Method

    Attributes:
        GET: A GET Request
        POST: A POST Request
        PUT: A PUT Request
        PATCH: A PATCH Request
        DELETE: A DELETE Request

    """

    GET: str = "GET"

    POST: str = "POST"

    PUT: str = "PUT"

    PATCH: str = "PATCH"

    DELETE: str = "DELETE"

    HEAD: str = "HEAD"

    @classmethod
    @validate_call
    def to_string(cls, http_method: str):
        """Returns the string equivalent for the Enum.

        """
        for k, v in list(vars(cls).items()):
            if v == http_method:
                return k

    @classmethod
    @validate_call
    def from_string(cls, value: str):
        """Creates an instance of the Enum from a given string.

        """
        return getattr(cls, value.upper(), None)