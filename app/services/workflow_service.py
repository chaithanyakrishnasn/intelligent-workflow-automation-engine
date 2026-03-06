from sqlalchemy.orm import Session
from app.models.workflow import Workflow
from app.core.scheduler import scheduler
from app.services.execution_service import ExecutionService
from app.core.scheduler import remove_job
from app.models.trigger import Trigger
from app.core.scheduler import scheduler
from app.services.execution_service import ExecutionService


class WorkflowService:

    @staticmethod
    def create_workflow(db: Session, name: str, description: str, is_active: bool):
        workflow = Workflow(
            name=name,
            description=description,
            is_active=is_active
        )
        db.add(workflow)
        db.commit()
        db.refresh(workflow)
        return workflow

    @staticmethod
    def get_all_workflows(db: Session):
        return db.query(Workflow).all()

    @staticmethod
    def get_workflow_by_id(db: Session, workflow_id: int):
        return db.query(Workflow).filter(Workflow.id == workflow_id).first()

    @staticmethod
    def update_workflow(db: Session, workflow_id: int, name: str, description: str, is_active: bool):
        workflow = db.query(Workflow).filter(
            Workflow.id == workflow_id).first()
        if not workflow:
            return None

        workflow.name = name
        workflow.description = description
        workflow.is_active = is_active

        db.commit()
        db.refresh(workflow)
        return workflow

    @staticmethod
    def delete_workflow(db: Session, workflow_id: int):
        workflow = db.query(Workflow).filter(
            Workflow.id == workflow_id).first()
        if not workflow:
            return None

        db.delete(workflow)
        db.commit()
        return workflow


def register_timer_trigger(db, workflow_id: int, interval_seconds: int):

    scheduler.add_job(
        ExecutionService.execute_workflow,
        "interval",
        seconds=interval_seconds,
        args=[db, workflow_id],
        id=f"workflow_{workflow_id}",
        replace_existing=True
    )


def deactivate_workflow(db, workflow_id: int):
    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()

    if not workflow:
        return None

    workflow.is_active = False
    db.commit()

    remove_job(f"workflow_{workflow_id}")

    return workflow


def activate_workflow(db, workflow_id: int):

    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()

    if not workflow:
        return None

    workflow.is_active = True
    db.commit()

    trigger = db.query(Trigger).filter(
        Trigger.workflow_id == workflow_id
    ).first()

    if trigger and trigger.type == "timer":

        interval = int(trigger.config)

        scheduler.add_job(
            ExecutionService.execute_workflow,
            "interval",
            seconds=interval,
            args=[db, workflow_id],
            id=f"workflow_{workflow_id}",
            replace_existing=True
        )

    return workflow
