from sqlalchemy.orm import Session
from app.models.workflow import Workflow
from app.models.trigger import Trigger
from app.models.action import Action
from app.actions.factory import ActionFactory
from app.models.execution_log import ExecutionLog
from datetime import datetime, timedelta
from app.core.scheduler import scheduler

MAX_RETRIES = 3


class ExecutionService:

    @staticmethod
    def execute_workflow(db, workflow_id: int):

        workflow = db.query(Workflow).filter(
            Workflow.id == workflow_id).first()

        if not workflow:
            return None, "Workflow not found"

        if not workflow.is_active:
            return None, "Workflow inactive"

        action = db.query(Action).filter(
            Action.workflow_id == workflow_id
        ).first()

        if not action:
            return None, "No action attached"

        try:

            action_handler = ActionFactory.get_action(action.type, db)

            result = action_handler.execute(workflow_id)

            log = ExecutionLog(
                status="SUCCESS",
                message="Action executed successfully",
                retry_count=0,
                workflow_id=workflow_id
            )

            db.add(log)
            db.commit()

            return result, None

        except Exception as e:

            retry_attempt = 1

            log = ExecutionLog(
                status="FAILED",
                message=str(e),
                retry_count=retry_attempt,
                workflow_id=workflow_id
            )

            db.add(log)
            db.commit()

            if retry_attempt <= MAX_RETRIES:

                scheduler.add_job(
                    ExecutionService.execute_workflow,
                    "date",
                    run_date=datetime.utcnow() + timedelta(seconds=5),
                    args=[db, workflow_id],
                    id=f"retry_{workflow_id}_{retry_attempt}",
                    replace_existing=True
                )

            return None, str(e)
