from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List
from {{cookiecutter.project_slug}}.domain.entities.base import BaseEntity

T = TypeVar('T', bound=BaseEntity)

class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[T]:
        """Retrieve an entity by its ID."""
        pass

    @abstractmethod
    async def list(self) -> List[T]:
        """List all entities."""
        pass

    @abstractmethod
    async def create(self, entity: T) -> T:
        """Create a new entity."""
        pass

    @abstractmethod
    async def update(self, entity: T) -> T:
        """Update an existing entity."""
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        """Delete an entity by its ID."""
        pass