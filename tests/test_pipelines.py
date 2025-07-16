import os
import tempfile
import pandas as pd
import pytest
from src.pipelines.data_processing import write_polygon_intraday_to_parquet


@pytest.fixture
def sample_dataframe():
    return pd.DataFrame(
        {
            "timestamp": ["2024-01-01 09:30:00", "2024-01-01 09:31:00"],
            "open": [100.0, 101.0],
            "close": [101.0, 102.0],
            "volume": [1000, 1500],
        }
    )


def test_write_polygon_intraday_to_parquet_creates_file(sample_dataframe):
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "test.parquet")
        write_polygon_intraday_to_parquet.write_to_parquet(
            sample_dataframe, output_path
        )
        assert os.path.exists(output_path)
        df_read = pd.read_parquet(output_path)
        pd.testing.assert_frame_equal(df_read, sample_dataframe)


def test_write_polygon_intraday_to_parquet_overwrites_file(sample_dataframe):
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "test.parquet")
        # Write initial file
        write_polygon_intraday_to_parquet.write_to_parquet(
            sample_dataframe, output_path
        )
        # Overwrite with new data
        new_df = sample_dataframe.copy()
        new_df["open"] = [200.0, 201.0]
        write_polygon_intraday_to_parquet.write_to_parquet(new_df, output_path)
        df_read = pd.read_parquet(output_path)
        pd.testing.assert_frame_equal(df_read, new_df)


def test_write_polygon_intraday_to_parquet_empty_dataframe():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "test.parquet")
        empty_df = pd.DataFrame()
        write_polygon_intraday_to_parquet.write_to_parquet(empty_df, output_path)
        df_read = pd.read_parquet(output_path)
        pd.testing.assert_frame_equal(df_read, empty_df)
