.PHONY: help install install-dev test lint format clean build release

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package in development mode
	pip install -e .

install-dev: ## Install development dependencies
	pip install -e ".[dev]"
	pre-commit install

test: ## Run tests
	pytest tests/ -v --cov=appgen --cov-report=term-missing

test-watch: ## Run tests in watch mode
	pytest tests/ -v --cov=appgen --cov-report=term-missing -f

lint: ## Run linting checks
	black --check --diff .
	isort --check-only --diff .
	flake8 .
	mypy appgen/ config.py generator/ --ignore-missing-imports

format: ## Format code
	black .
	isort .

security: ## Run security checks
	bandit -r . -f json -o bandit-report.json

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: ## Build the package
	python -m build

check-build: ## Check the built package
	twine check dist/*

release: ## Build and release to PyPI (requires PYPI_API_TOKEN)
	python -m build
	twine upload dist/*

ci: ## Run CI checks locally
	make lint
	make test
	make security
	make build
	make check-build

pre-commit: ## Run pre-commit hooks on all files
	pre-commit run --all-files

pre-commit-update: ## Update pre-commit hooks
	pre-commit autoupdate

version: ## Show current version
	@python -c "import appgen; print(appgen.__version__)"

bump-patch: ## Bump patch version
	cz bump --yes

bump-minor: ## Bump minor version
	cz bump --yes --increment MINOR

bump-major: ## Bump major version
	cz bump --yes --increment MAJOR 