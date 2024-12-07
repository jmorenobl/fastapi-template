"""
FastAPI application setup.
"""
from fastapi import FastAPI
from {{cookiecutter.project_slug}}.infrastructure.config import settings


def create_app() -> FastAPI:
    """Create FastAPI application."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="API Documentation",
    )
    
    # Add middleware
    
    # Register routes
    
    return app

app = create_app()
