from pydantic import BaseModel
from typing import Optional


class ActionCreate(BaseModel):
    type: str
    config: Optional[str] = None


class ActionResponse(BaseModel):
    id: int
    type: str
    config: Optional[str]
    workflow_id: int

    class Config:
        from_attributes = True
