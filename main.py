import os

def validate_number(input_value):
    try:
        value = int(input_value)
        return True
    except ValueError:
        try:
            value = float(input_value)
            return True
        except ValueError:
            return False    

class PersonalFinanceTracker:

    def __init__(self, income, currency):
        self.income = income
        self.currency = currency

    def print_options(self, text):
        print(text)
        command = input('~ ')
        self.clear()
        return command

    def create_options_str(self, title, options):
        text = f"\n{title}"
        for option in options:
            text += f"\n\t> {option}"
        text += f"\n\t> (q/quit) Quit"
        return f"{text}\n"
    
    def config(self):
        while True:
            options = self.create_options_str(
                "Configuration page",
                [
                    "(inc/income) Income",
                    "(curr/currency) Currency",
                    "(info) Check current configurations"
                ]
            )
            command = self.print_options(options)
            
            if command in ['inc', 'income']:
                print(f"Annualy income currently set to {self.income} {self.currency}.")
                user_input = input('Insert your annualy income: ')
                while not validate_number(user_input):
                    print('\nInvalid value.')
                    user_input = input('Insert your annualy income: ')
                self.income = user_input    
                print(f"Annualy income set to {self.income} {self.currency}.")

            elif command in ['curr', 'currency']:
                print(f"Currency set to {self.currency}.")
                user_input = input('Set your currency of preference (ISO 4217): ')
                while len(user_input) not in [2, 3]: # change to a decent validation (check if the code is valid using an API?)
                    print('\nInvalid currency code.')
                    user_input = input('Set your currency of preference (ISO 4217): ')
                self.currency = user_input.upper()
                print(f"Currency set to {self.currency}.")
            elif command in ['info']:
                print(f"\nCurrent configurations:\n\tAnnual income: {self.income}\n\tCurrency: {self.currency}")
            elif command in ['q', 'quit']:
                break
            
            else:
                print('Command not valid.')

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        while True:
            options = self.create_options_str(
                "Personal Finance Tracker",
                [
                    "(cfg/config) Configure your terminal"
                ]
            )
            command = self.print_options(options)
            
            if command in ['cfg', 'config']:
                self.config()
            elif command in ['q', 'quit']:
                exit(1)
            else:
                print('Command not valid.')

    def run(self):
        self.clear()
        self.menu()

if __name__ == "__main__":

    default_income = 21700
    default_currency = 'EUR'

    pft = PersonalFinanceTracker(
        default_income, 
        default_currency 
    )
    pft.run()