## Test task for Python backend-developer

#### Given:
The file text.txt

#### Create an asynchronous Fast API application based on a template:

```
import uvicorn
from fastapi import FastAPI

def create_app():
    app = FastAPI(docs_url='/')

    @app.on_event("startup")
    async def startup_event():
        ...

    return app

def main():
    uvicorn.run(
        f"{name}:create_app",
        host='0.0.0.0', port=8888,
        debug=True,
    )

if name == 'main':
    main()
```

#### Application:

provides an endpoint for uploading and sending line-by-line source data messages of the form ```{"datetime": "15.11.2023 15:00:25.001", "title": "Very fun book", "text": "...Rofl...lol../n..ololo..." }``` with an interval of 3 seconds

retrieves the source data from the message broker topic

calculates the number of occurrences of the letter "X" in lines of text from the "text" field

saves the result to the database

provides an endpoint for getting the result from the database in the form of ```[{"datetime": "15.11.2023 15:00:25.001", "title": "Very fun book", "x_avg_count_in_line": 0.012}, {"datetime": "18.01.2023 12:00:25.001", "title": "Other very fun book", "x_avg_count_in_line": 0.032} ]``` where x_avg_count_in_line is the average value of the number of occurrences for each of the uploaded texts

#### Requirements:

1. Apply asyncio
2. use SQL database
3. Use any message broker
4. Use Pedantic for data verification and parsing
5. Wrap the application in Docker
<hr>

#### Install:
1. Download the project.
2. Go to the root directory of the project.
3. Assemble the docker container and run it using the command ```docker-compose up --build```.
4. The application is available at ```0.0.0.0:8888```
