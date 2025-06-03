if __name__ == '__main__':

   # Import necessary libraries
    import pandas as pd
    import os
    from dotenv import load_dotenv

    # Import custom PolygonAPI class
    from polygon_api import PolygonAPI
    from os_lib import OSLib

    load_dotenv()
    api_key = os.getenv('POLYGON_API_KEY')

    # All tickers to fetch data for
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'IBM', 'AMZN', 'NVDA',
            'XOM', 'CVX', 'WMT', 'MMM', 'ARE', 'ALLE', 'JPM',
            'V', 'MA', 'PEP', 'CSCO', 'BA', 'ADBE', 'CAT', 
            'BLK', 'INTC', 'NKE', 'MDLZ']
    
    client = PolygonAPI(api_key=api_key)

    project_root_path = OSLib.get_root_path()

    for i, ticker in enumerate(tickers):

        sink_path = f"{project_root_path}/data/polygon/dividends/{ticker.lower()}/{ticker.lower()}_dividend_history.parquet"
        
        if os.path.exists(sink_path):
            print(f"File {sink_path} already exists, skipping download for {ticker}.")
            continue

        print(f"Fetching dividend history for {ticker} ({i+1}/{len(tickers)})...")
        dividends = client.fetch_dividends(ticker=ticker,
                                            sleep_time=0.5)
        df = pd.DataFrame(dividends).T
        df.drop(columns=['ticker'], inplace=True)
        df.index = pd.to_datetime(df.index)

        # Upsert the DataFrame to existing data if it exists
        if os.path.exists(sink_path):
            print(f"File {sink_path} already exists, appending new data for {ticker}.")
            existing_df = pd.read_parquet(sink_path)
            df = pd.concat([existing_df, df]).drop_duplicates(keep='last')

        df.to_parquet(sink_path, index=True)
        print(f"Wrote dividend history for {ticker}.")