from colorama import Fore, Style, init; import datetime
init()
def format_current_time():
    current_time = datetime.datetime.now();formatted_time = current_time.strftime("%H:%M:%S");return formatted_time
def Sprint(token: str):
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{format_current_time()}{Fore.LIGHTWHITE_EX}] [{Fore.LIGHTGREEN_EX}${Fore.LIGHTWHITE_EX}] {Fore.MAGENTA}- {Fore.LIGHTBLUE_EX}[REACTED] {Fore.LIGHTCYAN_EX}Reacted With Token {Fore.LIGHTBLUE_EX}{token[:18]}***")
def Eprint(token: str):
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{format_current_time()}{Fore.LIGHTWHITE_EX}] [{Fore.LIGHTRED_EX}-{Fore.LIGHTWHITE_EX}] {Fore.MAGENTA}- {Fore.LIGHTBLUE_EX}[FAILED] {Fore.LIGHTCYAN_EX}Reacting Failed With Token {Fore.LIGHTBLUE_EX}{token[:18]}***")
def Inp(content: str):
    return input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{format_current_time()}{Fore.LIGHTWHITE_EX}] [{Fore.LIGHTBLUE_EX}?{Fore.LIGHTWHITE_EX}] {Fore.MAGENTA}- {Fore.LIGHTBLUE_EX}[INPUT] {Fore.LIGHTCYAN_EX}{content}")
def Dprint(content: str):
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{format_current_time()}{Fore.LIGHTWHITE_EX}] [{Fore.LIGHTBLUE_EX}#{Fore.LIGHTWHITE_EX}] {Fore.MAGENTA}- {Fore.LIGHTBLUE_EX}[DEBUG] {Fore.LIGHTCYAN_EX}{content}")
def Iprint(proccessed: str, failed: str, reacted: str):
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{format_current_time()}{Fore.LIGHTWHITE_EX}] [{Fore.LIGHTBLUE_EX}@{Fore.LIGHTWHITE_EX}] {Fore.MAGENTA}- {Fore.LIGHTBLUE_EX}[INFO] {Fore.LIGHTCYAN_EX}Materials Finised, Reacted: {reacted}, Failed: {failed}, Proccessed: {proccessed}, Finised At: {format_current_time()}")