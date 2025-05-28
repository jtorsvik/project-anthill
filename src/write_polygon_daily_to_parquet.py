if __name__ == '__main__':

    # Import necessary libraries
    import pandas as pd
    import os, sys
    from polygon import RESTClient
    from dotenv import load_dotenv

    # Import custom PolygonAPI class
    from polygon_api import PolygonAPI

    load_dotenv()
    api_key = os.getenv('POLYGON_API_KEY')

    # All tickers to fetch data for
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'IBM', 'AMZN', 'NVDA',
            'XOM', 'CVX', 'WMT', 'MMM', 'ARE', 'ALLE', 'JPM',
            'V', 'MA', 'PEP', 'CSCO', 'BA', 'ADBE', 'CAT', 
            'BLK', 'INTC', 'NKE', 'MDLZ']

    # Initialize the Polygon API client
    client = RESTClient(api_key=api_key)
    client = PolygonAPI()

    to_date = client.last_working_day()
    from_date = f"{to_date[:4]}-01-01"

    for i, ticker in enumerate(tickers):
        # The sink path for the write operation
        sink_root_path = f'C:/Users/jmtorsvik/git_repos/project-anthill/data/polygon/daily/{ticker.lower()}/{ticker.lower()}_daily_{from_date[:4]}.parquet'
        
        # Check if the file already exists
        # if os.path.exists(sink_root_path):
        #     print(f"File already exists: {sink_root_path}. Skipping...\n")
        #     continue # Skip if the file already exists

        # Fetch intraday data for the ticker
        print(f"{i+1}/{len(tickers)} - Fetching data for: {ticker}, from {from_date} to {to_date}")
        intra_day_ticker = client.fetch_aggs_with_backoff(
            ticker=ticker,
            timespan='day',
            from_date=from_date, 
            to_date=to_date,
            limit=50000,
            sleep=True
            )

        print("Structuring data into a Pandas DataFrame...")
        df = pd.DataFrame(intra_day_ticker).T
        df.index = pd.to_datetime(df.index, utc=True).strftime('%Y-%m-%d')

        print("Saving intraday to parquet file...")
        df.to_parquet(sink_root_path, index=True)
        print(f"Data for {ticker} written to {sink_root_path}")
        print("----------------------------")