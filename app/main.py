import json
import logging

import requests
from fastapi import FastAPI

app: FastAPI = FastAPI()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def get_quote() -> str:
    url: str = "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json"
    response: requests.Response = requests.get(url)

    logging.info(f"Request to {url} returned {response.status_code}")
    logging.info(f"Response: {response.text}")

    data: dict = json.loads(response.text)

    logging.info(f"Quote: {data['quoteText']}")

    return data["quoteText"]


@app.get("/")
def root():
    try:
        quote: str = get_quote()

    except Exception as e:
        logging.error(f"Error getting quote: {e}")

        return {"message": "Error getting quote"}

    return {"quote": quote}
