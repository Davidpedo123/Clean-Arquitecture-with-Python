from sqlmodel import Field, SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(
    DATABASE_URL,
    echo=True,  
    pool_size=20,  
    max_overflow=10, 
    pool_timeout=30,  
    pool_recycle=3600  
)


async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,  
)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
        
async def init_db():
    async with engine.begin() as conn:
        
        await conn.run_sync(SQLModel.metadata.create_all)