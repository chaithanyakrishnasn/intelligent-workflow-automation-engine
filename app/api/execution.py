from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.execution_service import ExecutionService

router = APIRouter(prefix="/execute", tags=["Execution"])


@router.post("/{workflow_id}")
def execute_workflow(workflow_id: int, db: Session = Depends(get_db)):
    result, error = ExecutionService.execute_workflow(db, workflow_id)

    if error:
        raise HTTPException(status_code=400, detail=error)

    return {
        "status": "executed",
        "log_id": result.id
    }