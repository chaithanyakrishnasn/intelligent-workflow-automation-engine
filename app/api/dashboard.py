from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, date

from app.core.database import get_db
from app.models.workflow import Workflow
from app.models.execution_log import ExecutionLog

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/stats")
def get_dashboard_stats(db: Session = Depends(get_db)):

    total_workflows = db.query(Workflow).count()

    active_workflows = db.query(Workflow).filter(
        Workflow.is_active == True
    ).count()

    today = date.today()

    executions_today = db.query(ExecutionLog).filter(
        func.date(ExecutionLog.timestamp) == today
    ).count()

    failed_executions = db.query(ExecutionLog).filter(
        ExecutionLog.status == "FAILED"
    ).count()

    return {
        "total_workflows": total_workflows,
        "active_workflows": active_workflows,
        "executions_today": executions_today,
        "failed_executions": failed_executions
    }