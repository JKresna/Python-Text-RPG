# Title screens untuk game
import sys


def screen_selections():
    while True:
        option = input("> ").lower()

        if option in {"play", "start", "run"}:
            setup_game()
            break
        elif option in {"help", "h", "menu"}:
            help_menu()
            break
        elif option in {"quit", "q", "exit"}:
            sys.exit()
        else:
            print("Please enter a valid command.")


def setup_game():
    print("Setup game")


def help_menu():
    print("Help menu")
