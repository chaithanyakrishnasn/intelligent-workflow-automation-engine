from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.trigger import Trigger
from app.models.workflow import Workflow
from app.schemas.trigger import TriggerCreate, TriggerResponse
from app.services.workflow_service import register_timer_trigger

router = APIRouter(prefix="/triggers", tags=["Triggers"])


@router.post("/{workflow_id}", response_model=TriggerResponse)
def create_trigger(workflow_id: int, trigger: TriggerCreate, db: Session = Depends(get_db)):

    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")

    existing_trigger = db.query(Trigger).filter(
        Trigger.workflow_id == workflow_id
    ).first()

    if existing_trigger:
        raise HTTPException(
            status_code=400, detail="Trigger already exists for this workflow")

    new_trigger = Trigger(
        type=trigger.type,
        config=trigger.config,
        workflow_id=workflow_id
    )

    db.add(new_trigger)
    db.commit()
    db.refresh(new_trigger)

    # register timer trigger if needed
    if trigger.type == "timer":
        interval = int(trigger.config)
        register_timer_trigger(db, workflow_id, interval)

    return new_trigger
