if __name__ == "__main__":

    # Import necessary libraries
    import os
    import pandas as pd
    from datetime import datetime
    from dotenv import load_dotenv

    from modules.polygon_api import PolygonAPI  # Custom module for Polygon API interaction
    from modules.os_lib import OSLib           # Custom module for OS-related utilities

    # Load API key from environment variable
    load_dotenv()  # Load environment variables from a .env file
    api_key = os.getenv('POLYGON_API_KEY')  # Retrieve the Polygon API key
    if not api_key:
        raise ValueError("Polygon API key not found in environment variables.")

    # Initialize Polygon API client
    client = PolygonAPI(api_key)

    # Fetch market holiday dates from the API
    market_holidays = client.fetch_market_holiday_dates()
    # Convert the fetched data to a pandas DataFrame
    market_holidays = pd.DataFrame(market_holidays, columns=['Date', 'Exchange', 'Occasion'])

    print("Utilize oslib and get repo path")    
    oslib = OSLib()  # Initialize OS utility class
    repo_path = oslib.get_root_path()  # Get the root path of the repository

    # Construct the output file path for the parquet file
    file_path = f'{repo_path}/data/polygon/market_close_dates/market_holidays_{datetime.now().year}.parquet'
    print(file_path)

    # Write the market holidays DataFrame to a parquet file
    market_holidays.to_parquet(file_path)
