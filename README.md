# ML/DL Project Template (2025)

This is a modern, production-grade machine learning (ML) and deep learning (DL) project template for Python. It is designed to be fast, reproducible, and easy to maintain.

It leverages the latest high-performance tools from the Python ecosystem, including:

- **[uv](https://github.com/astral-sh/uv)**: An extremely fast Python package installer and resolver to replace `pip` and `venv`.
- **[Ruff](https://github.com/astral-sh/ruff)**: An extremely fast Python linter and code formatter to replace `Flake8`, `isort`, and `Black`.

All project configuration is centralized in the `pyproject.toml` file.

## Features

- **Unified Tooling**: `uv` and `Ruff` for a streamlined development experience.
- **Reproducible Environments**: `uv.lock` file ensures deterministic builds.
- **Organized Structure**: Clear separation of code, tests, notebooks, and data.
- **Optional Dependencies**: Easily manage dependencies for different environments (e.g., `mlops`, `viz`).

## Getting Started

1. **Install Prerequisites**:
    - **`uv`**:

      ```bash
      pip install uv
      ```

    - **`task`**: Follow the installation instructions at [taskfile.dev](https://taskfile.dev/installation/).

2. **Clone the repository**:

    ```bash
    git clone <your-repo-url>
    cd ml-project-template
    ```

3. **Sync and Setup Hooks**:

    ```bash
    task sync
    task install-hooks
    ```

    This will create a virtual environment, install all dependencies, and set up the pre-commit hooks.

## Task Commands

This project uses [Task](https://taskfile.dev) as a task runner. All common commands are defined in the `Taskfile.yml`.

- **`task lint`**: Check for linting errors.
- **`task format`**: Format the codebase.
- **`task fix`**: Fix linting errors automatically.
- **`task test`**: Run tests.
- **`task run`**: Run the main application script.
- **`task serve`**: Serve the FastAPI application.
- **`task sync`**: Sync the environment with `uv.lock`.
- **`task build`**: Build the project for distribution.

To see a list of all available tasks, run `task --list`.

## Learn More

To learn more about the philosophy and design of this template, read our [blog post](BLOG.md).
