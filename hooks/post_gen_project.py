#!/usr/bin/env python
import os
import shutil
import secrets

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

def generate_secret_key() -> str:
    """Generate a secure secret key."""
    return secrets.token_urlsafe(32)

def setup_project() -> None:
    """Post-generation project setup."""
    include_docker = '{{ cookiecutter.include_docker }}' == 'y'
    include_github_actions = '{{ cookiecutter.include_github_actions }}' == 'y'

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

    # Ensure proper package structure
    os.makedirs('src/{{cookiecutter.project_slug}}', exist_ok=True)

    # Initialize git repository
    init_git()

    # Generate and save secret key
    secret_key = generate_secret_key()
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(f'SECRET_KEY={secret_key}\n')

    print("\n✨ Project successfully created! ✨")
    print("\nNext steps:")
    print("1. Change directory to the project: cd {{cookiecutter.project_slug}}")
    print("2. Create a virtual environment: make setup")
    print("3. Install dependencies: make sync")
    print("4. Run the development server: make run")
    print("\nFor more information, check the README.md file.")

if __name__ == '__main__':
    setup_project()
