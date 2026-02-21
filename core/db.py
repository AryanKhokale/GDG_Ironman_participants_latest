
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
    'postgresql+asyncpg://neondb_owner:npg_Xsh7nzOP2fTq@ep-long-night-aiytomqd-pooler.c-4.us-east-1.aws.neon.tech/registration?ssl=require',
    echo=True,
    pool_pre_ping=True,
)

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
