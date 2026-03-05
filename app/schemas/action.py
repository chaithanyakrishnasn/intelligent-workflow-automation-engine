from pydantic import BaseModel
from typing import Optional
from app.core.enums import ActionType


class ActionCreate(BaseModel):
    type: ActionType
    config: Optional[str] = None


class ActionResponse(BaseModel):
    id: int
    type: ActionType
    config: Optional[str]
    workflow_id: int

    class Config:
        from_attributes = True