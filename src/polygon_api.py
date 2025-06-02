from datetime import datetime, timedelta, timezone
import time
from polygon import RESTClient
from requests.exceptions import HTTPError

class PolygonAPI():
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = RESTClient(api_key=self.api_key)

    def fetch_aggs_with_backoff(self,
                                ticker,
                                from_date,
                                to_date,
                                multiplier=1,
                                timespan='minute',
                                limit=1000,
                                sleep=True):
        
        """

        Fetches aggregate data for a given ticker symbol with exponential backoff for rate limiting.

        Description:
        This method retrieves aggregate data for a specified ticker symbol from the Polygon API.
        
        Parameters:
        ticker (str): The ticker symbol to fetch aggregate data for.
        from_date (str): The start date for the data in 'YYYY-MM-DD' format.
        to_date (str): The end date for the data in 'YYYY-MM-DD' format.
        multiplier (int): The multiplier for the aggregation (default is 1).
        timespan (str): The timespan for the aggregation (default is 'minute').
        limit (int): The maximum number of results to return (default is 1000).
        sleep (bool): Whether to sleep between requests to avoid hitting rate limits (default is True).
        
        Returns:
        dict: A dictionary containing aggregate data with timestamps as keys.
        """


        retries = 0
        max_retries = 5
        backoff = 1  # start with 1 second

        aggs = dict()

        while True:
            try:
                # Fetch aggregate data using the Polygon client
                for a in self.client.list_aggs(
                    ticker=ticker,
                    multiplier=multiplier,
                    timespan=timespan,
                    limit=limit,
                    from_=from_date,
                    to=to_date
                ):
                    timestamp = datetime.fromtimestamp(a.timestamp / 1000, timezone.utc)
                    aggs[timestamp] = a.__dict__

                # If sleep is True, wait for a short time to avoid hitting rate limits
                    if sleep:
                        time.sleep(0.25)
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
    
        # Function to calculate the last working day
    def last_working_day(self):

        """
        Calculates the last working day based on the current date.

        Description:
        This method determines the last working day based on the current date.

        Returns:
        str: The last working day in 'YYYY-MM-DD' format.
        """

        today = datetime.now()
        if today.weekday() == 0:
            # If today is Monday, subtract three days to get Friday
            last_working_day = today - timedelta(days=3)
        elif today.weekday() <= 4:
            last_working_day = today - timedelta(days=1)
        # If today is Saturday, subtract one day to get Friday
        elif today.weekday() == 5:
            last_working_day = today - timedelta(days=1)
        elif today.weekday() == 6:
            last_working_day = today - timedelta(days=2)
        
        return last_working_day.strftime('%Y-%m-%d')
    
    def fetch_dividends(self, 
                        ticker,
                        limit=10,
                        sort='ex_dividend_date',
                        order='desc',
                        sleep=True,
                        sleep_time=0.25,
                        max_retries=5,
                        ):
        
        """
        Fetches dividends for a given ticker symbol.

        Description:
        This method retrieves dividend data for a specified ticker symbol from the Polygon API.

        Parameters:
        ticker (str): The ticker symbol to fetch dividends for.
        limit (int): The maximum number of dividends to return.
        sort (str): The field to sort the dividends by.
        order (str): The order of sorting, either 'asc' or 'desc'.
        
        Returns:
        dict: A dictionary containing dividend data with ex-dividend dates as keys.
        """


        dividends = dict()
        retries = 0
        max_retries = max_retries
        backoff = 1

        while True:
            try:
                # Fetch dividends using the Polygon client
                for d in self.client.list_dividends(
                    ticker=ticker,
                    limit=limit,
                    sort=sort,
                    order=order
                ):
                    # Store dividend data in a dictionary with ex_dividend_date as the key
                    dividends[d.ex_dividend_date] = d.__dict__
                    
                    # If sleep is True, wait for a short time to avoid hitting rate limits
                    if sleep:
                        time.sleep(sleep_time)
                return dividends  # return the dividends dictionary if successful
            # Handle HTTP errors
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