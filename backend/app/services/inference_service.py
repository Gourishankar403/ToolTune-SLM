from app.schemas.inference import (
    InferenceRequest,
    InferenceResponse,
    ToolCall,
)


def generate_mock_tool_call(
    request: InferenceRequest,
) -> InferenceResponse:

    instruction = request.instruction.lower()

    if "weather" in instruction:
        tool_call = ToolCall(
            tool_name="get_weather",
            arguments={
                "location": "Chennai"
            },
            confidence=0.95,
        )

    else:
        tool_call = ToolCall(
            tool_name="unknown",
            arguments={},
            confidence=0.30,
        )

    return InferenceResponse(
        instruction=request.instruction,
        tool_call=tool_call,
        model_name="mock-model-v0.1",
    )