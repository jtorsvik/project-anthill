from datetime import datetime, timedelta, timezone
import time
from polygon import RESTClient
from requests.exceptions import HTTPError

class PolygonAPI():
    def __init__(self, api_key='rxdopHP51cQc3RtUbZrNj7Gy0CkpR2Qn'):
        self.api_key = api_key
        self.client = RESTClient(api_key=self.api_key)

    def fetch_aggs_with_backoff(self, ticker, from_date, to_date, multiplier=1, timespan='minute', limit=50000, sleep=True):
        retries = 0
        max_retries = 5
        backoff = 1  # start with 1 second

        aggs = dict()

        while True:
            try:
                for a in self.client.list_aggs(
                    ticker=ticker,
                    multiplier=multiplier,
                    timespan=timespan,
                    limit=1000,
                    from_=from_date,
                    to=to_date
                ):
                    timestamp = datetime.fromtimestamp(a.timestamp / 1000, timezone.utc)
                    aggs[timestamp] = a.__dict__
                    if sleep:
                        time.sleep(0.25)  # small delay between pages
                break  # exit loop if successful

            except HTTPError as e:
                if e.response.status_code == 429:
                    if retries < max_retries:
                        print(f"Rate limit hit. Retrying in {backoff} seconds...")
                        time.sleep(backoff)
                        retries += 1
                        backoff *= 2  # exponential backoff
                    else:
                        print("Max retries exceeded.")
                        break
                else:
                    raise  # re-raise other HTTP errors
        return aggs