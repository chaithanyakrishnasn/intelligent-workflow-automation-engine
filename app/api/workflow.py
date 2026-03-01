from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.workflow import WorkflowCreate, WorkflowResponse
from app.services.workflow_service import WorkflowService

router = APIRouter(prefix="/workflows", tags=["Workflows"])


@router.post("/", response_model=WorkflowResponse)
def create_workflow(workflow: WorkflowCreate, db: Session = Depends(get_db)):
    return WorkflowService.create_workflow(
        db=db,
        name=workflow.name,
        description=workflow.description,
        is_active=workflow.is_active
    )


@router.get("/", response_model=list[WorkflowResponse])
def get_all_workflows(db: Session = Depends(get_db)):
    return WorkflowService.get_all_workflows(db)


@router.get("/{workflow_id}", response_model=WorkflowResponse)
def get_workflow_by_id(workflow_id: int, db: Session = Depends(get_db)):
    workflow = WorkflowService.get_workflow_by_id(db, workflow_id)
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return workflow