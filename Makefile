.PHONY: up down test lint

up:
	docker compose up --build --wait

down:
	docker compose down

test:
	docker compose run --build --rm api python -m pytest -p no:cacheprovider

lint:
	docker compose run --build --rm --no-deps api ruff check --no-cache .
