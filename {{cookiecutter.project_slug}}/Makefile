.PHONY: setup run test coverage format lint typecheck check add-package add-usecase add-endpoint docs clean create-project

# Project variables
PYTHON := python3
PROJECT_NAME := {{cookiecutter.project_slug}}

# Development setup
setup:
	uv venv
	uv sync
	uv run pre-commit install

# Development
run:
	uv run uvicorn {{cookiecutter.project_slug}}.infrastructure.web.api:app --reload

shell:
	uv run ipython

# Testing
test:
	uv run pytest

test-unit:
	uv run pytest tests/unit

test-integration:
	uv run pytest tests/integration

coverage:
	uv run pytest --cov=src --cov-report=term-missing --cov-report=html

# Code quality
format:
	uv run ruff format .
	uv run ruff check --fix .

lint:
	uv run ruff check .
	uv run ruff format --check .

typecheck:
	uv run mypy src tests

check: format lint typecheck test

# Project evolution helpers
add-package:
	@test $(name) || (echo "Usage: make add-package name=package-name" && exit 1)
	mkdir -p packages/$(name)
	cd packages/$(name) && uv init --lib .
	@echo "Remember to add $(name) to workspace in pyproject.toml"

add-usecase:
	@test $(name) || (echo "Usage: make add-usecase name=usecase_name domain=domain_name" && exit 1)
	@test $(domain) || (echo "Usage: make add-usecase name=usecase_name domain=domain_name" && exit 1)
	scripts/create_usecase.py --name $(name) --domain $(domain)

add-endpoint:
	@test $(name) || (echo "Usage: make add-endpoint name=endpoint_name version=v1" && exit 1)
	@test $(version) || (echo "Usage: make add-endpoint name=endpoint_name version=v1" && exit 1)
	scripts/create_endpoint.py --name $(name) --version $(version)

add-domain:
	@test $(name) || (echo "Usage: make add-domain name=domain_name" && exit 1)
	scripts/create_domain.py --name $(name)

# Documentation
docs:
	uv run mkdocs serve

# Dependency management
sync:
	uv sync

update-deps:
	uv pip install --upgrade pip
	uv sync --upgrade

# Docker
docker-build:
	docker build -t $(PROJECT_NAME) .

docker-run:
	docker-compose up

# Cleanup
clean:
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +

# Create new project from template
create-project:
	@test $(name) || (echo "Usage: make create-project name=project-name" && exit 1)
	scripts/create_project.py --name $(name)
