"""Shared configuration used by all Project Anthill Airflow DAGs."""

from __future__ import annotations

from datetime import timedelta

import pendulum

# Absolute path to the project checkout on the machine running the scheduler/workers.
PROJECT_ROOT = "/Users/jm.torsvik/Documents/repos/project-anthill"

# Use the project's own uv-managed venv so pipeline dependencies match `uv run`.
PYTHON_BIN = f"{PROJECT_ROOT}/.venv/bin/python"

DEFAULT_ARGS = {
    "owner": "jtorsvik",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "depends_on_past": False,
}

# Fixed start date so `catchup=False` DAGs only trigger from their next schedule tick.
START_DATE = pendulum.datetime(2025, 1, 1, tz="UTC")


def script_command(relative_script_path: str) -> str:
    """Build the bash command that runs a pipeline script from the project root."""
    return f"cd {PROJECT_ROOT} && {PYTHON_BIN} {relative_script_path}"
