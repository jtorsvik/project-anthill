"""DAG that ingests the current year's market holiday/close dates from Polygon.io."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

from common import DEFAULT_ARGS, START_DATE, script_command

with DAG(
    dag_id="polygon_market_holiday_dates",
    description="Fetch the current year's market holiday/close dates from Polygon.io",
    default_args=DEFAULT_ARGS,
    start_date=START_DATE,
    # Once a year, early January, so the new year's calendar is available.
    schedule="0 6 2 1 *",
    catchup=False,
    max_active_runs=1,
    tags=["polygon", "ingestion", "reference-data"],
) as dag:
    BashOperator(
        task_id="fetch_market_holiday_dates",
        bash_command=script_command(
            "src/pipelines/data_processing/write_market_holiday_dates.py"
        ),
    )
