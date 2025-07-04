# If the script is run directly, execute the following code block
if __name__ == "__main__":
    import json
    import os

    import pandas as pd
    from dotenv import load_dotenv

    from modules.os_lib import OSLib
    from modules.polygon_api import PolygonAPI

    load_dotenv()
    api_key = os.getenv("POLYGON_API_KEY")

    oslib = OSLib()
    project_root_path = oslib.get_root_path()

   # All tickers to fetch data for
    stock_tick_path = f"{project_root_path}/data/polygon/portfolio/stock_tickers.json"
    with open(stock_tick_path) as s:
        tickers = json.load(s)

    # Initialize the PolygonAPI client
    client = PolygonAPI(api_key=api_key)

    # Get the last working day
    intra_day = client.last_working_day()
    # intra_day = "2025-07-02"

    # Fetch intraday data for each ticker and save to parquet files
    for i, ticker in enumerate(tickers):
        sink_root_path = f"{project_root_path}/data/polygon/intraday/{ticker.lower()}/{ticker.lower()}_intraday_{intra_day.replace('-', '_')}.parquet"

        if os.path.exists(sink_root_path):
            print(f"File already exists: {sink_root_path}. Skipping...\n")
            continue  # Skip if the file already exists

        print(f"{i + 1}/{len(tickers)} Fetching data for: {ticker}, on {intra_day}")
        intra_day_ticker = client.fetch_aggs_with_backoff(
            ticker=ticker,
            from_date=intra_day,
            to_date=intra_day,
            limit=50000,
            sleep=True,
        )

        print("Structuring data into a Pandas DataFrame...")
        df = pd.DataFrame(intra_day_ticker).T

        print("Saving intraday to parquet file...")
        df.to_parquet(sink_root_path, index=True)
        print(f"Data for {ticker} written to {sink_root_path}\n")

        print("----------------------------\n")
