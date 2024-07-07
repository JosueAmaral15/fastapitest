from pydantic_settings import BaseSettings
from pydantic import Field
import asyncpg

class Settings(BaseSettings):
    DB_URL : str = Field(default='postgresql+asyncpg://workout:workout@localhost:5432/workout')
    
settings = Settings()