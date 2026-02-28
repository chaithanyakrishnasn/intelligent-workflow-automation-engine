from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.workflow import Workflow
from app.schemas.workflow import WorkflowCreate, WorkflowResponse

router = APIRouter(prefix="/workflows", tags=["Workflows"])


@router.post("/", response_model=WorkflowResponse)
def create_workflow(
    workflow: WorkflowCreate,
    db: Session = Depends(get_db)
):
    db_workflow = Workflow(
        name=workflow.name,
        description=workflow.description,
        is_active=workflow.is_active
    )
    db.add(db_workflow)
    db.commit()
    db.refresh(db_workflow)
    return db_workflow