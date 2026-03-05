from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    config = Column(String, nullable=True)

    workflow_id = Column(Integer, ForeignKey("workflows.id"), unique=True)
    workflow = relationship("Workflow", back_populates="action")
