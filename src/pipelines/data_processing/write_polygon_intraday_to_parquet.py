"""Script to fetch intraday stock data for a single ticker from the Polygon API and save it as a parquet file.

Takes the ticker as a CLI argument so it can be invoked once per ticker (e.g. by an
Airflow dynamically-mapped task), allowing tickers to be fetched in parallel.
"""

import argparse
import os

import pandas as pd  # type: ignore


def write_to_parquet(df: pd.DataFrame, output_path: str) -> None:
    """Write a DataFrame to a Parquet file, creating parent directories if needed."""
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    df.to_parquet(output_path, index=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch intraday aggregates for a single ticker from Polygon.io"
    )
    parser.add_argument(
        "--ticker", required=True, help="Ticker symbol to fetch intraday data for"
    )
    return parser.parse_args()


# If the script is run directly, execute the following code block
if __name__ == "__main__":
    from dotenv import load_dotenv  # type: ignore

    from modules.os_lib import OSLib
    from modules.polygon_api import PolygonAPI

    args = parse_args()
    ticker = args.ticker

    load_dotenv()
    api_key = os.getenv("POLYGON_API_KEY")

    oslib = OSLib()
    project_root_path = oslib.get_root_path()

    # Initialize the PolygonAPI client
    client = PolygonAPI(api_key=api_key)

    # Get the last working day
    intra_day = client.last_working_day()
    # intra_day = "2025-07-07"

    sink_root_path = f"{project_root_path}/data/polygon/intraday/{ticker.lower()}/{ticker.lower()}_intraday_{intra_day.replace('-', '_')}.parquet"

    if os.path.exists(sink_root_path):
        print(f"File already exists: {sink_root_path}. Skipping...\n")
    else:
        print(f"Fetching data for: {ticker}, on {intra_day}")
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
        write_to_parquet(df, sink_root_path)
        print(f"Data for {ticker} written to {sink_root_path}\n")
