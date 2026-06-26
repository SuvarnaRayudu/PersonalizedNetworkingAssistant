from fastapi import APIRouter
from backend.services.event_analyzer import analyze_event
from backend.services.fact_checker import verify_topic

from backend.models.schemas import (
    EventRequest,
    ConversationRequest,
    FactRequest,
    FactResponse
)

router = APIRouter()


@router.get("/")
async def root():
    return {
        "message": "Personalized Networking Assistant API"
    }


@router.get("/health")
async def health():
    return {
        "status": "Running"
    }


@router.post("/analyze-event")
async def analyze_event_route(request: EventRequest):

    themes = analyze_event(request.event)

    return {
        "event": request.event,
        "themes": themes
    }
    

@router.post("/fact-check", response_model=FactResponse)
async def fact_check(request: FactRequest):

    return verify_topic(request.topic)


@router.post("/generate-conversation")
async def generate(request: ConversationRequest):

    return {
        "event": request.event,
        "interest": request.interest,
        "message": "GPT2 Generator coming in Part-4"
    }