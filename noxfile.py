"""Nox sessions for testing and linting the project."""

import nox  # type: ignore


@nox.session  # type: ignore
def tests(session: nox.Session) -> None:
    """Run tests using pytest.

    This session installs pytest and runs it against the codebase to ensure that all tests pass.

    Usage:
        nox -s tests

    Requirements:
        - Python 3.8 or higher
        - Nox installed in your Python environment
        - pytest installed as a dependency in the session
    """
    session.install("pytest")
    session.run("pytest")


@nox.session  # type: ignore
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
