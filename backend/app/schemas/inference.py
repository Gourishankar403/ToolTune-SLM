from pydantic import BaseModel, Field
from typing import Any


class InferenceRequest(BaseModel):
    instruction: str = Field(
        ...,
        min_length=1,
        description="Natural language instruction"
    )


class ToolCall(BaseModel):
    tool_name: str
    arguments: dict[str, Any]
    confidence: float = Field(
        ge=0.0,
        le=1.0
    )


class InferenceResponse(BaseModel):
    instruction: str
    tool_call: ToolCall
    model_name: str