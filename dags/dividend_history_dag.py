"""DAG that ingests/upserts dividend history for a fixed ticker list from Polygon.io."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

from common import DEFAULT_ARGS, START_DATE, script_command

with DAG(
    dag_id="polygon_dividend_history",
    description="Fetch and upsert dividend history for tracked tickers from Polygon.io",
    default_args=DEFAULT_ARGS,
    start_date=START_DATE,
    # Weekly, Monday morning.
    schedule="0 6 * * 1",
    catchup=False,
    max_active_runs=1,
    tags=["polygon", "ingestion", "dividends"],
) as dag:
    BashOperator(
        task_id="fetch_dividend_history",
        bash_command=script_command(
            "src/pipelines/data_processing/write_dividend_history_to_parquet.py"
        ),
    )
