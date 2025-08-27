from __future__ import annotations
from typing import Optional


class VerificationResult:
    """
    Outcome of signature verification.

    Attributes:
        ok: True if the signature verification passed.
        error: Optional exception raised by the verifier. None when ok=True.
    """
    ok: bool
    error: Optional[Exception] = None

    def __init__(self, ok: bool, error: Optional[Exception] = None):
        self.ok = ok
        self.error = error

    @staticmethod
    def passed() -> "VerificationResult":
        return VerificationResult(ok=True, error=None)

    @staticmethod
    def failed(error: Optional[Exception] = None) -> "VerificationResult":
        return VerificationResult(ok=False, error=error)