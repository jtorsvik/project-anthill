import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests, json, os, sys

from datetime import datetime, timedelta, timezone

from polygon import RESTClient

sys.path.append(os.path.abspath(os.path.join('..', 'scripts')))

from polygon_api import PolygonAPI

client = RESTClient(api_key='rxdopHP51cQc3RtUbZrNj7Gy0CkpR2Qn')

from datetime import datetime, timedelta


tickers = ['AAPL', 'MSFT', 'GOOGL', 'IBM', 'AMZN', 'NVDA',
          'XOM', 'CVX', 'WMT', 'MMM', 'ARE', 'ALLE', 'JPM',
          'V', 'MA', 'PEP', 'CSCO', 'BA', 'ADBE', 'CAT', 
          'BLK', 'INTC', 'NKE', 'MDLZ']

client = PolygonAPI()

intra_day = client.last_working_day()

for ticker in tickers:

    print(f"Fetching data for: {ticker}, on {intra_day}")
    intra_day_ticker = client.fetch_aggs_with_backoff(
        ticker=ticker, 
        from_date=intra_day, 
        to_date=intra_day, 
        limit=50000,
        sleep=True
        )

    print("Structuring data into a Pandas DataFrame...")
    df = pd.DataFrame(intra_day_ticker).T

    print("Saving intraday to parquet file...")
    sink_root_path = f'C:/Users/jmtorsvik/git_repos/project-anthill/data/polygon/intraday/{ticker.lower()}/{ticker.lower()}_intraday_{intra_day.replace('-', '_')}.parquet'
    df.to_parquet(sink_root_path, index=True)
    print(f"Data for {ticker} written to {sink_root_path}\n")

    print("----------------------------\n")