from pydantic import BaseModel
from typing import Optional, Callable, Any

from apimatic_core_interfaces.formats.datetime_format import DateTimeFormat


class UnionTypeContext(BaseModel):
    is_array: bool = False
    is_dict: bool = False
    is_array_of_dict: bool = False
    is_optional: bool = False
    is_nullable: bool = False
    discriminator: Optional[str] = None
    discriminator_value: Optional[str] = None
    date_time_format: Optional[DateTimeFormat] = None
    date_time_converter: Optional[Callable[[Any], Any]] = None
    is_nested: bool = False

    @property
    def is_nullable_or_optional(self):
        return self.is_nullable or self.is_optional

    @classmethod
    def create(cls, is_array=False, is_dict=False, is_array_of_dict=False, is_optional=False, is_nullable=False,
               discriminator=None, discriminator_value=None, date_time_format=None, date_time_converter=None):
        return cls(is_array=is_array, is_dict=is_dict, is_array_of_dict=is_array_of_dict, is_optional=is_optional,
                   is_nullable=is_nullable, discriminator=discriminator, discriminator_value=discriminator_value,
                   date_time_format=date_time_format, date_time_converter=date_time_converter)
