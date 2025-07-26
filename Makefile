.PHONY: help install run test

help:
	@echo "Commands:"
	@echo "  install    : Install dependencies using uv."
	@echo "  run        : Run the development server."
	@echo "  test       : Run tests using pytest."
	@echo "  uvicorn    : Run the app with uvicorn (production)."

install:
	uv pip install -e .[dev]

run:
	uv run litestar run -d --reload --host localhost --port 8000

test:
	uv run pytest

uvicorn:
	uv run uvicorn app.main:app --reload

check:
	uv run ruff format . --check \
	&& uv run ruff check .

format:
	uv run ruff format .
	uv run ruff check --fix-only --show-fixes --statistics .