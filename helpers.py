# IMPORTATION STANDARD
import datetime

# IMPORTATION THIRD PARTY

# IMPORTATION INTERNAL
from config import console


def print_options(text: str) -> str:
    console.print(f"\n{text}\n")
    now = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
    command = input(f"[{str(now)}] ~ ")
    return command


def create_options_str(title: str, options: str) -> str:
    text = f"\n[bold][steel_blue3]{title}[/][/bold]"
    for option in options:
        text += f"\n\t> [bold][khaki3]{option[0]}[/][/]"
        text += f"\t[bold]{option[1]}[/]"
    text += f"\n\t> [bold][khaki3]quit[/][/]"
    text += f"\tQuit"
    return f"{text}\n"
