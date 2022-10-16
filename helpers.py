# IMPORTATION STANDARD
import datetime
from typing import List, Tuple

# IMPORTATION THIRD PARTY

# IMPORTATION INTERNAL
from config.configurations import console


def print_options(text: str) -> tuple:
    console.print(f"\n{text}\n")
    now = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
    command = input(f"[{str(now)}] ~ ")
    command = command.split(" ")
    args = " ".join(command[1:])
    return command[0], str_to_args(args)


def str_to_args(args: str) -> tuple:
    args = args.split(" ")

    if len(args) == 1:
        return args[0]

    return (
        f"{arg} {args[index + 1]}"
        for index, arg in enumerate(args)
        if arg.startswith("-")
    )


def create_options_str(title: str, options: str) -> str:
    text = f"\n[bold][steel_blue3]{title}[/][/bold]\n"
    for option in options:
        text += f"\n\t> [bold][khaki3]{option[0]}[/][/]"
        text += f"\t[bold]{option[1]}[/]"
    text += f"\n\t> [bold][khaki3]quit[/][/]"
    text += f"\tQuit"
    return f"{text}\n"


def show_balance(balance: float) -> str:
    color = "dark_slate_gray2" if balance > 0 else "red"
    return f"[{color}]{balance}[/]"
