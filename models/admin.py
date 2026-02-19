from sqlalchemy.orm import  mapped_column
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import JSONB
from .dependency import Base
from sqlalchemy import Column, Integer, Text

class Admin(Base):
    __tablename__ = "admin"

    Team_Name = mapped_column(Text)
    score = mapped_column(Integer)

#Team_Name
#INTEGER
#PRIMARY KEY
#GENERATED ALWAYS AS IDENTITY
#
#score
#INTEGER