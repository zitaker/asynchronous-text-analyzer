install:
	poetry install

flake8:
	poetry run flake8 app

docker-start:
	sudo docker-compose up --build