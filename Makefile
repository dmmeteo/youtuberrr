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
	uv run litestar run -d --reload

test:
	uv run pytest

uvicorn:
	uv run uvicorn app.main:app --reload
