"""DAG that ingests daily OHLC aggregates for portfolio stocks and indices from Polygon.io."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

from common import DEFAULT_ARGS, START_DATE, script_command

with DAG(
    dag_id="polygon_daily_prices",
    description="Fetch daily OHLC aggregates for portfolio stocks and indices from Polygon.io",
    default_args=DEFAULT_ARGS,
    start_date=START_DATE,
    # Weekdays, after the US market close.
    schedule="0 22 * * 1-5",
    catchup=False,
    max_active_runs=1,
    tags=["polygon", "ingestion", "daily"],
) as dag:
    BashOperator(
        task_id="fetch_daily_prices",
        bash_command=script_command(
            "src/pipelines/data_processing/write_polygon_daily_to_parquet.py"
        ),
    )
