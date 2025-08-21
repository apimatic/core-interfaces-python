from abc import ABC, abstractmethod
from typing import Mapping

class SignatureVerifier(ABC):
    """
    Abstract base class for signature verification.

    Implementations must validate that the provided JSON payload matches
    the signature contained in the headers.
    """

    @abstractmethod
    def verify(self, headers: Mapping[str, str], payload: str) -> bool:
        """
        Verify the signature for a given JSON payload and headers.

        Args:
            headers (Mapping[str, str]): HTTP headers containing signature fields.
            payload (str): Raw request body as a JSON string.

        Returns:
            bool: True if the signature is valid; False otherwise.
        """
        raise NotImplementedError
