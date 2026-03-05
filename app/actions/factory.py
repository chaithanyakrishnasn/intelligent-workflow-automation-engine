from app.actions.log_action import LogAction


class ActionFactory:

    @staticmethod
    def get_action(action_type: str, db):
        if action_type.lower() == "log":
            return LogAction(db)

        raise ValueError(f"Unsupported action type: {action_type}")
