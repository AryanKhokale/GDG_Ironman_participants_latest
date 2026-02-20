import cloudinary.uploader
import cloudinary.api
import cloudinary
from dotenv import load_dotenv
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from fastapi import UploadFile

load_dotenv()
from models.round_3 import Round_3




async def submit_round_3_service(
    db: AsyncSession,
    Team_Name: str,
    figma_links: str,
    description: str,
    status_3: str,
    score_3: int,
    files: List[UploadFile]
):

    # 1. Upload new files
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
        select(Round_3).where(Round_3.Team_Name == Team_Name)
    )

    existing_team = result.scalar_one_or_none()


    # 3. If exists → UPDATE
    if existing_team:

        # Merge old + new file URLs
      
        all_urls =  uploaded_urls

        existing_team.figma_links = figma_links
        existing_team.description = description
        existing_team.status_3 = status_3

        # ADD score instead of replacing
        existing_team.score_3 += score_3

        # Update files
        existing_team.ss_links_round_3 = ",".join(all_urls)

        await db.commit()
        await db.refresh(existing_team)

        return existing_team, uploaded_urls


    # 4. If not exists → CREATE new record
    else:

        ss_links = ",".join(uploaded_urls)

        event = Round_3(
            Team_Name=Team_Name,
            figma_links=figma_links,
            ss_links_round_3=ss_links,
            description=description,
            status_3=status_3,
            score_3=score_3
        )

        db.add(event)
        await db.commit()
        await db.refresh(event)

        return event, uploaded_urls