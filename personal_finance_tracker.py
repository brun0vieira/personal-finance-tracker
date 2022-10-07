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
    DEFAULT_CATEGORIES,
)
from commands import COMMANDS as cmds


class PersonalFinanceTracker:
    def __init__(
        self,
        income: float = DEFAULT_ANNUAL_INCOME,
        currency: str = DEFAULT_CURRENCY,
        categories: list = DEFAULT_CATEGORIES,
        info_msg: str = None,
    ):
        self.income = income
        self.currency = currency
        self.info_msg = None
        self.categories = categories

    def clear_console(self):
        console.clear()
        if self.info_msg:
            console.print(self.info_msg)
            self.info_msg = None

    def show_options(self, title: str, options: list) -> str:
        options_str = create_options_str(title=title, options=options)
        return print_options(options_str)

    def display_current_config(self):
        self.clear_console()
        console.print(f"\n[bold][medium_orchid3]Current configurations[/][/]\n")
        console.print(
            f"\t[bold][deep_sky_blue1]Annual income[/]: {self.income} {self.currency}"
        )
        console.print(
            f"\t[bold][deep_sky_blue1]Monthly income[/]: {self.income / 12 :.2f} {self.currency}"
        )
        console.print(f"\t[bold][deep_sky_blue1]Currency[/]: {self.currency}")
        console.print(
            f"\t[bold][deep_sky_blue1]Expense categories[/]: {self.categories}"
        )

    def config(self):
        while True:
            self.display_current_config()
            command = self.show_options(
                title="Configuration page",
                options=cmds.get("configuration"),
            )

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
                case "cat":
                    user_input = Prompt.ask("Insert your categories (comma separated)")
                    self.set_categories(user_input)
                case "q" | "quit":
                    break
                case _:
                    self.info_msg = "[bold][red]Command not valid.[/][/]"

    def set_annual_income(self, income: float):
        self.income = round(income, 2)
        self.info_msg = (
            f"Annual income set to [deep_sky_blue1]{self.income}[/] {self.currency}."
        )

    def set_currency(self, currency: str):
        self.currency = currency
        self.info_msg = f"Currency set to [deep_sky_blue1]{self.currency}.[/]"

    def set_categories(self, categories: str):
        self.categories = categories.strip().split(",")
        self.info_msg = f"Categories set to [deep_sky_blue1]{self.categories}.[/]"

    def menu(self):
        while True:
            self.clear_console()
            command = self.show_options(
                title="Personal Finance Tracker",
                options=cmds.get("main_menu"),
            )

            match command:
                case "cfg":
                    self.config()
                case "q" | "quit":
                    exit(1)
                case _:
                    self.info_msg = "[bold][red]Command not valid.[/][/]"

    def run(self):
        console.clear()
        self.menu()
