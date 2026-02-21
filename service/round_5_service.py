import cloudinary.uploader
import cloudinary.api
import cloudinary
from dotenv import load_dotenv
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from fastapi import UploadFile

load_dotenv()
from models.round_5 import Round_5


cloudinary.config(
    cloud_name='dokzyijqo',
    api_key='519149328713126',
    api_secret='LLeSvMpg1xwzdvtPNp4w6dmTnvs'
)

async def submit_round_5_service(
    db: AsyncSession,
    Team_Name: str,
    abstract: str,
    score_5: int,
    files: List[UploadFile]
):
    uploaded_urls = []

    for file in files:
        result = cloudinary.uploader.upload(
            file.file,
            resource_type="auto",
            folder="round_3"
        )
        uploaded_urls.append(result["secure_url"])


    # 2. Check if Team already exists
    result = await db.execute(
        select(Round_5).where(Round_5.Team_Name == Team_Name)
    )

    existing_team = result.scalar_one_or_none()


    # 3. If exists → UPDATE
    if existing_team:


        existing_team.ppt_link = uploaded_urls[0]  # Assuming only one file for PPT
        existing_team.abstract = abstract


        await db.commit()
        await db.refresh(existing_team)

        return existing_team, uploaded_urls

    
    else :

        event = Round_5(
            Team_Name=Team_Name,
            abstract=abstract,
            score_5=0,
            ppt_link=uploaded_urls[0]  # Assuming only one file for PPT
        )
    
        db.add(event)
        await db.commit()
        await db.refresh(event)
    
        return event, uploaded_urls
    