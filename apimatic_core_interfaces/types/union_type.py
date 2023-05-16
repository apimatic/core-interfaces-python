from abc import ABC, abstractmethod
from apimatic_core.types.union_types.union_type_context import UnionTypeContext


class UnionType(ABC):
    NATIVE_TYPES = [int, str, float, bool]

    def __init__(self, union_types, union_type_context: UnionTypeContext):
        self._union_types = union_types
        self._union_type_context = union_type_context
        self.is_valid = False

    @abstractmethod
    def validate(self, value):
        ...

    @abstractmethod
    def deserialize(self, value):
        ...
