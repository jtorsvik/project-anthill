"""
This script fetches intraday stock data for IBM from
the Alpha Vantage API and saves it as a Parquet file.
"""

# Import necessary libraries
import json

import pandas as pd
import requests

print("Ingesting data from Alpha Vantage API")
# Fetch data from Alpha Vantage API
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
r = requests.get(url)
data = r.json()

# Convert the JSON data to a Pandas DataFrame
ibm = pd.DataFrame(data["Time Series (5min)"]).T

# Get the current date from the intraday data
ingest_date = pd.to_datetime(data["Meta Data"]["3. Last Refreshed"]).strftime(
    "%Y_%m_%d"
)

# Create a directory path to save the Parquet file
sink_dir_path = "~/git_repos/project-anthill/data/"
filename = f"ibm_{ingest_date}.parquet"
save_path = sink_dir_path + filename
print(f"Writing to {save_path}")

# Write the DataFrame to a Parquet file
ibm.to_parquet(save_path, index=True)

print("Data ingestion complete!")
