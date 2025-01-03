from colorama import Fore


def error_paint(error, message):
    print(f"{Fore.RED}[error] {error} {Fore.RESET}")
    return f"{Fore.BLUE} {message} {Fore.RESET}"
