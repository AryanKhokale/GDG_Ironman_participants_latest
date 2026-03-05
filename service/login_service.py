from sqlalchemy import select
from models.registration import Registration
from sqlalchemy.ext.asyncio import AsyncSession


async def login_service(db: AsyncSession, Team_Name: str, Leader_Email: str):

    result = await db.execute(
        select(Registration).where(Registration.Team_Name == Team_Name)
    )

    team = result.scalar_one_or_none()

    if not team:
        return {"message": "Team not registered", "flag": "Failed"}

    leader = next((m for m in team.team_members if m["role"] == "LEADER"), None)

    if not leader or leader["email"] != Leader_Email:
        return {"message": "Invalid leader email", "flag": "Failed"}

    return {"Team_Name": team.Team_Name,  "flag": "Success"}
