if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join('..', 'src')))
    from os_lib import OSLib
    # Import custom lib
    oslib = OSLib

    # Get the root path of the repository
    repo_path = oslib.get_root_path()

    def get_all_tickers_with_dirpaths(root_directory):

        all_files = []

        for ticker in os.listdir(root_directory):
            if ticker == 'index':
                idx_dir_path = root_directory + '/index'
                for idx in os.listdir(idx_dir_path):
                    ix_dir_path = f"{idx_dir_path}/{idx}"
                    all_files.append(('i_' + idx, ix_dir_path))
            else:
                ticker_dir_path = f"{root_directory}/{ticker}"
                all_files.append((ticker, ticker_dir_path))

        return all_files

    all_file_paths = get_all_tickers_with_dirpaths(repo_path + '/data/polygon/daily')

    combined_df = pd.DataFrame()

    for tick, dir_path in all_file_paths:
        tick_df = pd.read_parquet(dir_path)
        combined_df[tick + '_close'] = tick_df['close']
        combined_df[tick + '_1d_rtns'] = (tick_df['close'] / tick_df['close'].shift(1)) - 1
        combined_df[tick + '_rtns_from_2023'] = (tick_df['close']/tick_df['close'].iloc[0]) * 100

    combined_df['market_mean_close'] = np.mean([combined_df['i_comp_close'], combined_df['i_ndx_close']])
    combined_df['market_1d_rtns'] = (combined_df['market_mean_close'] / combined_df['market_mean_close'].shift(1)) - 1
    combined_df['market_rtns_from_2023'] = combined_df['market_mean_close']/combined_df['market_mean_close'].iloc[0] * 100
    
    sink_path = f"{repo_path}/data/polygon/portfolio/portfolio_returns.parquet"

    combined_df.to_parquet(sink_path)