.PHONY: lint lint-ruff lint-mypy format test run

lint: lint-ruff lint-mypy

lint-ruff:
	uv run ruff check .

lint-mypy:
	uv run mypy game/

format:
	uv run ruff format .

test:
	uv run pytest -q

run:
	uv run python -m game
