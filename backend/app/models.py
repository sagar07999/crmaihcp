from sqlalchemy import Column, Integer, String, Text, Date, TIMESTAMP, text
from .database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String(100))
    hospital = Column(String(100))
    speciality = Column(String(100))
    interaction_type = Column(String(50))
    discussion = Column(Text)
    products = Column(Text)
    next_followup = Column(Date)
    summary = Column(Text)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))