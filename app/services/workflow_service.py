from sqlalchemy.orm import Session
from app.models.workflow import Workflow


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
