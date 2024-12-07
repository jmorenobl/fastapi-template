# Clean FastAPI Cookiecutter

A production-ready FastAPI project generator that follows clean architecture principles and modern Python best practices. This template provides a solid foundation for building scalable web APIs with optional support for PostgreSQL, Redis, Celery, Docker, and more.

## ✨ Features

- **Clean Architecture** structure with clear separation of concerns
  - Domain-driven design principles
  - SOLID principles implementation
  - Clear dependency boundaries
  - Easy to test and maintain

- **Modern Python Setup**
  - Python 3.11+ support
  - Type hints everywhere
  - UV for dependency management
  - Ruff for fast, comprehensive linting
  - MyPy for strict type checking
  - Pre-commit hooks configured

- **FastAPI Best Practices**
  - Structured API routing
  - Comprehensive error handling
  - Request validation
  - Response serialization
  - OpenAPI documentation

- **Testing Suite**
  - Pytest configuration
  - Async test support
  - Factory-based fixtures
  - Integration test helpers
  - 100% test coverage setup

- **Optional Components**
  - 🐘 PostgreSQL with SQLAlchemy and Alembic
  - 🔄 Redis for caching
  - 🗃️ Celery for background tasks
  - 🐋 Docker and docker-compose setup
  - 🔄 GitHub Actions CI/CD

## 🚀 Quickstart

1. Install Cookiecutter:
```bash
pip install cookiecutter
```

2. Generate your project:
```bash
cookiecutter gh:yourusername/clean-fastapi-cookiecutter
```

3. Answer the prompts:
```
project_name [My FastAPI Project]: 
project_slug [my_fastapi_project]: 
project_description [A FastAPI project with clean architecture]: 
author_name [Your Name]: 
author_email [your.email@example.com]: 
version [0.1.0]: 
python_version [3.11]: 
include_docker [y]: 
include_github_actions [y]: 
open_source_license [MIT]: 
```

4. Set up your development environment:
```bash
cd my_fastapi_project
make setup
```

5. Run the development server:
```bash
make run
```

## 🏗️ Project Structure

The generated project follows this structure:

```
my_fastapi_project/
├── src/
│   ├── core/
│   │   ├── domain/          # Business entities and rules
│   │   │   ├── entities/
│   │   │   └── value_objects/
│   │   ├── application/     # Use cases and interfaces
│   │   │   ├── interfaces/
│   │   │   └── use_cases/
│   │   └── infrastructure/  # External implementations
│   │       ├── database/
│   │       └── messaging/
│   └── api/
│       ├── v1/             # API version 1
│       └── health/         # Health checks
├── tests/
│   ├── unit/
│   └── integration/
├── docs/                   # Project documentation
├── scripts/               # Utility scripts
└── pyproject.toml        # Project configuration
```

## 🛠️ Development Commands

The generated project includes a Makefile with useful commands:

```bash
# Setup development environment
make setup

# Run development server
make run

# Run tests
make test
make test-unit
make test-integration
make coverage

# Code quality
make format        # Format code with ruff
make lint         # Run linting
make typecheck    # Run type checking
make check        # Run all checks

# Documentation
make docs         # Serve documentation locally

# Dependencies
make sync         # Sync dependencies
make update-deps  # Update dependencies

# Docker
make docker-build
make docker-run
```

## 📋 Template Options

### Docker Setup
If you choose `include_docker=y`:
- Adds Dockerfile and docker-compose.yml
- Configures multi-stage builds
- Sets up development and production profiles
- Includes health checks

### GitHub Actions
If you choose `include_github_actions=y`:
- Configures CI/CD pipeline
- Sets up testing and linting
- Configures Docker image builds
- Adds dependency scanning

## 🌱 Project Evolution

The template is designed to grow with your project:

### Adding New Components

```bash
# Add a new domain module
make add-domain name=users

# Add a new use case
make add-usecase name=create_user domain=users

# Add a new API endpoint
make add-endpoint name=users version=v1

# Add a new package to the workspace
make add-package name=my-package
```

### Workspace Management

The project uses UV workspace for managing multiple packages:

1. Add new packages:
```bash
make add-package name=my-package
```

2. Update workspace in pyproject.toml:
```toml
[tool.uv.workspace]
members = [".", "packages/*"]
```

## 📚 Documentation

The generated project includes comprehensive documentation:

- `docs/architecture.md` - Architectural decisions and patterns
- `docs/development.md` - Development workflow and guidelines
- `docs/contributing.md` - Contribution guidelines
- API documentation at `http://localhost:8000/docs`

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on:

- Code of Conduct
- Development process
- How to submit pull requests
- Coding standards

## 📜 License

This project is licensed under the terms of the MIT license.

## 🙏 Acknowledgments

This template is inspired by various best practices and patterns from:
- Clean Architecture by Robert C. Martin
- Domain-Driven Design by Eric Evans
- FastAPI best practices
- Modern Python development tools and practices

## ❓ FAQ

**Q: Why use this template?**
A: This template provides a production-ready foundation following best practices, saving you time in project setup and ensuring scalability.

**Q: Can I use different dependencies?**
A: Yes, the template is flexible. You can modify `pyproject.toml` and related configurations after generation.

**Q: How do I update the template in an existing project?**
A: While cookiecutter doesn't support direct updates, you can manually sync changes from the template repository.

## 🌟 Projects Using This Template

- Add your project here!

## 📫 Support

- Create an issue for bug reports
- Start a discussion for feature requests
- Star the project if you find it useful!