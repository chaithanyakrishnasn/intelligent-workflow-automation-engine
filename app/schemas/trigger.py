from pydantic import BaseModel
from typing import Optional


class TriggerCreate(BaseModel):
    type: str
    config: Optional[str] = None


class TriggerResponse(BaseModel):
    id: int
    type: str
    config: Optional[str]
    workflow_id: int

    class Config:
        from_attributes = True