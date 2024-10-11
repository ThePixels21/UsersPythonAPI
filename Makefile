deploy:
	@docker compose build
	@docker compose up -d

stop:
	@docker compose down

run_migrations:
	@echo "Running migrations"
	@alembic revision --autogenerate -m "commit"
	@alembic upgrade head

reset_migrations:
	@echo "Resetting migrations"
	@rm alembic.ini
	@mv FastAPI/app/alembic/env.py .
	@rm -rf FastAPI/app/alembic
	@alembic init FastAPI/app/alembic
	@mv env.py FastAPI/app/alembic/
	@make delete_volumes
	@echo "Done"

delete_volumes:
	@echo "Deleting volumes"
	@sudo rm -rf MySQL/volumes
	@echo "Done"