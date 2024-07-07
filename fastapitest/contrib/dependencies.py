from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapitest.configs.database import get_session

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)]