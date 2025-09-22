.PHONY: qa black ruff install build publish publish-test help

# Default target
help:
	@echo "Available commands:"
	@echo "  qa           - Run code quality checks (black + ruff)"
	@echo "  black        - Format code with black"
	@echo "  ruff         - Lint code with ruff"
	@echo "  install      - Install package in development mode"
	@echo "  build        - Build distribution packages"
	@echo "  publish-test - Build and upload to TestPyPI"
	@echo "  publish      - Build and upload to PyPI"

# Code quality checks
qa: black ruff

# Format code with black
black:
	black .

# Lint code with ruff
ruff:
	ruff check

# Install package in development mode
install:
	python -m pip install .
	# Use isolated mode to avoid picking up local chatgpt_query.py.
	python -I dev_install.py

# Build distribution packages
build:
	python -m build

# Build and upload to TestPyPI
publish-test: build
	python -m twine upload --repository testpypi dist/*

# Build and upload to PyPI
publish: build
	python -m twine upload dist/*
