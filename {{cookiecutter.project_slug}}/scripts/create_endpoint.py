#!/usr/bin/env python3
"""Script to create a new endpoint."""

import argparse
from pathlib import Path

ENDPOINT_TEMPLATE = '''"""
{endpoint_name} endpoints.
"""
from fastapi import APIRouter, Depends, status

from {project_name}.application.use_cases.{endpoint_name} import (
    {usecase_class},
    {usecase_class}Request,
)
from {project_name}.presentation.schemas.{endpoint_name} import (
    {schema_class}Request,
    {schema_class}Response,
)
from {project_name}.infrastructure.web.dependencies import get_{endpoint_name}_service


router = APIRouter(prefix="/{version}/{endpoint_name}", tags=["{endpoint_name}"])


@router.post(
    "",
    response_model={schema_class}Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_{endpoint_name}(
    request: {schema_class}Request,
    service = Depends(get_{endpoint_name}_service),
) -> {schema_class}Response:
    """Create a new {endpoint_name}."""
    usecase = {usecase_class}(service)
    result = await usecase.execute({usecase_class}Request(**request.model_dump()))
    return {schema_class}Response(**result.model_dump())
'''


SCHEMA_TEMPLATE = '''"""
{endpoint_name} schemas.
"""
from pydantic import BaseModel


class {schema_class}Request(BaseModel):
    """Request schema for {endpoint_name}."""
    pass


class {schema_class}Response(BaseModel):
    """Response schema for {endpoint_name}."""
    pass
'''


def create_endpoint(name: str, version: str = "v1") -> None:
    """Create a new endpoint."""
    # Convert names to proper format
    endpoint_name = name.lower().replace("-", "_")
    usecase_class = "".join(word.capitalize() for word in endpoint_name.split("_"))
    schema_class = usecase_class
    project_name = Path.cwd().name

    # Create paths
    endpoint_dir = Path(f"src/{project_name}/infrastructure/web/endpoints/{version}")
    schema_dir = Path(f"src/{project_name}/presentation/schemas")

    # Create directories
    endpoint_dir.mkdir(parents=True, exist_ok=True)
    schema_dir.mkdir(parents=True, exist_ok=True)

    # Create __init__.py files
    for dir_path in [endpoint_dir, schema_dir]:
        init_file = dir_path / "__init__.py"
        init_file.touch(exist_ok=True)

    # Create endpoint file
    endpoint_path = endpoint_dir / f"{endpoint_name}.py"
    endpoint_content = ENDPOINT_TEMPLATE.format(
        endpoint_name=endpoint_name,
        usecase_class=usecase_class,
        schema_class=schema_class,
        project_name=project_name,
        version=version,
    )
    endpoint_path.write_text(endpoint_content)

    # Create schema file
    schema_path = schema_dir / f"{endpoint_name}.py"
    schema_content = SCHEMA_TEMPLATE.format(
        endpoint_name=endpoint_name,
        schema_class=schema_class,
    )
    schema_path.write_text(schema_content)

    print(f"Created endpoint {endpoint_name} (version {version})")
    print(f"- Endpoint: {endpoint_path}")
    print(f"- Schema: {schema_path}")
    print("\nDon't forget to:")
    print(f"1. Add the router to src/{project_name}/infrastructure/web/api.py")
    print(
        "2. Implement the service dependency in "
        f"src/{project_name}/infrastructure/web/dependencies.py"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new endpoint")
    parser.add_argument("--name", required=True, help="Name of the endpoint")
    parser.add_argument("--version", default="v1", help="API version (default: v1)")
    args = parser.parse_args()

    create_endpoint(args.name, args.version)
