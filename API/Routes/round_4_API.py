
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import get_db
from schemas.round_4_schema import Round_4_Submit
from service.round_4_service import submit_round_4_service

router_4 = APIRouter()

@router_4.post("/round_4")
async def submit_round_4_endpoint(
    round_4: Round_4_Submit,
    db: AsyncSession = Depends(get_db)
):

    event = await submit_round_4_service(
        db=db,
        Team_Name=round_4.Team_Name,
        structured_submission=round_4.structured_submission,
        status_4=round_4.status_4,
        question=round_4.question,
        score_4=round_4.score_4
    )

    return {
        "message": "Submitted successfully",
        "event": event
    }
