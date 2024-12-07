#!/usr/bin/env python3
"""Script to create a new domain."""

import argparse
from pathlib import Path

ENTITY_TEMPLATE = '''"""
{domain_name} entity.
"""
from dataclasses import dataclass

from {project_name}.domain.entities.base import BaseEntity


@dataclass
class {entity_class}(BaseEntity):
    """
    {domain_name} entity.
    """
    pass
'''


REPOSITORY_TEMPLATE = '''"""
{domain_name} repository interface.
"""
from typing import Protocol

from {project_name}.domain.entities.{domain_name} import {entity_class}
from {project_name}.application.interfaces.repositories.base import BaseRepository


class {entity_class}RepositoryProtocol(BaseRepository[{entity_class}], Protocol):
    """Repository interface for {domain_name}."""
    pass
'''


SERVICE_TEMPLATE = '''"""
{domain_name} service interface.
"""
from typing import Protocol

from {project_name}.application.interfaces.services.base import BaseService
from {project_name}.domain.entities.{domain_name} import {entity_class}


class {entity_class}ServiceProtocol(BaseService[{entity_class}], Protocol):
    """Service interface for {domain_name}."""
    pass
'''


DB_REPOSITORY_TEMPLATE = '''"""
Database implementation of {domain_name} repository.
"""
from {project_name}.domain.entities.{domain_name} import {entity_class}
from {project_name}.application.interfaces.repositories.{domain_name} import {entity_class}RepositoryProtocol
from {project_name}.infrastructure.databases.repositories.base import BaseRepositoryImpl


class {entity_class}Repository(BaseRepositoryImpl[{entity_class}], {entity_class}RepositoryProtocol):
    """Database implementation of {domain_name} repository."""
    pass
'''


def create_domain(name: str) -> None:
    """Create a new domain with all necessary files."""
    # Convert names to proper format
    domain_name = name.lower().replace("-", "_")
    entity_class = "".join(word.capitalize() for word in domain_name.split("_"))
    project_name = Path.cwd().name

    # Define all required directories
    directories = {
        "entity": Path(f"src/{project_name}/domain/entities"),
        "repository_interface": Path(
            f"src/{project_name}/application/interfaces/repositories"
        ),
        "service_interface": Path(
            f"src/{project_name}/application/interfaces/services"
        ),
        "db_repository": Path(
            f"src/{project_name}/infrastructure/databases/repositories"
        ),
        "tests_unit": Path(f"tests/unit/domain/entities"),
        "tests_integration": Path(f"tests/integration/infrastructure/repositories"),
    }

    # Create directories and __init__.py files
    for dir_path in directories.values():
        dir_path.mkdir(parents=True, exist_ok=True)
        init_file = dir_path / "__init__.py"
        init_file.touch(exist_ok=True)

    # Create entity
    entity_path = directories["entity"] / f"{domain_name}.py"
    entity_content = ENTITY_TEMPLATE.format(
        domain_name=domain_name,
        entity_class=entity_class,
        project_name=project_name,
    )
    entity_path.write_text(entity_content)

    # Create repository interface
    repo_interface_path = directories["repository_interface"] / f"{domain_name}.py"
    repo_interface_content = REPOSITORY_TEMPLATE.format(
        domain_name=domain_name,
        entity_class=entity_class,
        project_name=project_name,
    )
    repo_interface_path.write_text(repo_interface_content)

    # Create service interface
    service_interface_path = directories["service_interface"] / f"{domain_name}.py"
    service_interface_content = SERVICE_TEMPLATE.format(
        domain_name=domain_name,
        entity_class=entity_class,
        project_name=project_name,
    )
    service_interface_path.write_text(service_interface_content)

    # Create repository implementation
    db_repo_path = directories["db_repository"] / f"{domain_name}.py"
    db_repo_content = DB_REPOSITORY_TEMPLATE.format(
        domain_name=domain_name,
        entity_class=entity_class,
        project_name=project_name,
    )
    db_repo_path.write_text(db_repo_content)

    print(f"Created domain {domain_name} with:")
    print(f"- Entity: {entity_path}")
    print(f"- Repository Interface: {repo_interface_path}")
    print(f"- Service Interface: {service_interface_path}")
    print(f"- Repository Implementation: {db_repo_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new domain")
    parser.add_argument("--name", required=True, help="Name of the domain")
    args = parser.parse_args()

    create_domain(args.name)
