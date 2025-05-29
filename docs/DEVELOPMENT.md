# Development Guide

## Setup

1. Install dependencies: `make install`
2. Install pre-commit hooks: `make setup-hooks`
3. Run tests: `make test`

## Code Quality

- **Formatting**: `make format`
- **Linting**: `make lint`
- **Auto-fix**: `make autofix`
- **All checks**: `make check-all`

## Testing

- **Run tests**: `make test`
- **With coverage**: `make test-cov`
- **View coverage**: Open `htmlcov/index.html`

## Workflow

1. Make changes
2. Run `make autofix` to fix formatting/linting
3. Run `make test` to ensure tests pass
4. Commit (pre-commit hooks will run automatically)
