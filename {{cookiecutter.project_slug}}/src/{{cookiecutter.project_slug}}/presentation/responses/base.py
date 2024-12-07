"""
Base response wrapper for all API responses.
"""
from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class BaseResponse(BaseModel, Generic[T]):
    """Base response wrapper for all API responses"""
    data: T | None = None
    message: str | None = None
    error: str | None = None
