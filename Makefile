tests:
	poetry install
	poetry run pytest

format:
	poetry install
	poetry run black .

rover:
	poetry install
	poetry run python rover.py ignite

compose:
	docker-compose run rover bash -c "make rover"
