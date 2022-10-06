import os
from rich.console import Console
from rich.prompt import FloatPrompt
import datetime

RICH_ERROR = 'red'
RICH_CMD = 'khaki3'
RICH_NUMBERS = 'deep_sky_blue1'
RICH_TITLE = 'steel_blue3'
RICH_INFO = 'medium_orchid3'

console = Console(
    tab_size = 4,
    highlight = False
)

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
        text = f"\n[bold][{RICH_TITLE}]{title}[/][/bold]"
        for option in options:
            text += f"\n\t> [bold][{RICH_CMD}]{option[0]}[/][/]"
            text += f"\t[bold]{option[1]}[/]"
        text += f"\n\t> [bold][{RICH_CMD}]quit[/][/]" 
        text += f"\tQuit"
        return f"{text}\n"

    def show_options(self, options):
        text = self.create_options_str(options[0], options[1])
        command = self.print_options(text)
        return command

    def config(self):
        while True:
            options = (
                "Configuration page",
                [
                    ("inc", "Set your annualy income"),
                    ("curr", "Set your currency of preference"),
                    ("info", "Check current configurations")
                ]
            )
            command = self.show_options(options)
            
            if command == 'inc':
                console.print(f"Annualy income currently set to [{RICH_NUMBERS}]{self.income}[/] {self.currency}.")
                user_input = FloatPrompt.ask('Insert your annualy income')
                self.income = user_input
                console.print(f"Annualy income set to [{RICH_NUMBERS}]{self.income}[/] {self.currency}.")

            elif command == 'curr':
                console.print(f"Currency currently set to [{RICH_NUMBERS}]{self.currency}[/].")
                user_input = input('Set your currency of preference (ISO 4217): ')
                while len(user_input) not in [2, 3]: # change to a decent validation (check if the code is valid using an API?)
                    console.print(f"\n[bold][{RICH_ERROR}]Invalid currency code.[/][/]")
                    user_input = input('Set your currency of preference (ISO 4217): ')
                self.currency = user_input.upper()
                console.print(f"Currency set to [{RICH_NUMBERS}]{self.currency}.[/]")
            
            elif command in ['info']:
                console.print(f"\n[bold][{RICH_INFO}]Current configurations[/][/]\n\tAnnual income: [{RICH_NUMBERS}]{self.income}[/]\n\tCurrency: [{RICH_NUMBERS}]{self.currency}[/]")
            
            elif command in ['q', 'quit']:
                break
            
            else:
                console.print(f'[bold][{RICH_ERROR}]Command not valid.[/][/]')

    def clear(self):
        console.clear()
    
    def menu(self):
        while True:
            options = (
                "Personal Finance Tracker",
                [
                    ("cfg", "Configure your terminal")
                ]
            )
            command = self.show_options(options)
            
            if command == 'cfg':
                self.config()
            elif command in ['q', 'quit']:
                exit(1)
            else:
                console.print(f"[bold][{RICH_ERROR}]Command not valid.[/][/]")

    def run(self):
        console.clear()
        self.menu()

if __name__ == "__main__":

    default_income = 21700
    default_currency = 'EUR'
    
    pft = PersonalFinanceTracker(
        default_income, 
        default_currency 
    )
    pft.run()