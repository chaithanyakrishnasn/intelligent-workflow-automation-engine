from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class ExecutionLog(Base):
    __tablename__ = "execution_logs"

    id = Column(Integer, primary_key=True, index=True)

    status = Column(String, nullable=False)
    message = Column(String, nullable=True)

    retry_count = Column(Integer, default=0)

    timestamp = Column(DateTime, default=datetime.utcnow)

    workflow_id = Column(Integer, ForeignKey("workflows.id"))
    workflow = relationship("Workflow", back_populates="executions")
