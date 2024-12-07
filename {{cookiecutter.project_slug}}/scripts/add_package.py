#!/usr/bin/env python3
"""Script to add a new package to the workspace."""

import argparse
import subprocess
from pathlib import Path

import tomli
import tomli_w


def add_package_to_workspace(name: str) -> None:
    """Add a new package to the workspace."""
    # Create package directory
    package_path = Path("packages") / name
    package_path.mkdir(parents=True, exist_ok=True)

    # Initialize package
    subprocess.run(["uv", "init", "--lib", "."], cwd=package_path, check=True)

    # Update workspace configuration
    pyproject_path = Path("pyproject.toml")
    with open(pyproject_path, "rb") as f:
        config = tomli.load(f)

    workspace = (
        config.setdefault("tool", {}).setdefault("uv", {}).setdefault("workspace", {})
    )
    members = workspace.setdefault("members", ["."])

    # Only add packages/* if it's not already there
    if "packages/*" not in members:
        members.append("packages/*")
        with open(pyproject_path, "wb") as f:
            tomli_w.dump(config, f)
        print('Added "packages/*" to workspace')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a new package to the workspace")
    parser.add_argument("name", help="Name of the package to create")
    args = parser.parse_args()

    add_package_to_workspace(args.name)
