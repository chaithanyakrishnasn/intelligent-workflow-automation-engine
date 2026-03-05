from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base


class Trigger(Base):
    __tablename__ = "triggers"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    from sqlalchemy import Text
    config = Column(Text, nullable=True)

    workflow_id = Column(Integer, ForeignKey("workflows.id"), unique=True)
    workflow = relationship("Workflow", back_populates="trigger")
