# IMPORTATION STANDARD
import datetime
from email.policy import default

# IMPORTATION THIRD PARTY
from rich.prompt import FloatPrompt


# IMPORTATION INTERNAL
from config import console
from helpers import validate_number
from constants import (
    DEFAULT_ANNUAL_INCOME,
    DEFAULT_CURRENCY,
    DEFAULT_CURRENCY_LIST,
)


class PersonalFinanceTracker:
    def __init__(
        self, income: float = DEFAULT_ANNUAL_INCOME, currency: str = DEFAULT_CURRENCY
    ):
        self.income = income
        self.currency = currency

    def print_options(self, text):
        console.print(text)
        now = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        command = input(f"[{str(now)}] ~ ")
        return command

    def create_options_str(self, title, options):
        text = f"\n[bold][steel_blue3]{title}[/][/bold]"
        for option in options:
            text += f"\n\t> [bold][khaki3]{option[0]}[/][/]"
            text += f"\t[bold]{option[1]}[/]"
        text += f"\n\t> [bold][khaki3]quit[/][/]"
        text += f"\tQuit"
        return f"{text}\n"

    def display_current_config(self):
        console.clear()
        console.print(f"\n[bold][medium_orchid3]Current configurations[/][/]\n")
        console.print(
            f"\t[bold][deep_sky_blue1]Annual income[/]: {self.income} {self.currency}"
        )
        console.print(f"\t[bold][deep_sky_blue1]Currency[/]: {self.currency}")

    def config(self):
        while True:
            self.display_current_config()

            options = self.create_options_str(
                "\nConfiguration page\n",
                [
                    ("inc", "Set your annualy income"),
                    ("curr", "Set your currency of preference"),
                ],
            )
            command = self.print_options(options)

            match command:
                case "inc":
                    user_input = FloatPrompt.ask("Insert your annual income")
                    self.set_annual_income(user_input)
                case "curr":
                    user_input = input("Insert your currency of preference: ").upper()
                    self.set_currency(user_input)
                case "q" | "quit":
                    break
                case _:
                    console.print("[bold][red]Command not valid.[/][/]")

    def set_annual_income(self, income: float):
        if not validate_number(income):
            console.print("\n[bold][red]Invalid value.[/][/]")
            return

        self.income = income
        console.print(
            f"Annual income set to [deep_sky_blue1]{self.income}[/] {self.currency}."
        )

    def set_currency(self, currency: str):
        if currency not in DEFAULT_CURRENCY_LIST:
            console.print("\n[bold][red]Invalid currency code.[/][/]")
            return

        self.currency = currency
        console.print(f"Currency set to [deep_sky_blue1]{self.currency}.[/]")

    def menu(self):
        while True:
            console.clear()
            options = self.create_options_str(
                "\nPersonal Finance Tracker\n", [("cfg", "Configure your terminal")]
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
