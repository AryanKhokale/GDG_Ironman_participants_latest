from typing import List
from fastapi import APIRouter, Depends, Form, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import get_db
from service.round_5_service import submit_round_5_service


router_5 = APIRouter()

@router_5.post("/round_5")
async def submit_round_5_endpoint(
    Team_Name: str = Form(...),
    abstract: str = Form(...),
    score_5: int = Form(...),
    files: List[UploadFile] = File(...),
    db: AsyncSession = Depends(get_db)
):

    event, uploaded_urls = await submit_round_5_service(
        db=db,
        Team_Name=Team_Name,
        abstract=abstract,
        score_5=score_5,
        files=files
    )

    return {
        "message": "Submitted successfully",
        "urls": uploaded_urls
    }