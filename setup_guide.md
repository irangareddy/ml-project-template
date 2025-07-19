# Step-by-Step Guide: Building a Comprehensive ML/DL Project Setup (2025)

Follow these steps to create a modern, production-grade machine learning (ML) or deep learning (DL) project using the latest Python ecosystem best practices—leveraging `pyproject.toml`, `uv`, `uv.lock`, and Ruff as your unified linter/formatter.

## 1. **Install Prerequisites**

- **Python 3.10+**: Ensure you have Python 3.10 or later installed (ideally, use the latest stable release).
- **uv**: Install the all-in-one package/dependency manager:

  ```bash
  pip install uv
  ```

- **git**: Set up version control for safe collaboration.

## 2. **Initialize Your Project Directory**

- **Create a new project with uv**:

  ```bash
  uv init ml-project-template
  cd ml-project-template
  ```

  This generates:

  - `.gitignore`
  - `.python-version`
  - `README.md`
  - `main.py`
  - `pyproject.toml`
  - `.venv/` (created after running a uv command)
  - `uv.lock` (appears after adding dependencies or syncing)

## 3. **Configure pyproject.toml**

### a. **Core Project Metadata**

Edit `[project]` in `pyproject.toml`:

```toml
[project]
name = "ml-project-template"
version = "0.1.0"
description = "Comprehensive ML/DL project"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
  "numpy",
  "pandas",
  "scikit-learn",
  "tensorflow",      # or "torch" for PyTorch projects
  "fastapi"          # optional: for serving models as APIs
]
```

### b. **Optional Dependencies**

Separate MLOps, NLP, visualization, and notebook tools for on-demand install:

```toml
[project.optional-dependencies]
mlops = ["mlflow", "wandb", "dvc"]
nlp = ["transformers", "spacy"]
viz = ["matplotlib", "seaborn", "plotly"]
notebooks = ["jupyter", "jupyterlab"]
```

### c. **Development/Testing Tool Groups**

Organize dev/test/lint tooling:

```toml
[dependency-groups]
test = ["pytest", "pytest-cov"]
lint = ["ruff"]
notebook = ["jupyter", "jupyterlab"]
```

## 4. **Set Up Unified Linting and Formatting (Ruff Only)**

Add and configure Ruff for all your Python code:

```bash
uv add ruff --dev
```

Add configuration to `pyproject.toml`:

```toml
[tool.ruff]
target-version = "py312"
line-length = 120
fix = true
extend-exclude = ["notebooks/", "data/"]
```

## 5. **Add/Organize Source Code**

Create a clean folder structure:

```
ml-project-template/
├── src/
│   ├── __init__.py
│   ├── data/
│   ├── models/
│   ├── pipelines/
│   └── utils/
├── tests/
├── notebooks/
├── data/
```

- **Place all code under `src/`** for import hygiene.
- Keep datasets, notebooks, scripts, and tests clearly separated.

## 6. **Manage Dependencies**

- **Add production dependencies** (already in `pyproject.toml`) using:

  ```bash
  uv add pandas scikit-learn tensorflow
  ```

- **Add extra/optional groups** by editing `pyproject.toml` or:

  ```bash
  uv add mlflow --optional mlops
  uv add transformers --optional nlp
  ```

- **Install extras when needed**:

  ```bash
  uv pip install ".[mlops,viz]"
  ```

## 7. **Pin Exact Dependencies for Reproducibility**

- After any dependency change, uv updates the cross-platform `uv.lock` file, recording exact versions.
- Always commit `uv.lock` to git; never edit manually.

## 8. **Setup Version Control**

- Initialize git in your project folder:

  ```bash
  git init
  git add .
  git commit -m "Initial ML/DL project setup"
  ```

## 9. **Testing, Linting, and Formatting**

- **Lint entire codebase**:

  ```bash
  uv run -- ruff check .
  ```

- **Auto-fix issues**:

  ```bash
  uv run -- ruff check --fix .
  ```

- **Format code**:

  ```bash
  uv run -- ruff format .
  ```

- **Run tests**:

  ```bash
  uv run -m pytest
  ```

## 10. **Develop, Run, and Serve Your ML/DL Code**

- Run your main script (and check the environment is in sync):

  ```bash
  uv run main.py
  ```

- Serve models (with FastAPI):

  ```bash
  uv run -- uvicorn src.server:app
  ```

## 11. **Sync, Build, and Distribute**

- **Sync dependencies and virtual environment**:

  ```bash
  uv sync
  ```

- **Build for distribution**:

  ```bash
  uv build
  ```

- Distribute `dist/` artifacts to PyPI or your own repository, if needed.

## 12. **General Best Practices**

- Use only Ruff for linting/formatting (no flake8, black, isort, etc.).
- Document the project in `README.md`.
- Add **pre-commit hooks** for Ruff to catch issues before pushing.
- Leverage `pyproject.toml` for all configuration.
- Regularly update dependencies and lockfile.
- Separate data, code, notebooks, and configs.
- Follow modular design—split data loading, model, pipeline, and utility code.

### **Frequently Used Commands Reference Table**

| Scenario            | Command                                    |
|---------------------|--------------------------------------------|
| Add dependency      | `uv add `                         |
| Remove dependency   | `uv remove `                      |
| Add test group      | `uv add pytest --dev`                      |
| Install extras      | `uv pip install ".[mlops,notebooks]"`      |
| Sync environment    | `uv sync`                                  |
| Lint code           | `uv run -- ruff check .`                   |
| Format code         | `uv run -- ruff format .`                  |
| Run tests           | `uv run -m pytest`                         |
| Build project       | `uv build`                                 |

You now have a **future-proof, maintainable, high-performance ML/DL project setup** ready for scalable research and production engineering.

: CLI Reference | Astral Docs  
: Ruff Documentation | astral.sh