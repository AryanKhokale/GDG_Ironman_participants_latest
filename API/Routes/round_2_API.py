from typing import List
from fastapi import APIRouter, Depends, Form, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import get_db
from service.round_2_service import submit_round_2_service

router_2 = APIRouter()

@router_2.post("/round_2")
async def submit_round_2_endpoint(
    Team_Name: str = Form(...),
    git_hub_link: str = Form(...),
    hosted_link: str = Form(...),
    files: List[UploadFile] = File(...),
    db: AsyncSession = Depends(get_db)
):

    event, uploaded_urls = await submit_round_2_service(
        db=db,
        Team_Name=Team_Name,
        git_hub_link=git_hub_link,
        hosted_link=hosted_link,
        status="Submitted",
            score_2=0,
        files=files
    )

    return {
        "message": "Submitted successfully",
        "urls": uploaded_urls
    }