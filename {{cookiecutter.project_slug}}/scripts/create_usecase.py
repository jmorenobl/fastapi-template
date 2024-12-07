#!/usr/bin/env python3
"""Script to create a new use case."""

import argparse
from pathlib import Path

USECASE_TEMPLATE = '''"""
{usecase_name} use case.
"""
from dataclasses import dataclass
from typing import Protocol

from {project_name}.application.interfaces.services.base import BaseService


@dataclass
class {usecase_class}Request:
    """Request model for {usecase_name}."""
    pass


@dataclass
class {usecase_class}Response:
    """Response model for {usecase_name}."""
    pass


class {usecase_class}Protocol(Protocol):
    """Protocol for {usecase_name} use case."""
    
    async def execute(
        self, request: {usecase_class}Request
    ) -> {usecase_class}Response:
        """Execute the use case."""
        ...


class {usecase_class}:
    """Implementation of {usecase_name} use case."""

    def __init__(self, service: BaseService) -> None:
        """Initialize the use case."""
        self.service = service

    async def execute(
        self, request: {usecase_class}Request
    ) -> {usecase_class}Response:
        """Execute the use case."""
        # Implement use case logic here
        return {usecase_class}Response()
'''


TEST_TEMPLATE = '''"""
Tests for {usecase_name} use case.
"""
import pytest
from {project_name}.application.use_cases.{domain}.{usecase_file} import (
    {usecase_class},
    {usecase_class}Request,
)


@pytest.mark.asyncio
async def test_{usecase_name}() -> None:
    """Test {usecase_name} use case."""
    # Arrange
    request = {usecase_class}Request()
    
    # Act
    # response = await usecase.execute(request)
    
    # Assert
    # Add your assertions here
    assert True  # Replace with actual assertions
'''


def create_usecase(name: str, domain: str) -> None:
    """Create a new use case."""
    # Convert names to proper format
    usecase_name = name.lower().replace("-", "_")
    usecase_class = "".join(word.capitalize() for word in usecase_name.split("_"))
    usecase_file = usecase_name
    project_name = Path.cwd().name

    # Create paths
    usecase_dir = Path(f"src/{project_name}/application/use_cases/{domain}")
    test_dir = Path(f"tests/unit/application/use_cases/{domain}")

    # Create directories
    usecase_dir.mkdir(parents=True, exist_ok=True)
    test_dir.mkdir(parents=True, exist_ok=True)

    # Create __init__.py files
    for dir_path in [usecase_dir, test_dir]:
        init_file = dir_path / "__init__.py"
        init_file.touch(exist_ok=True)

    # Create use case file
    usecase_path = usecase_dir / f"{usecase_file}.py"
    usecase_content = USECASE_TEMPLATE.format(
        usecase_name=usecase_name,
        usecase_class=usecase_class,
        project_name=project_name,
    )
    usecase_path.write_text(usecase_content)

    # Create test file
    test_path = test_dir / f"{usecase_file}_test.py"
    test_content = TEST_TEMPLATE.format(
        usecase_name=usecase_name,
        usecase_class=usecase_class,
        usecase_file=usecase_file,
        domain=domain,
        project_name=project_name,
    )
    test_path.write_text(test_content)

    print(f"Created use case {usecase_name} in domain {domain}")
    print(f"- Use case: {usecase_path}")
    print(f"- Test: {test_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new use case")
    parser.add_argument("--name", required=True, help="Name of the use case")
    parser.add_argument("--domain", required=True, help="Domain of the use case")
    args = parser.parse_args()

    create_usecase(args.name, args.domain)
