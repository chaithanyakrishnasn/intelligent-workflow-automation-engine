from pydantic import BaseModel
from typing import Optional


class WorkflowCreate(BaseModel):
    name: str
    description: Optional[str] = None
    is_active: bool = True


class WorkflowResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    is_active: bool

    class Config:
        from_attributes = True

class WorkflowUpdate(BaseModel):
    name: str
    description: Optional[str] = None
    is_active: bool