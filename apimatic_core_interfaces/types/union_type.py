from abc import ABC, abstractmethod

from typing import List, Any, Set, Type

from typing_extensions import Self

from apimatic_core_interfaces.types.union_type_context import UnionTypeContext


class UnionType(ABC):
    NATIVE_TYPES: List[Type] = [int, str, float, bool]

    def __init__(self, union_types: List[Self], union_type_context: UnionTypeContext):
        self._union_types = union_types
        self._union_type_context = union_type_context
        self.is_valid: bool = False
        self.error_messages: Set[str] = set()

    @abstractmethod
    def validate(self, value: Any) -> Self:
        ...

    @abstractmethod
    def deserialize(self, value: Any) -> Any:
        ...

    def get_context(self) -> UnionTypeContext:
        return self._union_type_context
