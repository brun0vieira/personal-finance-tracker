from pathlib import Path

REPOSITORY_DIRECTORY = Path(__file__).parent.parent

USER_DATA_DIRECTORY = REPOSITORY_DIRECTORY / "pftUserData"

DEFAULT_DATA_FILE = USER_DATA_DIRECTORY / "my_data.json"

DEFAULT_CONFIG_FILE = USER_DATA_DIRECTORY / "my_config.json"