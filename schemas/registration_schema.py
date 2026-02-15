from pydantic import BaseModel
from typing import List

class Team_Members(BaseModel):
    name: str
    role: str
    email: str

class RegistrationCreate(BaseModel):
    Team_Name: str
    team_members: List[Team_Members]
    
    