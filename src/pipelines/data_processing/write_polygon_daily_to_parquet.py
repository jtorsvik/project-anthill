if __name__ == "__main__":
    # Import necessary libraries
    import json
    import os

    import pandas as pd
    from dotenv import load_dotenv

    # Import custom PolygonAPI class
    from modules import os_lib, polygon_api

    # from polygon import RESTClient
    load_dotenv()
    api_key = os.getenv("POLYGON_API_KEY")

    oslib = os_lib.OSLib()
    project_root_path = oslib.get_root_path()

    # All tickers to fetch data for
    stock_tick_path = f"{project_root_path}/data/polygon/portfolio/stock_tickers.json"
    idx_tick_path = f"{project_root_path}/data/polygon/portfolio/idx_tickers.json"
    with open(stock_tick_path) as s:
        stock_ticks = json.load(s)
    
    with open(idx_tick_path) as i:
        idx_ticks = json.load(i)
    
    tickers = stock_ticks + idx_ticks

    # Initialize the Polygon API client
    client = polygon_api.PolygonAPI(api_key=api_key)

    to_date = client.last_working_day()
    # to_date = "2022-12-31"
    from_date = f"{to_date[:4]}-01-01"



    for i, ticker in enumerate(tickers):
        # The sink path for the write operation
        if ticker.startswith("I:"):
            index = ticker.split(":")[1]
            sink_root_path = f"{project_root_path}/data/polygon/daily/index/{index.lower()}/{index.lower()}_daily_{from_date[:4]}.parquet"
        else:
            sink_root_path = f"{project_root_path}/data/polygon/daily/{ticker.lower()}/{ticker.lower()}_daily_{from_date[:4]}.parquet"

        # # Check if the file already exists
        # if os.path.exists(sink_root_path):
        #     print(f"File already exists: {sink_root_path}. Skipping...\n")
        #     continue # Skip if the file already exists

        # Check if the directory has been modified on in the same day
        if (
            os.path.exists(sink_root_path)
            and os.path.getmtime(sink_root_path)
            > pd.Timestamp.now(tz="UTC").normalize().timestamp()
        ):
            print(
                f"File already exists and is up-to-date: {sink_root_path}. Skipping...\n"
            )
            continue

        # Fetch intraday data for the ticker
        print(
            f"{i + 1}/{len(tickers)} - Fetching data for: {ticker}, from {from_date} to {to_date}"
        )
        intra_day_ticker = client.fetch_aggs_with_backoff(
            ticker=ticker,
            timespan="day",
            from_date=from_date,
            to_date=to_date,
            limit=50000,
            sleep=True,
        )

        print("Structuring data into a Pandas DataFrame...")
        df = pd.DataFrame(intra_day_ticker).T
        df.index = pd.to_datetime(df.index, utc=True)
        df.index.astype("datetime64[ns, UTC]")
        df.index.name = "date"

        print("Saving to parquet file...")
        df.to_parquet(sink_root_path, index=True)
        print(f"Data for {ticker} written to {sink_root_path}")
        print("----------------------------")
