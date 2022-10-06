# IMPORTATION STANDARD
import datetime

# IMPORTATION THIRD PARTY


# IMPORTATION INTERNAL
from config import console
from helpers import validate_number


class PersonalFinanceTracker:
    def __init__(self, income, currency):
        self.income = income
        self.currency = currency

    def print_options(self, text):
        console.print(text)
        now = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        command = input(f"[{str(now)}] ~ ")
        console.clear()
        return command

    def create_options_str(self, title, options):
        text = f"\n[bold][steel_blue3]{title}[/][/bold]"
        for option in options:
            text += f"\n\t> [bold][khaki3]{option[0]}[/][/]"
            text += f"\t[bold]{option[1]}[/]"
        text += f"\n\t> [bold][khaki3]quit[/][/]"
        text += f"\tQuit"
        return f"{text}\n"

    def config(self):
        while True:
            options = self.create_options_str(
                "Configuration page",
                [
                    ("inc", "Set your annualy income"),
                    ("curr", "Set your currency of preference"),
                    ("info", "Check current configurations"),
                ],
            )
            command = self.print_options(options)

            if command == "inc":
                console.print(
                    f"Annualy income currently set to [deep_sky_blue1]{self.income}[/] {self.currency}."
                )
                user_input = input("Insert your annualy income: ")
                while not validate_number(user_input):
                    console.print("\n[bold][red]Invalid value.[/][/]")
                    user_input = input("Insert your annualy income: ")
                self.income = user_input
                console.print(
                    f"Annualy income set to [deep_sky_blue1]{self.income}[/] {self.currency}."
                )

            elif command == "curr":
                console.print(f"Currency set to [deep_sky_blue1]{self.currency}[/].")
                user_input = input("Set your currency of preference (ISO 4217): ")
                while len(user_input) not in [
                    2,
                    3,
                ]:  # change to a decent validation (check if the code is valid using an API?)
                    console.print("\n[bold][red]Invalid currency code.[/][/]")
                    user_input = input("Set your currency of preference (ISO 4217): ")
                self.currency = user_input.upper()
                console.print(f"Currency set to [deep_sky_blue1]{self.currency}.[/]")
            elif command in ["info"]:
                console.print(
                    f"\n[bold][medium_orchid3]Current configurations[/][/]\n\tAnnual income: [deep_sky_blue1]{self.income}[/]\n\tCurrency: [deep_sky_blue1]{self.currency}[/]"
                )
            elif command in ["q", "quit"]:
                break

            else:
                console.print("[bold][red]Command not valid.[/][/]")

    def clear(self):
        console.clear()

    def menu(self):
        while True:
            options = self.create_options_str(
                "Personal Finance Tracker", [("cfg", "Configure your terminal")]
            )
            command = self.print_options(options)

            if command == "cfg":
                self.config()
            elif command in ["q", "quit"]:
                exit(1)
            else:
                console.print("[bold][red]Command not valid.[/][/]")

    def run(self):
        console.clear()
        self.menu()
