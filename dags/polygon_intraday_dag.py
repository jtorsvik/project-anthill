"""DAG that ingests intraday minute aggregates for portfolio stocks from Polygon.io."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

from common import DEFAULT_ARGS, START_DATE, script_command

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
    BashOperator(
        task_id="fetch_intraday_prices",
        bash_command=script_command(
            "src/pipelines/data_processing/write_polygon_intraday_to_parquet.py"
        ),
    )
