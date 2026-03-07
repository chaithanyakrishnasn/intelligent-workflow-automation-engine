from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.execution_service import ExecutionService

router = APIRouter(prefix="/trigger", tags=["Webhook Trigger"])


@router.post("/webhook/{workflow_id}")
async def webhook_trigger(
    workflow_id: int,
    request: Request,
    db: Session = Depends(get_db)
):

    payload = await request.json()

    result, error = ExecutionService.execute_workflow(db, workflow_id)

    if error:
        raise HTTPException(status_code=400, detail=error)

    return {
        "message": "Webhook triggered workflow execution",
        "workflow_id": workflow_id,
        "payload_received": payload
    }