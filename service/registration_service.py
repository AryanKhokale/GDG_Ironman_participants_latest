from models.model import Registration
from sqlalchemy.ext.asyncio import AsyncSession


async def registration_service(team_name: str, team_members: dict, db: AsyncSession ):
     team = Registration(
        Team_Name=team_name,
        team_members=team_members
    )

     db.add(team)
 
     await db.commit()
 
     return {"message": "Team registered"}
     
