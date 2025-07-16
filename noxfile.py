"""Nox sessions for testing and linting the project."""

import nox  # type: ignore
import sys
import glob
import os

from pathlib import Path
from textwrap import dedent

nox.options.default_venv_backend = "uv"  # Use uv for virtual environments
nox.options.reuse_existing_virtualenvs = True  # Reuse existing virtual environments
nox.options.sessions = ["tests", "lint", "build"]  # Default sessions to run
locations = "srcsrc/pipelines/data_processing/src/modules/"  # Directories to check


@nox.session(
    python=[
        "3.12",
        "3.13",
    ]  # Specify the Python versions to test against
)
def tests(session: nox.Session) -> None:
    """Run tests using pytest.

    This session installs pytest and runs it against the codebase to ensure that all tests pass.

    Usage:
        nox -s tests

    Requirements:
        - Python 3.12 or higher
        - Nox installed in your Python environment
        - pytest installed as a dependency in the session
    """
    session.install(".[tests]")
    session.run(
        "pytest",
        "--cov",
        "--cov-config=pyproject.toml",
        "session.posargs",
        env={"COVERAGE_FILE": f".coverage.{session.python}"},
    )


@nox.session(
    python=[
        "3.12",
        "3.13",
    ]  # Specify the Python versions to test against
)
def build(session: nox.Session) -> None:
    """Build the project using setuptools.

    This session installs the project in editable mode and builds the distribution packages.

    Usage:
        nox -s build

    Requirements:
        - Python 3.12 or higher
        - Nox installed in your Python environment
        - setuptools installed as a dependency in the session
    """
    session.install("build", "twine", "uv")
    session.run("python", "-m", "build", "--installer", "uv")
    dists = glob.glob("dist/*")
    session.run("twine", "check", *dists)


@nox.session(
    python=["3.12", "3.13"],  # Specify the Python versions to test against
)
def lint(session: nox.Session) -> None:
    """Lint the codebase using Flake8.

    This session installs Flake8 and runs it against the codebase to check for style violations.

    Usage:
        nox -s lint

    Requirements:
        - Python 3.8 or higher
        - Nox installed in your Python environment
        - Flake8 installed as a dependency in the session
    """
    session.install("flake8")
    session.run("flake8")
