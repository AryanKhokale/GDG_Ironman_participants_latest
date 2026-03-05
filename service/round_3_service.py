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
    cloudinary.config(
    cloud_name='dkq2hk958',
    api_key='347234613443183',
    api_secret='aEFOdN7sAlAJPprpWDMkDv1r2ys'
)


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

        
        return {"message": "Team has already submitted for Round 3. Please contact the admin if you want to update your submission."}


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

        return {
        "message": "Submitted successfully",
        "urls": uploaded_urls
    }