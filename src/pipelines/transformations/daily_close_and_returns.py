if __name__ == "__main__":
    import os

    import numpy as np
    import pandas as pd

    from modules.os_lib import OSLib

    # Import custom lib
    oslib = OSLib()

    # Get the root path of the repository
    repo_path = oslib.get_root_path()
    print(f"Repository path: {repo_path}")

    def get_all_tickers_with_dirpaths(root_directory):
        all_files = []
        for ticker in os.listdir(root_directory):
            if ticker == "index":
                idx_dir_path = root_directory + "/index"
                for idx in os.listdir(idx_dir_path):
                    ix_dir_path = f"{idx_dir_path}/{idx}"
                    all_files.append(("i_" + idx, ix_dir_path))
            else:
                ticker_dir_path = f"{root_directory}/{ticker}"
                all_files.append((ticker, ticker_dir_path))
        return all_files

    all_file_paths = get_all_tickers_with_dirpaths(f"{repo_path}/data/polygon/daily")
    print(f"Found {len(all_file_paths)} tickers/directories.")

    combined_df = pd.DataFrame()

    print(
        "Ingesting all daily stocks and creating a DataFrame with daily close and returns..."
    )
    for tick, dir_path in all_file_paths:
        tick_df = pd.read_parquet(dir_path)
        combined_df[tick + "_close"] = tick_df["close"]
        combined_df[tick + "_1d_rtns"] = (
            tick_df["close"] / tick_df["close"].shift(1)
        ) - 1
        combined_df[tick + "_rtns_from_2023"] = (
            tick_df["close"] / tick_df["close"].iloc[0]
        ) * 100

    print("Calculating market mean and returns...")
    combined_df["market_mean_close"] = np.mean(
        [combined_df["i_comp_close"], combined_df["i_ndx_close"]]
    )
    combined_df["market_1d_rtns"] = (
        combined_df["market_mean_close"] / combined_df["market_mean_close"].shift(1)
    ) - 1
    combined_df["market_rtns_from_2023"] = (
        combined_df["market_mean_close"]
        / combined_df["market_mean_close"].iloc[0]
        * 100
    )

    sink_path = f"{repo_path}/data/polygon/portfolio/portfolio_returns.parquet"
    print(f"Saving combined DataFrame to {sink_path}")

    combined_df.to_parquet(sink_path)
    print("Done.")
