
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import get_db
from service.round_1_service.submission_service import submission_service
from schemas.round_1_schema.submission_schema import Submission
from service.round_1_service.problems_service import get_problem_by_id

router_1 = APIRouter()

@router_1.post("/submit")
async def api_new_submission(
    submission: Submission,
    db: AsyncSession = Depends(get_db)
):
    return await submission_service(
        db,
        submission.Team_Name,
        submission.contest_id,
        submission.problem_id,
        submission.code,
        submission.status,
        submission.score
    )

@router_1.get("/problem/{problem_id}")
async def get_problem(problem_id: int, db: AsyncSession = Depends(get_db)):
    problem = await get_problem_by_id(db, problem_id)
    if problem:
        return {
            "problem_id": problem.problem_id,
            "contest_id": problem.contest_id,
            "title": problem.title,
            "description": problem.description,
            "test_cases": problem.test_cases,
            "score": problem.score,
            "pre_code": problem.pre_code,
            "post_code": problem.post_code
        }
    else:
        return {"message": "Problem not found"}