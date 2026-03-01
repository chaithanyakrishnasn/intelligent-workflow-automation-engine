from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.workflow import Workflow
from app.schemas.workflow import WorkflowCreate, WorkflowResponse
from fastapi import HTTPException

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

@router.get("/", response_model=list[WorkflowResponse])
def get_all_workflows(db: Session = Depends(get_db)):
    workflows = db.query(Workflow).all()
    return workflows


@router.get("/{workflow_id}", response_model=WorkflowResponse)
def get_workflow_by_id(workflow_id: int, db: Session = Depends(get_db)):
    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return workflow