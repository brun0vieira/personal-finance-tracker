# IMPORTATION STANDARD
from email.policy import default
import json
from os import path
import argparse
import datetime

# IMPORTATION THIRD PARTY
from rich.prompt import FloatPrompt, Prompt

# IMPORTATION INTERNAL
from config.configurations import console
from helpers import print_options, create_options_str, show_balance
from config.constants import (
    DEFAULT_CURRENCY_LIST,
)
from core.commands import COMMANDS as cmds


class PersonalFinanceTracker:
    def __init__(
        self,
        user_config_dir: str,
        user_data_dir: str = None,
        info_msg: str = None,
    ):
        configs = self.parse_config(user_config_dir)
        self.income = configs.get("annual_income")
        self.currency = configs.get("currency")
        self.categories = configs.get("categories")
        self.monthly_fixed_expenses = configs.get("default_monthly_expenses")
        self.monthly_budget = round(self.income / 12 - self.monthly_fixed_expenses, 2)
        self.month_expenses = self.get_month_expenses()
        self.monthly_balance = self.calc_monthly_balance()
        self.info_msg = info_msg
        self.user_data_dir = user_data_dir
        self.user_data = self.parse_user_data(user_data_dir)

    def parse_config(self, user_config: str) -> dict:
        try:
            with open(user_config, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Config file not found. Please create a config file."
            )

    def parse_user_data(self, user_data_dir: str) -> dict:
        if path.isfile(user_data_dir):
            with open(user_data_dir, "r") as f:
                return json.load(f)

    def get_month_expenses(self):
        return []

    def calc_monthly_balance(self):
        return self.monthly_budget - sum(self.month_expenses)

    def clear_console(self):
        console.clear()
        if self.info_msg:
            console.print(self.info_msg)
            self.info_msg = None

    def show_options(self, title: str, options: list) -> tuple:
        options_str = create_options_str(title=title, options=options)
        return print_options(options_str)

    def display_current_config(self):
        # self.clear_console()
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
            command, args = self.show_options(
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
        # self.clear_console()
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

    def cmd_add_expense(self, *args, **kwargs):

        # TODO: -h option not working properly

        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="add_expense",
            description="Add an expense to the monthly expenses.",
        )
        parser.add_argument(
            "-a",
            "--amount",
            type=float,
            dest="amount",
            required=True,
            help="Amount of the expense.",
        )
        parser.add_argument(
            "-c",
            "--category",
            type=str,
            dest="category",
            required=True,
            # choices=self.categories,
            help="Category of the expense.",
        )
        parser.add_argument(
            "-d",
            "--description",
            type=str,
            dest="description",
            required=True,
            help="Description of the expense.",
        )
        parser.add_argument(
            "-dt",
            "--date",
            type=str,
            dest="date",
            required=False,
            help="Date of the expense.",
            default=datetime.datetime.now().strftime("%Y-%m-%d"),
        )
        parser.add_argument(
            "-co",
            "--comment",
            type=str,
            dest="comment",
            required=False,
            help="Comment of the expense.",
            default="",
        )

        try:
            args = parser.parse_args(args)

            if args:

                self.add_expense(
                    amount=args.amount,
                    category=args.category,
                    description=args.description,
                    date=args.date,
                    comment=args.comment,
                )
        except Exception as e:
            console.print(f"[red]{str(e)}[/]")

    def add_expense(
        self,
        amount: float,
        category: str,
        description: str,
        date: str,
        comment: str = "",
    ):

        current_month = datetime.datetime.now().strftime("%B")

        if self.user_data:
            if not self.user_data.get(current_month):
                self.user_data[current_month] = []
        else:
            self.user_data = {current_month: []}

        self.user_data[current_month].append(
            {
                "amount": amount,
                "category": category,
                "description": description,
                "date": date,
                "comment": comment,
            }
        )

        f = open(self.user_data_dir, "w")
        f.write(json.dumps(self.user_data))
        f.close()
        self.update_balance(-amount)

    def update_balance(self, amount: float):
        self.monthly_balance += amount

    def menu(self):
        while True:
            self.display_current_balances()
            command, args = self.show_options(
                title="Personal Finance Tracker",
                options=cmds.get("main_menu"),
            )

            match command:
                case "add":
                    self.cmd_add_expense(*args)
                case "cfg":
                    self.config()
                case "q" | "quit":
                    exit(1)
                case _:
                    self.info_msg = "[bold][red]Command not valid.[/][/]"

    def run(self):
        console.clear()
        self.menu()
