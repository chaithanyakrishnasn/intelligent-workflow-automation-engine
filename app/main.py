from fastapi import FastAPI
from sqlalchemy import text
from app.core.database import engine, Base
from app.api.workflow import router as workflow_router
import app.models  # IMPORTANT: ensures models are registered
from app.api.trigger import router as trigger_router
from app.api.execution import router as execution_router
from app.api.action import router as action_router
from app.core.scheduler import start_scheduler
from app.api.webhook import router as webhook_router

app = FastAPI(
    title="Intelligent Workflow Automation Engine",
    version="0.1.0"
)

app.include_router(action_router)

app.include_router(trigger_router)

app.include_router(workflow_router)

app.include_router(execution_router)

app.include_router(webhook_router)

# Create tables at startup


@app.on_event("startup")
def startup_event():
    start_scheduler()
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Automation Engine Running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/db-check")
def db_check():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return {"database": "connected", "result": result.scalar()}
    except Exception as e:
        return {"database": "error", "details": str(e)}
