# Tutorial: Get started with Data Version Control (DVC)

## Project Structure

```text
mlops-get-started-iris/
├── .git/                   # Git version control
├── .venv/                  # Virtual environment
├── data/                   # Data directory (DVC tracked)
│   ├── .gitignore          # Ignore data files in git
│   ├── features_iris.csv   # Processed features
│   ├── train.csv           # Training dataset
│   ├── test.csv            # Test dataset
│   ├── model.joblib        # Trained model
│   └── eval.json           # Evaluation metrics
├── src/                    # Source code
│   ├── load_data.py        # Data loading and preprocessing
│   ├── split_dataset.py    # Data splitting logic
│   ├── train.py            # Model training
│   ├── evaluate.py         # Model evaluation
│   └── utils.py            # Utility functions
├── tests/                   # Test suite
│   ├── __init__.py         # Tests package
│   └── test_utils.py       # Utility function tests
├── .gitignore              # Git ignore patterns
├── .python-version         # Python version specification
├── config.yaml             # ML pipeline configuration
├── dvc.yaml                # DVC pipeline definition
├── Makefile                # Development commands
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Dependency lock file
└── README.md               # Project documentation
```

## Prerequisites

- Python 3.11+
- `uv` ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- Git
- Make (optional, for using Makefile commands)

## Quick Start: Installation & Setup

1. **Clone the repository:**

    ```bash
    git clone REPO_URL
    cd REPO_NAME
    ```

2. **Install dependencies:**

    ```bash
    # Using uv (recommended)
    uv sync
    
    # Or using make
    make install
    ```

3. **Activate the virtual environment:**

    ```bash
    # On macOS and Linux:
    source .venv/bin/activate
    # On Windows:
    # .\.venv\Scripts\activate
    ```

## Running the Pipeline

### Option 1: Manual Execution

```bash
python src/load_data.py
python src/split_dataset.py --test_size 0.2
python src/train.py
python src/evaluate.py
```

### Option 2: Using Make

```bash
make run-pipeline
```

### Option 3: Using DVC (Recommended for MLOps)

```bash
# Run the entire pipeline
dvc repro

# Run specific stage
dvc repro train
```

## Development Workflow

### Code Quality

```bash
# Format code
make format

# Check formatting
make format-check

# Run linting
make lint

# Run all checks
make check-all
```

### Testing

```bash
# Run tests
make test

# Run tests with coverage
make test-cov
```

### Configuration

The pipeline is configured via `config.yaml`. Key parameters:

- **Data splitting**: `data.test_size`, `data.random_state`
- **Model parameters**: `model.parameters.*`
- **File paths**: `paths.*`

## MLOps Features

### Data Version Control (DVC)

- **Track data**: `dvc add data/`
- **Version models**: Automatically tracked in DVC pipeline
- **Reproduce experiments**: `dvc repro`
- **Compare metrics**: `dvc metrics show`

### Pipeline Automation

- **Reproducible**: DVC pipeline ensures reproducibility
- **Parameterized**: Configuration-driven experiments
- **Tracked**: All artifacts and metrics are versioned

### Code Quality

- **Type hints**: Full type annotation coverage
- **Linting**: Ruff for code quality
- **Testing**: Pytest with coverage reporting
- **Formatting**: Consistent code style

## Available Commands

Run `make help` to see all available commands:

```bash
make help
```

## Learning Objectives

This repository demonstrates:

1. **Data Version Control** with DVC
2. **Pipeline Automation** and reproducibility
3. **Configuration Management** for ML experiments
4. **Code Quality** practices (linting, testing, type hints)
5. **MLOps Workflow** from data to model evaluation
