"""
Base entity class for all domain entities.
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseEntity:
    """
    Base entity class for all domain entities.
    """

    id: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
