import threading
from qtgame.commands import Command
from qtgame.levels.level01.handler import Strange_House_Class


def start_game():
    new_turn()
    try:
        while True:
            get_input("Co chcesz zrobić? >>> ")
    except KeyboardInterrupt:
        print("Użytkowinik zakończył process")
    


def new_turn():
    print('''
    \t\t.: Quick Text Game :.
    \t.: Wpisz 'pomoc', aby zobaczyc liste dostępnych komend.
    ''')


def get_input(text):
    user_input = input(text)
    if user_input == "wyjscie":
        print("<< Opuszczasz grę >>")
        raise SystemExit
    verify_input(user_input)


def test():
    print("rozdzial drugi...")


def run(content):
    match content:
        case "pomoc":
            print(f"\n{Strange_House_Class().pomoc()}\n")
        case "start":
            threading.Thread(target=Strange_House_Class().start(),).start()
            threading.Thread(target=test(),).start()
        case other:
            pass


def verify_input(user_input):
    if Command(user_input).check_command() is False:
        print("Nie obsługuje tej komendy.")
    else:
        run(user_input)
