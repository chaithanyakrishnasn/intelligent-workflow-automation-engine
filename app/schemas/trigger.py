from pydantic import BaseModel
from typing import Optional
from app.core.enums import TriggerType


class TriggerCreate(BaseModel):
    type: TriggerType
    config: Optional[str] = None


class TriggerResponse(BaseModel):
    id: int
    type: TriggerType
    config: Optional[str]
    workflow_id: int

    class Config:
        from_attributes = True
