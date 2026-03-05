
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import get_db
from service.leaderboard_service import get_records_desc
from service.registration_service import registration_service
from schemas.registration_schema import RegistrationCreate
from service.login_service import login_service



router_x = APIRouter()

@router_x.post("/register")
async def register_team(registration: RegistrationCreate, db: AsyncSession = Depends(get_db)):
    res = await registration_service(registration.Team_Name, team_members=[mem.dict() for mem in registration.team_members], db=db)
    return res

@router_x.get("/leaderboard")
async def get_leaderboard(db: AsyncSession = Depends(get_db)):
    records = await get_records_desc(db)
    return records

@router_x.get("/login")
async def login(Team_Name: str, Leader_Email: str, db: AsyncSession = Depends(get_db)):
    return await login_service(db=db, Team_Name=Team_Name, Leader_Email=Leader_Email)