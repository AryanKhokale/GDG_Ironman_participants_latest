from pydantic import BaseModel
from datetime import datetime

class round_2_submit(BaseModel):
    Team_Name: str
    description: str
    start_time: datetime   
    end_time: datetime
