clean:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

# Run command to install python libraryes
setUp: clean
	pip install -r requirements.txt

psql_start: clean
	docker-compose -f .docker/docker-compose.yml up -d db_postgresql

migrations: clean
	python manage.py makemigrations

migrate: clean
	python manage.py migrate

superUser: clean
	python manage.py createsuperuser

server: clean
	python manage.py runserver