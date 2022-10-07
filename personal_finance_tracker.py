# IMPORTATION STANDARD
from email.policy import default

# IMPORTATION THIRD PARTY
from rich.prompt import FloatPrompt, Prompt

# IMPORTATION INTERNAL
from config import console
from helpers import print_options, create_options_str
from constants import (
    DEFAULT_ANNUAL_INCOME,
    DEFAULT_CURRENCY,
    DEFAULT_CURRENCY_LIST,
)


class PersonalFinanceTracker:
    def __init__(
        self,
        income: float = DEFAULT_ANNUAL_INCOME,
        currency: str = DEFAULT_CURRENCY,
        info_msg: str = None,
    ):
        self.income = income
        self.currency = currency
        self.info_msg = None

    def clear_console(self):
        console.clear()
        if self.info_msg:
            console.print(self.info_msg)
            self.info_msg = None

    def show_options(self, options) -> str:
        options_str = create_options_str(options[0], options[1])
        return print_options(options_str)

    def display_current_config(self):
        self.clear_console()
        console.print(f"\n[bold][medium_orchid3]Current configurations[/][/]\n")
        console.print(
            f"\t[bold][deep_sky_blue1]Annual income[/]: {self.income} {self.currency}"
        )
        console.print(f"\t[bold][deep_sky_blue1]Currency[/]: {self.currency}")

    def config(self):
        while True:
            self.display_current_config()

            options = (
                "Configuration page",
                [
                    ("inc", "Set your annualy income"),
                    ("curr", "Set your currency of preference"),
                ],
            )
            command = self.show_options(options)

            match command:
                case "inc":
                    user_input = FloatPrompt.ask("Insert your annual income")
                    self.set_annual_income(user_input)
                case "curr":
                    user_input = Prompt.ask(
                        "Insert your currency of preference",
                        choices=DEFAULT_CURRENCY_LIST,
                    )
                    self.set_currency(user_input)
                case "q" | "quit":
                    break
                case _:
                    self.info_msg = "[bold][red]Command not valid.[/][/]"

    def set_annual_income(self, income: float):
        self.income = income
        self.info_msg = (
            f"Annual income set to [deep_sky_blue1]{self.income}[/] {self.currency}."
        )

    def set_currency(self, currency: str):
        self.currency = currency
        self.info_msg = f"Currency set to [deep_sky_blue1]{self.currency}.[/]"

    def menu(self):
        while True:
            self.clear_console()
            options = ("Personal Finance Tracker", [("cfg", "Configure your terminal")])
            command = self.show_options(options)

            if command == "cfg":
                self.config()
            elif command in ["q", "quit"]:
                exit(1)
            else:
                self.info_msg = "[bold][red]Command not valid.[/][/]"

    def run(self):
        console.clear()
        self.menu()
