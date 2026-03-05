from app.actions.base import BaseAction


class LogAction(BaseAction):

    def __init__(self, db):
        self.db = db

    def execute(self, workflow_id: int):
        from app.models.execution_log import ExecutionLog
        from datetime import datetime

        log = ExecutionLog(
            status="SUCCESS",
            message="Log action executed successfully",
            workflow_id=workflow_id,
            timestamp=datetime.utcnow()
        )

        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)

        return log
