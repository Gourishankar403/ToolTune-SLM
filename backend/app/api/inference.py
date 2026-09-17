from fastapi import APIRouter

from app.schemas.inference import (
    InferenceRequest,
    InferenceResponse,
)

from app.services.inference_service import (
    generate_mock_tool_call,
)


router = APIRouter(
    prefix="/inference",
    tags=["Inference"],
)


@router.post(
    "/",
    response_model=InferenceResponse,
)
def run_inference(
    request: InferenceRequest,
):
    return generate_mock_tool_call(request)