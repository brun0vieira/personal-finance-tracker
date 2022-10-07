# IMPORTATION STANDARD
import datetime
import os

# IMPORTATION THIRD PARTY
from rich.console import Console

# IMPORTATION INTERNAL
from personal_finance_tracker import PersonalFinanceTracker

user_config_file = ""

if __name__ == "__main__":

    pft = PersonalFinanceTracker(
        user_config="pftUserData/config_example.json",
        user_data="pftUserData/data_example.json"
    )
    pft.run()
