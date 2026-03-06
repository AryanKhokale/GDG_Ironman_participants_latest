from typing import List

from sqlalchemy import select

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
load_dotenv()
from models.permission import Permission


async def permission_service(
    db: AsyncSession,
    Role: str,
):


    result = await db.execute(select(Permission.permission).where(Permission.User == Role))
    return result.scalar_one_or_none()
   

   

    

