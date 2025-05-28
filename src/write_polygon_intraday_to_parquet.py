# If the script is run directly, execute the following code block
if __name__ == '__main__':

    # Import necessary libraries
    import pandas as pd
    import os, sys
    from polygon import RESTClient

    # Import custom PolygonAPI class
    sys.path.append(os.path.abspath(os.path.join('..', 'scripts')))
    from polygon_api import PolygonAPI

    # All tickers to fetch data for
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'IBM', 'AMZN', 'NVDA',
            'XOM', 'CVX', 'WMT', 'MMM', 'ARE', 'ALLE', 'JPM',
            'V', 'MA', 'PEP', 'CSCO', 'BA', 'ADBE', 'CAT', 
            'BLK', 'INTC', 'NKE', 'MDLZ']

    # Initialize the PolygonAPI client
    client = RESTClient(api_key='rxdopHP51cQc3RtUbZrNj7Gy0CkpR2Qn')
    client = PolygonAPI()

    # Get the last working day
    intra_day = client.last_working_day()
    intra_day = "2025-05-26"

    # Fetch intraday data for each ticker and save to parquet files
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