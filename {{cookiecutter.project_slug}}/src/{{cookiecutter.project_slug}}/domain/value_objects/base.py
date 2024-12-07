"""
Base class for value objects. Value objects are immutable.
"""
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ValueObject:
    """
    Base class for value objects. Value objects are immutable.
    """

    def equals(self, other: Any) -> bool:
        """
        Check if two value objects are equal.
        """
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

