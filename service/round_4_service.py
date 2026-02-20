from dotenv import load_dotenv
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from fastapi import UploadFile

load_dotenv()
from models.round_4 import  Round_4


async def submit_round_4_service(
    db: AsyncSession,
    Team_Name: str,
    structured_submission: str,
    status_4: str,
    question: str,
    score_4: int,
):
    
    result = await db.execute(
        select(Round_4).where(Round_4.Team_Name == Team_Name)
    )

    existing_team = result.scalar_one_or_none()


    # 3. If exists → UPDATE
    if existing_team:

        existing_team.structured_submission = structured_submission

        await db.commit()
        await db.refresh(existing_team)
        return existing_team
    else:
        
        event = Round_4(
            Team_Name=Team_Name,
            structured_submission=structured_submission,
            status_4=status_4,
            question=question,
            score_4=score_4,
        )
    
        db.add(event)
        await db.commit()
        await db.refresh(event)
    
        return event
