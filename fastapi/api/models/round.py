from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Float, Text
from sqlalchemy.orm import relationship

from db import Base

class Round(Base):
    __tablename__ = "rounds"

    id = Column(Integer, primary_key=True)
    motion = Column(String(1024))
    source = Column(JSON)
    POIs = Column(JSON)

    rebuttals = relationship("Rebuttal", back_populates="round", cascade="delete")
    speeches = relationship("Speech", back_populates="round", cascade="delete")

class Rebuttal(Base):
    __tablename__ = "rebuttals"

    id = Column(Integer, primary_key=True)

    src = Column(Integer)
    tgt = Column(Integer)

    round_id = Column(Integer, ForeignKey("rounds.id"))
    round = relationship("Round", back_populates="rebuttals")

class Speech(Base):
    __tablename__ = "speeches"

    id = Column(Integer, primary_key=True)

    start_time = Column(Float)

    round_id = Column(Integer, ForeignKey("rounds.id"))
    round = relationship("Round", back_populates="speeches")

    ADUs = relationship("ADU", back_populates="speech", cascade="delete")

class ADU(Base):
    __tablename__ = "ADUs"

    id = Column(Integer, primary_key=True)

    sequence_id = Column(Integer)
    transcript = Column(Text)

    speech_id = Column(Integer, ForeignKey("speeches.id"))
    speech = relationship("Speech", back_populates="ADUs")