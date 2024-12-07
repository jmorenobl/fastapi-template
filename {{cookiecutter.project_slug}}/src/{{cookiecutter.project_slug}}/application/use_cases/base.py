"""
Base class for all use cases following the command pattern.
"""
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Input = TypeVar('Input')
Output = TypeVar('Output')


class BaseUseCase(ABC, Generic[Input, Output]):
    """
    Base class for all use cases following the command pattern.
    """
    
    @abstractmethod
    async def execute(self, input_data: Input) -> Output:
        """Execute the use case with the given input data."""
