startup:
	uvicorn app.main:create_app --host 0.0.0.0 --port 8888 --reload

build:
	./build.sh

flake8:
	poetry run flake8 app