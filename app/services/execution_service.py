from sqlalchemy.orm import Session
from app.models.workflow import Workflow
from app.models.trigger import Trigger
from app.models.execution_log import ExecutionLog
from datetime import datetime


class ExecutionService:

    @staticmethod
    def execute_workflow(db: Session, workflow_id: int):
        workflow = db.query(Workflow).filter(
            Workflow.id == workflow_id).first()
        if not workflow:
            return None, "Workflow not found"

        if not workflow.is_active:
            return None, "Workflow is inactive"

        trigger = db.query(Trigger).filter(
            Trigger.workflow_id == workflow_id).first()
        if not trigger:
            return None, "No trigger attached"

        if trigger.type != "webhook":
            return None, "Unsupported trigger type"

        # Simulated action execution
        log = ExecutionLog(
            status="SUCCESS",
            message="Webhook trigger executed successfully",
            workflow_id=workflow_id,
            timestamp=datetime.utcnow()
        )

        db.add(log)
        db.commit()

        return log, None
