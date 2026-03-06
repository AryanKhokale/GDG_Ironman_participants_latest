from sqlalchemy import Column, Integer, Text
from sqlalchemy.dialects.postgresql import JSONB
from core.dependency import Base

class Permission(Base):
    __tablename__ = "Permission"

    User = Column(Text, primary_key=True, index=True)
    permission = Column(Text,nullable=True)
   