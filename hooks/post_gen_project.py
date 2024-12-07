#!/usr/bin/env python
import os
import shutil

def remove_file(filepath: str) -> None:
    """Remove a file if it exists."""
    if os.path.exists(filepath):
        os.remove(filepath)

def remove_folder_and_contents(folderpath: str) -> None:
    """Remove a folder and all its contents if it exists."""
    if os.path.exists(folderpath):
        shutil.rmtree(folderpath)

def init_git() -> None:
    """Initialize git repository."""
    os.system('git init')
    os.system('git add .')
    os.system('git commit -m "Initial commit from clean-fastapi-cookiecutter"')

def setup_project() -> None:
    """Post-generation project setup."""
    use_postgresql = '{{ cookiecutter.use_postgresql }}' == 'y'
    use_redis = '{{ cookiecutter.use_redis }}' == 'y'
    use_celery = '{{ cookiecutter.use_celery }}' == 'y'
    include_docker = '{{ cookiecutter.include_docker }}' == 'y'
    include_github_actions = '{{ cookiecutter.include_github_actions }}' == 'y'

    # Remove unused infrastructure components
    if not use_postgresql:
        remove_folder_and_contents('src/infrastructure/database/postgresql')
        remove_file('migrations/README.md')
        remove_file('alembic.ini')

    if not use_redis:
        remove_folder_and_contents('src/infrastructure/cache/redis')

    if not use_celery:
        remove_folder_and_contents('src/infrastructure/tasks')
        remove_file('celery.py')
        remove_file('src/infrastructure/celery_config.py')

    # Remove Docker files if not needed
    if not include_docker:
        remove_file('Dockerfile')
        remove_file('docker-compose.yml')
        remove_file('.dockerignore')

    # Remove GitHub Actions if not needed
    if not include_github_actions:
        remove_folder_and_contents('.github')

    # Create necessary directories
    os.makedirs('logs', exist_ok=True)
    os.makedirs('data', exist_ok=True)

    # Initialize git repository
    init_git()

    print("\n✨ Project successfully created! ✨")
    print("\nNext steps:")
    print("1. Create a virtual environment: make setup")
    print("2. Install dependencies: make sync")
    print("3. Run the development server: make run")
    print("\nFor more information, check the README.md file.")

if __name__ == '__main__':
    setup_project()
