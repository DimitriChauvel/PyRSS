"""Run scripts"""

import subprocess


def lint_fix() -> None:
    """Run linter"""
    subprocess.run(["black", "."], check=False)


def lint() -> None:
    """Run pylint"""
    subprocess.run(["pylint", "."], check=False)


def tests() -> None:
    """Run tests"""
    subprocess.run(["pytest", "."], check=False)
