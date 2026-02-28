from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

    trigger = relationship("Trigger", back_populates="workflow", uselist=False)
    action = relationship("Action", back_populates="workflow", uselist=False)
    executions = relationship("ExecutionLog", back_populates="workflow")
