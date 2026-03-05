from app.actions.log_action import LogAction
from app.core.enums import ActionType


class ActionFactory:

    @staticmethod
    def get_action(action_type: str, db):
        if action_type == ActionType.LOG:
            return LogAction(db)

        raise ValueError(f"Unsupported action type: {action_type}")
