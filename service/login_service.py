from sqlalchemy import select
from models.leaderboard import Leaderboard
from sqlalchemy.ext.asyncio import AsyncSession


async def login_service(db: AsyncSession, Team_Name: str):
    result = await db.execute(
        select(Leaderboard).where(Leaderboard.Team_Name == Team_Name)
    )
    problem = result.scalar_one_or_none()
    if not problem:
        return {"message": "Team not registered"}
    return problem
