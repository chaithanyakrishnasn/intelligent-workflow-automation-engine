from sqlalchemy.orm import Session
from app.models.workflow import Workflow
from app.models.trigger import Trigger
from app.models.action import Action
from app.actions.factory import ActionFactory


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
            Trigger.workflow_id == workflow_id
        ).first()

        if not trigger:
            return None, "No trigger attached"

        action = db.query(Action).filter(
            Action.workflow_id == workflow_id
        ).first()

        if not action:
            return None, "No action attached"

        try:
            action_handler = ActionFactory.get_action(action.type, db)
            result = action_handler.execute(workflow_id)
            return result, None

        except ValueError as e:
            return None, str(e)
