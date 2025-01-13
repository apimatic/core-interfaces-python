from pydantic import BaseModel

class EndpointConfiguration(BaseModel):
    has_binary_response: bool = False
    should_retry: bool = False
