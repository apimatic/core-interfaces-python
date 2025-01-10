from abc import ABC, abstractmethod

from typing import List, Any

from pydantic import validate_call

from apimatic_core_interfaces.types.union_type_context import UnionTypeContext


class UnionType(ABC):
    NATIVE_TYPES: List[type] = [int, str, float, bool]

    def __init__(self, union_types: List['UnionType'], union_type_context: UnionTypeContext):
        self._union_types = union_types
        self._union_type_context = union_type_context
        self.is_valid = False
        self.error_messages = set()

    @abstractmethod
    @validate_call
    def validate(self, value: Any) -> bool:
        ...

    @abstractmethod
    @validate_call
    def deserialize(self, value: Any) -> Any:
        ...

    def get_context(self) -> UnionTypeContext:
        return self._union_type_context
