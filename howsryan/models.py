from sqlalchemy import Column, Integer, String, DateTime
from howsryan.database import Base
from datetime import datetime


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    author = Column(String(40), nullable=False)
    date_started = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    mood = Column(String(60), nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        repr_text = self.mood
        if len(repr_text) > 20:
            repr_text = self.mood[0:21] + "..."
        return f"Status('{self.mood[0:15]}', '{self.date}')"


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    project = Column(String(60), nullable=False)

    def __repr__(self):
        return f"Project('{self.project}')"
