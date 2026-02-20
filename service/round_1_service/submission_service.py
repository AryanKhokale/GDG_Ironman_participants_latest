from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.round_1.submissions import Submission
from core.final_score import add_score, add_status


async def submission_service(
    db: AsyncSession,
    Team_Name: str,
    contest_id: str,
    problem_id: int,
    code: str,
    status: str,
    score: int 
):
    
    result = await db.execute(
        select(Submission).where(Submission.Team_Name == Team_Name )
    )
    
    existing_team = result.scalar_one_or_none()


    # 3. If exists → UPDATE
    if existing_team:

        existing_team.code = code
        existing_team.status = status
        await add_score(db, Team_Name, score)
        await add_status(db, Team_Name, status)
        await db.commit()
        await db.refresh(existing_team)
        return {"message": "Submission updated", "submission_id": existing_team.submission_id}
    
     

    # Optional: check if contest exists
    # (recommended if foreign key exists)

    # Create problem object
    else:
            
        new_submission = Submission(
            Team_Name=Team_Name,
            contest_id=contest_id,
            problem_id=problem_id,
            code=code,
            status=status
        )
    
        # Save to DB
        db.add(new_submission)
    
        await db.commit()
        await db.refresh(new_submission)
        await add_score(db, Team_Name, score)
        await add_status(db, Team_Name, status)
    
        return {"message": "Submission created", "submission_id": new_submission.submission_id}



