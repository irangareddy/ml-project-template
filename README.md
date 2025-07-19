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

1.  **Install `uv`**:
    ```bash
    pip install uv
    ```

2.  **Clone the repository**:
    ```bash
    git clone <your-repo-url>
    cd ml-project-template
    ```

3.  **Sync the environment**:
    ```bash
    uv sync
    ```
    This will create a virtual environment in `.venv` and install all dependencies.

## Common Commands

- **Lint and Format**:
  ```bash
  # Check for issues
  uv run -- ruff check .

  # Fix issues automatically
  uv run -- ruff check --fix .

  # Format the codebase
  uv run -- ruff format .
  ```

- **Run Tests**:
  ```bash
  uv run -m pytest
  ```

- **Run a Script**:
  ```bash
  uv run main.py
  ```

## Learn More

To learn more about the philosophy and design of this template, read our [blog post](BLOG.md).
