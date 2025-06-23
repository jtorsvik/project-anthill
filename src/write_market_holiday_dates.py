if __name__ == "__main__":

    # Import necessary libraries
    import os
    from dotenv import load_dotenv

    from polygon_api import PolygonAPI
    from os_lib import OSLib

    # Load API key from environment variable
    load_dotenv()
    api_key = os.getenv('POLYGON_API_KEY')
    if not api_key:
        raise ValueError("Polygon API key not found in environment variables.")

    client = PolygonAPI(api_key)

    market_holidays = client.fetch_market_holiday_dates()
    
    
    oslib = OSLib
    repo_path = oslib.get_root_path()
    file_path = os.path.join(repo_path, 'data/polygon/market_close_dates', 'market_holidays.csv')

    # Write the market holidays to a parquet file
    market_holidays.to_parquet(file_path, index=False)
