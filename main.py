# IMPORTATION STANDARD
import datetime
import os

# IMPORTATION THIRD PARTY
from rich.console import Console

# IMPORTATION INTERNAL
from personal_finance_tracker import PersonalFinanceTracker
from config.paths import DEFAULT_CONFIG_FILE, DEFAULT_DATA_FILE

user_config_file = ""

if __name__ == "__main__":

    pft = PersonalFinanceTracker(
        user_config_dir=DEFAULT_CONFIG_FILE,
        user_data_dir=DEFAULT_DATA_FILE,
    )
    pft.run()
