from typing import Annotated, List
from fastapi import APIRouter, Depends, Form, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import get_db
from service.round_3_service import submit_round_3_service


router_3 = APIRouter()


@router_3.post("/round_3")
async def submit_round_3_endpoint(
    Team_Name: str = Form(...),
    figma_links: str = Form(...),
    description: str = Form(...),
    files: list[UploadFile] = File(...),
    db: AsyncSession = Depends(get_db)
):

    event = await submit_round_3_service(
        db=db,
        Team_Name=Team_Name,
        figma_links=figma_links,
        description=description,
        status_3='Submitted',
        score_3=0,
        files=files
    )

   
    return event

@router_3.post("/debug_upload")
async def debug_upload(
    files: Annotated[list[UploadFile], File(..., media_type="multipart/form-data")]
):
    return {"count": len(files)}