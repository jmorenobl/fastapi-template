# Clean FastAPI Template

A production-ready template for building scalable FastAPI applications following clean architecture principles.

## 🏗️ Project Structure

```
{{cookiecutter.project_slug}}/
├── src/
│   ├── core/                      # Core business logic
│   │   ├── domain/               # Business entities and rules
│   │   │   ├── entities/        # Domain entities
│   │   │   └── value_objects/   # Value objects
│   │   ├── application/         # Application services
│   │   │   ├── interfaces/     # Abstract interfaces
│   │   │   └── use_cases/     # Use case implementations
│   │   └── infrastructure/     # External services implementation
│   │       ├── database/      # Database implementations
│   │       └── messaging/     # Message queue implementations
│   └── api/                    # API layer
│       ├── v1/               # API version 1 routes
│       └── health/          # Health check endpoints
├── tests/                    # Test suite
│   ├── unit/              # Unit tests
│   └── integration/      # Integration tests
├── docs/                 # Documentation
├── scripts/             # Utility scripts
└── pyproject.toml      # Project configuration
```

## 🚀 Quick Start

1. Create a new project from this template:
```bash
make create-project name=my-project
```

2. Set up the development environment:
```bash
make setup
```

3. Start the development server:
```bash
make run
```

## 📦 Adding New Components

### Adding a New Package
```bash
make add-package name=my-package
```
This will:
- Create a new package directory in `packages/`
- Set up the package structure
- Add it to the workspace

### Adding a New Use Case
```bash
make add-usecase name=create_user domain=users
```
This will:
- Create use case boilerplate
- Create corresponding tests
- Add necessary interfaces

### Adding a New API Endpoint
```bash
make add-endpoint name=users version=v1
```
This will:
- Create route module
- Create request/response models
- Add OpenAPI documentation

## 🧪 Testing

```bash
# Run all tests
make test

# Run unit tests only
make test-unit

# Run integration tests only
make test-integration

# Run tests with coverage
make coverage
```

## 🔧 Development Tools

```bash
# Format code
make format

# Run linting
make lint

# Run type checking
make typecheck

# Run all checks
make check
```

## 📝 Documentation

- [Architecture Guide](docs/architecture.md)
- [Development Guide](docs/development.md)
- [Contributing Guide](docs/contributing.md)

## 🌱 Project Evolution

This template is designed to grow with your project. Here's how to handle common scenarios:

### 1. Adding New Dependencies

1. Add to `pyproject.toml`:
```toml
[project]
dependencies = [
    "new-package>=1.0.0"
]
```

2. Update environment:
```bash
make sync
```

### 2. Creating a New Library

When your project grows and you need to extract functionality:

1. Create a new library:
```bash
make create-lib name=my-lib
```

2. Move relevant code to the new library
3. Add library to workspace in root `pyproject.toml`
4. Update dependencies

### 3. Scaling the Application

As your application grows:

1. Use the provided scripts to maintain consistency:
```bash
make add-domain name=new-domain  # Add a new domain with entities
make add-repository name=new-repo  # Add a new repository
make add-service name=new-service  # Add a new service
```

2. Follow the architecture guidelines in `docs/architecture.md`
3. Maintain test coverage with `make coverage`

## 📊 Project Quality Metrics

- Test Coverage: Minimum 80% required
- Type Safety: Strict mypy checks enabled
- Code Quality: Enforced by ruff and black
- Documentation: Required for all public APIs

## 🤝 Contributing

See our [Contributing Guide](docs/contributing.md) for details on:
- Code style
- Pull request process
- Development workflow
- Release process

## 📜 License

MIT