from pydantic import BaseModel

class Login(BaseModel):
    Team_Name: str
