# Real-time stock price dashboard 

## Project overview

The project is built from two main components:

- a backend that periodically fetches user-defined stock data from Finnhub
- a front-end that utilizes Plotly and Dash to visualize the gathered data on
  interactive charts

We use Celery backed by Redis as the message broker and QuestDB as storage to periodically fetch data.


### Prerequisites

- Python 3.8 and above
- Docker & Docker Compose
- Finnhub account and sandbox API key


### Installing QuestDB & Redis

To install the services required for our project, we are using Docker and Docker
Compose. Within the project root, create a file, called docker-compose.yml. 

```yaml
version: "3"

volumes:
  questdb_data: {}

services:
  redis:
    image: "redis:latest"
    ports:
      - "6379:6379"

  questdb:
    image: "questdb/questdb:latest"
    volumes:
      - questdb_data:/root/.questdb/db
    ports:
      - "9000:9000"
      - "8812:8812"
```

When run `docker-compose up`, DB and Redis will fire up.
We can access DB interactive console on
[http://127.0.0.1:9000](http://127.0.0.1:9000/).

### Create the database table

```sql
CREATE TABLE
      quotes(stock_symbol SYMBOL CAPACITY 5 CACHE INDEX, 
             current_price DOUBLE,
             high_price DOUBLE,
             low_price DOUBLE,
             open_price DOUBLE,
             percent_change DOUBLE,
             tradets TIMESTAMP, -- timestamp of the trade
             ts TIMESTAMP)      -- time of insert in our table
      timestamp(ts)
PARTITION BY DAY;
```

### Create venv and install dependencies

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


### Create .env file where API KEY and tickers are stored

```
SMD_API_KEY = "<SANDBOX API KEY>"
SMD_FREQUENCY = 10
SMD_SYMBOLS = ["AAPL","DOCN","EBAY"]
```

To retrieve the key, sign up to Finnhub, and your API key will appear on the dashboard after login.



 ### Shedule a job using Celery to retrieve data. Execute command in venv:

```shell
python -m celery --app app.worker.celery_app worker --beat -l info -c 1
```


 ### Run dashboard

Make sure that the Docker containers are started and execute `PYTHONPATH=. python app/main.py` from
the project root:

```shell
$ PYTHONPATH=. python app/main.py
```

Navigate to http://127.0.0.1:8050/, to see the application in action.


### If have problems with Dash:

pip uninstall werkzeug
pip install -v https://github.com/pallets/werkzeug/archive/refs/tags/2.0.1.tar.gz


### To run tests:

coverage run -m unittest discover