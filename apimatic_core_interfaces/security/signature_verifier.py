from abc import ABC, abstractmethod

from apimatic_core_interfaces.http.request import Request


class SignatureVerifier(ABC):
    """
    Abstract base class for signature verification.

    Implementations must validate that the provided JSON payload matches
    the signature contained in the headers.
    """

    @abstractmethod
    def verify(self, request: Request) -> bool:
        """Validate the request signature.

        Args:
            request: The incoming event request wrapper.

        Returns:
            True if the request passes this verifier; otherwise False.
        """
        raise NotImplementedError
