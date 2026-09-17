from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="ToolTune-SLM API",
    description="LLM Fine-Tuning and LLMOps Platform",
    version="0.1.0"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to ToolTune-SLM API"
    }


from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="ToolTune-SLM API",
    version="0.1.0"
)

app.include_router(health_router)