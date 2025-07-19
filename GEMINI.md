# Gemini Project Guide: ml-project-template

This document provides a summary of the project's structure, conventions, and common commands for the Gemini agent.

## 1. Project Overview

This is a machine learning (ML) / deep learning (DL) project configured with modern Python tooling. It uses `uv` for package management and `Ruff` for unified linting and formatting. All configuration is centralized in `pyproject.toml`.

## 2. Key Files

- **`pyproject.toml`**: Defines all project metadata, dependencies (production, optional, dev), and tool configurations (like Ruff).
- **`uv.lock`**: Pins exact versions of all dependencies for reproducibility. Commit this file to version control.
- **`src/`**: Contains all the primary Python source code.
- **`tests/`**: Contains all the tests.
- **`notebooks/`**: Contains Jupyter notebooks.
- **`data/`**: Contains data files.

## 3. Dependency Management with `uv`

The project uses `uv` to manage dependencies.

- **Sync environment from `uv.lock`**:
  ```bash
  uv sync
  ```

- **Add a production dependency**:
  ```bash
  uv add <package-name>
  ```
  *Example:* `uv add numpy`

- **Add a development/testing dependency**:
  ```bash
  uv add <package-name> --dev
  ```
  *Example:* `uv add pytest --dev`

- **Install optional dependency groups**:
  ```bash
  uv pip install ".[<group1>,<group2>]"
  ```
  *Example:* `uv pip install ".[mlops,viz]"`

- **Remove a dependency**:
  ```bash
  uv remove <package-name>
  ```

## 4. Code Linting and Formatting with Ruff

Ruff is the single tool for linting and formatting. Configuration is in `pyproject.toml` under `[tool.ruff]`.

- **Check for linting errors**:
  ```bash
  uv run -- ruff check .
  ```

- **Fix linting errors automatically**:
  ```bash
  uv run -- ruff check --fix .
  ```

- **Format the entire codebase**:
  ```bash
  uv run -- ruff format .
  ```

## 5. Testing with Pytest

The project uses `pytest` for testing.

- **Run all tests**:
  ```bash
  uv run -m pytest
  ```

## 6. Running Code

- **Run a script**:
  ```bash
  uv run <script_name>.py
  ```
  *Example:* `uv run main.py`

- **Serve a FastAPI application** (if applicable):
  ```bash
  uv run -- uvicorn src.server:app
  ```

## 7. Building the Project

- **Build for distribution**:
  ```bash
  uv build
  ```
  This creates distributable artifacts in the `dist/` directory.
