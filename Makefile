startup:
	uvicorn app.main_app:create_app --host 0.0.0.0 --port 8888 --reload

build:
	./build.sh