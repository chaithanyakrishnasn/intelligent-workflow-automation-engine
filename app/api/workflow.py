from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.workflow import WorkflowCreate, WorkflowResponse
from app.services.workflow_service import WorkflowService
from app.schemas.workflow import WorkflowUpdate

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

@router.put("/{workflow_id}", response_model=WorkflowResponse)
def update_workflow(workflow_id: int, workflow: WorkflowUpdate, db: Session = Depends(get_db)):
    updated = WorkflowService.update_workflow(
        db=db,
        workflow_id=workflow_id,
        name=workflow.name,
        description=workflow.description,
        is_active=workflow.is_active
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return updated


@router.delete("/{workflow_id}")
def delete_workflow(workflow_id: int, db: Session = Depends(get_db)):
    deleted = WorkflowService.delete_workflow(db, workflow_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return {"message": "Workflow deleted successfully"}