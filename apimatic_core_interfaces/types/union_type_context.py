from pydantic import BaseModel
from typing import Optional, Callable, Any

from apimatic_core_interfaces.types.datetime_format import DateTimeFormat


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
