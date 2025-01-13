from pydantic import BaseModel
from typing import Optional

class EndpointConfiguration(BaseModel):
    has_binary_response: Optional[bool] = None
    should_retry: Optional[bool] = None
