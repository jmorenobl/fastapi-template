"""
Base schema for all DTOs.
"""
from datetime import datetime
from typing import TypeVar

from pydantic import BaseModel, ConfigDict

T = TypeVar('T')


class BaseSchema(BaseModel):
    """Base schema for all DTOs"""
    model_config = ConfigDict(from_attributes=True)


class BaseResponseSchema(BaseSchema):
    """Base schema for all response DTOs"""
    id: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
