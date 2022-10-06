# IMPORTATION STANDARD
import datetime

# IMPORTATION THIRD PARTY
from rich.console import Console

# IMPORTATION INTERNAL
from personal_finance_tracker import PersonalFinanceTracker

if __name__ == "__main__":

    default_income = 21700
    default_currency = "EUR"

    pft = PersonalFinanceTracker(default_income, default_currency)
    pft.run()
