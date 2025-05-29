.PHONY: help install test lint format clean run-pipeline
CODE_DIRS = src/ tests/

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	uv sync

test: ## Run tests
	uv run pytest tests/ -v

test-cov: ## Run tests with coverage
	uv run pytest tests/ -v --cov=src --cov-report=term-missing --cov-report=html

format: ## Format code using Ruff formatter
	@echo "Formatting code..."
	uv run ruff format $(CODE_DIRS)

format-check: ## Check if code is formatted correctly (for CI)
	@echo "Checking code formatting..."
	uv run ruff format --check $(CODE_DIRS)

lint: ## Check for linting issues using Ruff (no fixes)
	@echo "Linting code..."
	uv run ruff check $(CODE_DIRS)

lint-fix: ## Attempt to automatically fix linting issues using Ruff
	@echo "Attempting to fix linting issues..."
	uv run ruff check --fix $(CODE_DIRS)

autofix: lint-fix format ## Automatically fix linting issues and then format code
	@echo "Code auto-fixing and formatting complete."

clean: ## Clean up generated files
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .mypy_cache/
	rm -rf __pycache__/
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyc" -delete

run-pipeline: ## Run the complete ML pipeline
	python src/load_data.py
	python src/split_dataset.py --test_size 0.2
	python src/train.py
	python src/evaluate.py

check-all: lint test ## Run all checks (lint + test) 
