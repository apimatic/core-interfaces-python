from abc import ABC, abstractmethod

from apimatic_core_interfaces.http.request import Request
from apimatic_core_interfaces.security.verification_result import VerificationResult


class SignatureVerifier(ABC):
    """
    Abstract base class for signature verification.

    Implementations must validate that the provided JSON payload matches
    the signature contained in the headers.
    """

    @abstractmethod
    def verify(self, request: Request) -> VerificationResult:
        """
        Perform signature verification.

        Returns:
            VerificationResult: ok=True when the signature is valid; ok=False with the
            underlying exception (if any) when invalid or an error occurred.

        Notes:
            Implementations should NOT raise for runtime verification outcomes; return
            VerificationResult.failed(error) instead. Reserve raising for programmer
            errors (invalid construction/config).
        """
        raise NotImplementedError
