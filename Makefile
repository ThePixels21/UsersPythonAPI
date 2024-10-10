deploy:
	@docker compose build
	@docker compose up -d

run_migrations:
	@echo "Running migrations"
	@alembic revision --autogenerate -m "commit"
	@alembic upgrade head