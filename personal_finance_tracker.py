# IMPORTATION STANDARD
from email.policy import default

# IMPORTATION THIRD PARTY
from rich.prompt import FloatPrompt, Prompt

# IMPORTATION INTERNAL
from config import console
from helpers import print_options, create_options_str, show_balance
from constants import (
    DEFAULT_ANNUAL_INCOME,
    DEFAULT_CURRENCY,
    DEFAULT_CURRENCY_LIST,
    DEFAULT_CATEGORIES,
    DEFAULT_MONTHLY_BUDGET,
    DEFAULT_MONTHLY_FIXED_EXPENSES,
    DEFAULT_MONTHLY_BALANCE,
)
from commands import COMMANDS as cmds


class PersonalFinanceTracker:
    def __init__(
        self,
        income: float = DEFAULT_ANNUAL_INCOME,
        currency: str = DEFAULT_CURRENCY,
        categories: list = DEFAULT_CATEGORIES,
        info_msg: str = None,
        monthly_budget: float = DEFAULT_MONTHLY_BUDGET,
        monthly_fixed_expenses: float = DEFAULT_MONTHLY_FIXED_EXPENSES,
        monthly_expenses: float = 0,
        monthly_balance: float = DEFAULT_MONTHLY_BALANCE,
    ):
        self.income = income
        self.currency = currency
        self.categories = categories
        self.info_msg = None
        self.monthly_budget = monthly_budget
        self.monthly_fixed_expenses = monthly_fixed_expenses
        self.month_expenses = monthly_expenses
        self.monthly_balance = monthly_balance

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
                case "cur":
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
        self.income = income
        self.info_msg = (
            f"Annual income set to [deep_sky_blue1]{self.income}[/] {self.currency}."
        )

    def set_currency(self, currency: str):
        self.currency = currency
        self.info_msg = f"Currency set to [deep_sky_blue1]{self.currency}.[/]"

    def set_categories(self, categories: str):
        self.categories = categories.strip().split(",")
        self.info_msg = f"Categories set to [deep_sky_blue1]{self.categories}.[/]"
    
    def display_current_balances(self):
        self.clear_console()
        console.print(f"\n[bold][medium_orchid3]Monthly Summary[/][/]\n")
        console.print(
            f"\t[bold][deep_sky_blue1]Budget[/]: {self.monthly_budget} {self.currency}"
        )
        console.print(
            f"\t[bold][deep_sky_blue1]Fixed Expenses[/]: {show_balance(self.monthly_fixed_expenses)} {self.currency}"
        )
        console.print("\t...")
        console.print(
            f"\t[bold][deep_sky_blue1]Balance[/]: {show_balance(self.monthly_balance)} {self.currency}"
        )

    def update_balance(self, amount: float):
        self.monthly_balance += amount

    def add_expense(self):
        self.clear_console()
        amount = FloatPrompt.ask("\nAmount") # Elaborate
        self.update_balance(amount)
        self.info_msg = f"Expense added {show_balance(self.monthly_balance)} {self.currency}."
            

    def menu(self):
        while True:
            self.display_current_balances()
            command = self.show_options(
                title="Personal Finance Tracker",
                options=cmds.get("main_menu"),
            )

            match command:
                case "add":
                    self.add_expense()
                case "cfg":
                    self.config()
                case "q" | "quit":
                    exit(1)
                case _:
                    self.info_msg = "[bold][red]Command not valid.[/][/]"

    def run(self):
        console.clear()
        self.menu()
