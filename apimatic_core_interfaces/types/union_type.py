from abc import ABC, abstractmethod


class UnionType(ABC):
    NATIVE_TYPES = [int, str, float, bool]
    NONE_MATCHED_ERROR_MESSAGE = 'We could not match any acceptable types against the given JSON.'
    MORE_THAN_1_MATCHED_ERROR_MESSAGE = 'There are more than one acceptable type matched against the given JSON.'

    def __init__(self, union_types, union_type_context):
        self._union_types = union_types
        self._union_type_context = union_type_context
        self.is_valid = False
        self.error_messages = None

    @abstractmethod
    def validate(self, value):
        ...

    @abstractmethod
    def deserialize(self, value):
        ...

    def get_context(self):
        return self._union_type_context
