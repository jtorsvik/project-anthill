"""DAG that ingests intraday minute aggregates for portfolio stocks from Polygon.io."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

from common import DEFAULT_ARGS, START_DATE, load_stock_tickers, script_command

with DAG(
    dag_id="polygon_intraday_prices",
    description="Fetch intraday minute aggregates for portfolio stocks from Polygon.io",
    default_args=DEFAULT_ARGS,
    start_date=START_DATE,
    # Weekdays, shortly after the US market close.
    schedule="30 21 * * 1-5",
    catchup=False,
    max_active_runs=1,
    tags=["polygon", "ingestion", "intraday"],
) as dag:
    # One mapped task instance per ticker, so tickers fetch in parallel (subject to executor parallelism).
    BashOperator.partial(
        task_id="fetch_intraday_prices",
    ).expand(
        bash_command=[
            script_command(
                f"src/pipelines/data_processing/write_polygon_intraday_to_parquet.py --ticker {ticker}"
            )
            for ticker in load_stock_tickers()
        ]
    )
