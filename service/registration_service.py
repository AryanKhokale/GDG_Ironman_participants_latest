from models.registration import Registration
from sqlalchemy.ext.asyncio import AsyncSession
from core.register_leaderboard import add_team_to_leaderboard


async def registration_service(team_name: str, team_members: dict, db: AsyncSession ):
     team = Registration(
        Team_Name=team_name,
        team_members=team_members
    )

     db.add(team)
 
     await db.commit()

     await add_team_to_leaderboard(db, Team_Name=team_name)
 
     return {"message": "Team registered"}
     
