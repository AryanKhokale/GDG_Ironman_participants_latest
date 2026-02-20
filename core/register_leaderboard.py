from sqlalchemy.ext.asyncio import AsyncSession
from models.leaderboard import Leaderboard

async def add_team_to_leaderboard(db: AsyncSession, Team_Name: str):

    event = Leaderboard(
        Team_Name=Team_Name,
        team_score=0,
        status_1='REJECTED',
        status_2='REJECTED',
        status_3='REJECTED',
        status_4='REJECTED'
    )

    db.add(event)
    await db.commit()
    await db.refresh(event)

    return event
       