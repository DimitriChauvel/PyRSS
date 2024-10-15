"""Env"""

from os import environ


def load_env(file_path: str) -> None:
    """Load environment variables from .env file"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    environ[key] = value.replace('"', "")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{file_path}'.")
