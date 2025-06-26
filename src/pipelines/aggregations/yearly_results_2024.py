if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import os
    from modules.os_lib import OSLib

    print("Initializing OSLib and getting repository root path...")
    oslib = OSLib()
    repo_path = oslib.get_root_path()
    print(f"Repository root path: {repo_path}")

    # Define source and sink paths for data
    source_daily_path = f"{repo_path}/data/polygon/daily/"
    source_dividends_path = f"{repo_path}/data/polygon/dividends/"
    source_idx_daily_path = f"{repo_path}/data/polygon/daily/index/"
    sink_path = f"{repo_path}/data/polygon/portfolio/portfolio_results_2024.parquet"

    print("Loading dividend data...")
    divs = pd.read_parquet(source_dividends_path)
    print(f"Dividend data loaded: {len(divs)} records.")

    # Calculate total dividend payout per ticker for 2024
    print("Calculating total dividend payout per ticker for 2024...")
    sum_divs = divs[(divs.index >= '2024-01-01') & (divs.index < '2025-01-01')][['ticker', 'cash_amount']].groupby('ticker').sum()
    sum_divs = sum_divs.rename(columns={'cash_amount': 'total_dividend_2024'})
    print(f"Total dividend payout calculated for {len(sum_divs)} tickers.")

    # Helper function to recursively get all file paths in a directory
    def get_all_file_paths(directory):
        file_paths = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                full_path = root + '/' + file 
                file_paths.append(full_path.replace('\\', '/').replace('//', '/'))  # Normalize path separators
        return file_paths

    print("Getting all daily price file paths...")
    all_files = get_all_file_paths(source_daily_path)
    print(f"Found {len(all_files)} daily price files.")

    idx_2024_df = pd.DataFrame()

    print("Getting all index daily file paths for 2024...")
    all_idx_files = get_all_file_paths(source_idx_daily_path)
    idx_2024_files = [f for f in all_idx_files if '2024' in f]
    print(f"Found {len(idx_2024_files)} index daily files for 2024.")

    # Load index data for 2024 and build a DataFrame with close prices
    print("Loading index data for 2024...")
    for dir_path in idx_2024_files:
        ticker = dir_path.split('/')[-1].split('_')[0].upper()  # Extract ticker symbol from filename
        df = pd.read_parquet(dir_path)
        df.index = pd.to_datetime(df.index).strftime('%Y-%m-%d')
        idx_2024_df[ticker] = df['close']
    print(f"Index data loaded for {len(idx_2024_df.columns)} indices.")

    # Calculate the market index as the mean of all indices
    print("Calculating market index as mean of all indices...")
    idx_2024_df['market'] = idx_2024_df.mean(axis=1)

    # DataFrame to store average price and statistics for each ticker
    avg_price_df = pd.DataFrame()

    print("Processing each ticker's daily price file for 2024...")
    processed_count = 0
    for file in all_files:
        if '2024' in file:
            ticker = file.split('/')[-1].split('_')[0].upper()
            avg_price_2024 = pd.read_parquet(file)
            avg_price_2024.index = pd.to_datetime(avg_price_2024.index).strftime('%Y-%m-%d')
            # Join with market index data
            avg_price_2024 = avg_price_2024.join(idx_2024_df, how='left', rsuffix='_idx')
            # Calculate average price, return %, variance, and covariance with market
            avg_price_df.loc[ticker.upper(), 'avg_price_2024'] = avg_price_2024['close'].mean()
            avg_price_df.loc[ticker.upper(), 'returns_2024_%'] = (avg_price_2024['close'].iloc[-1] / avg_price_2024['close'].iloc[0]) - 1
            avg_price_df.loc[ticker.upper(), 'variance_2024'] = avg_price_2024['close'].var()
            avg_price_df.loc[ticker.upper(), 'covariance_2024'] = avg_price_2024['close'].cov(avg_price_2024['market']) 

    # join the dfs on the index
    agg_12mnd_df = avg_price_df.join(sum_divs, how='left')

    # Calculate the dividend yield for each ticker
    agg_12mnd_df['dividend_yield_%_2024'] = (agg_12mnd_df['total_dividend_2024'] / agg_12mnd_df['avg_price_2024']) * 100

    risk_free_rate = 0.04
    # Calculate the beta, capm and sharpe ratio for each ticker
    agg_12mnd_df['beta_2024'] = agg_12mnd_df['covariance_2024'] / ((agg_12mnd_df.loc['COMP', 'variance_2024'] + agg_12mnd_df.loc['NDX', 'variance_2024']) / 2) # type: ignore
    agg_12mnd_df["capm_2024"] = risk_free_rate + agg_12mnd_df['beta_2024'] * (np.mean([agg_12mnd_df.loc['COMP', 'returns_2024_%'], agg_12mnd_df.loc['NDX', 'returns_2024_%']]) - risk_free_rate) # type: ignore
    agg_12mnd_df["sharpe_2024"] = (agg_12mnd_df["returns_2024_%"] - risk_free_rate) / np.sqrt(agg_12mnd_df['variance_2024'])


    # Save the results to a parquet file
    print(f"Saving results to {sink_path}...")
    avg_price_df.to_parquet(sink_path)
    print("Results saved.")