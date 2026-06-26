from pydantic import BaseModel
from pydantic import BaseModel


class EventRequest(BaseModel):
    event: str


class ConversationRequest(BaseModel):
    event: str
    interest: str


class FactResponse(BaseModel):
    verified: bool
    topic: str
    summary: str


class FeedbackRequest(BaseModel):
    feedback: str


class HealthResponse(BaseModel):
    status: str
    version: str
    