# IMPORTATION STANDARD
import datetime

# IMPORTATION THIRD PARTY
from rich.console import Console

# IMPORTATION INTERNAL
from personal_finance_tracker import PersonalFinanceTracker

if __name__ == "__main__":

    pft = PersonalFinanceTracker()
    pft.run()