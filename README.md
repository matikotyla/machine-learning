# Machine Learning Project

A modern Python environment for Machine Learning, Data Science, and Linear Algebra research. This project uses **uv** for blazingly fast dependency management and the **src layout** for professional code organization.

## 🚀 Quick Start

### 🐍 Prerequisites
Ensure you have **uv** installed:
```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
```

## Setup

Clone the repository and sync the environment. This command automatically creates a virtual environment, installs the correct Python version, and sets up all dependencies in editable mode.

git clone [https://github.com/yourusername/machine-learning.git](https://github.com/yourusername/machine-learning.git)
cd machine-learning
uv sync

## Activate quality tools

Install the pre-commit hooks to ensure code formatting (Ruff) and type checking (Mypy) run automatically before every commit:

```bash
uv run pre-commit install
```

## 📘 Verify setup

Run the included test to ensure everything works:

```bash
uv run test
```

## 📂 Project Structure

We use the **src layout**, which is standard for serious Python projects. It keeps your source code separate from configuration and other assets.

```
machine-learning/
├── pyproject.toml      # Project metadata and dependencies
├── uv.lock             # Deterministic lockfile
└── src/                # Root for all source code
    ├── data/           # Raw data files
    ├── tests/          # Tests
    ├── data_science/   # Data analysis and exploration scripts
    ├── machine_learning/ # Model training and evaluation
    └── linear_algebra/ # Mathematical utility modules
```

## 💻 Development workflow

### ⚙️ Running scripts

Because we use the src layout, always run scripts as modules using the -m flag to ensure imports resolve correctly.

```bash
uv run python -m data_science.analyse
uv run python -m machine_learning.train
```

### 🧪 Running Tests

Run the test suite using pytest:

```bash
uv run test
```

### 🔗 Linting and Formatting

```bash
uv run poe lint            # Lint and auto-fix
uv run poe format          # Format code
```

### 🔍 Type checking

```bash
uv run poe check
```

### 📝 Committing

```bash
uv run poe commit
```

### 📦 Managing dependencies

To add a new package (like `scikit-learn`):

```bash
uv add scikit-learn
```

To add a tool only needed for development (like `ipykernel` for Jupyter):

```bash
uv add --dev ipykernel
```

To update all dependencies:

```bash
uv update
```

### ✅ Quality checks

To run all quality checks (linting, formatting, type checking, testing):

```bash
uv run poe all
```
