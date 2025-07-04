if __name__ == "__main__":
    # Import necessary libraries
    import os
    from datetime import datetime

    import pandas as pd
    from dotenv import load_dotenv

    from modules.os_lib import OSLib  # Custom module for OS-related utilities
    from modules.polygon_api import (
        PolygonAPI,  # Custom module for Polygon API interaction
    )

    # Load API key from environment variable
    load_dotenv()  # Load environment variables from a .env file
    api_key = os.getenv("POLYGON_API_KEY")  # Retrieve the Polygon API key

    # Initialize Polygon API client
    client = PolygonAPI(api_key)

    # Fetch market holiday dates from the API
    market_holidays = client.fetch_market_holiday_dates()
    # Convert the fetched data to a pandas DataFrame
    market_holidays = pd.DataFrame(
        market_holidays, columns=["Date", "Exchange", "Occasion"]
    )

    # Utilize oslib and get repo path
    oslib = OSLib()  # Initialize OS utility class
    repo_path = oslib.get_root_path()  # Get the root path of the repository

    # Construct the output file path for the parquet file
    file_path = f"{repo_path}/data/polygon/market_close_dates/market_holidays_{datetime.now().year}.parquet"
    print("Fetch complete, writing file to: ", file_path)

    # Write the market holidays DataFrame to a parquet file
    market_holidays.to_parquet(file_path)
