from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.action import Action
from app.models.workflow import Workflow
from app.schemas.action import ActionCreate, ActionResponse

router = APIRouter(prefix="/actions", tags=["Actions"])


@router.post("/{workflow_id}", response_model=ActionResponse)
def create_action(workflow_id: int, action: ActionCreate, db: Session = Depends(get_db)):
    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")

    existing_action = db.query(Action).filter(
        Action.workflow_id == workflow_id
    ).first()

    if existing_action:
        raise HTTPException(status_code=400, detail="Action already exists for this workflow")

    new_action = Action(
        type=action.type,
        config=action.config,
        workflow_id=workflow_id
    )

    db.add(new_action)
    db.commit()
    db.refresh(new_action)
    return new_action