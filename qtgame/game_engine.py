from qtgame.commands import Command

LOOP_FLAG = True

def start_game():
    try:
        while LOOP_FLAG:
            new_turn()
            get_input("Co chcesz zrobić? >>> ")
    except KeyboardInterrupt:
        print("Użytkowinik zakończył process")
    


def new_turn():
    print('''
    \t\t.: Quick Text Game :: Moja pierwsza gra w Pythonie
    \t.: Nowa tura :: Wpisz 'pomoc', aby zobaczyc liste dostępnych komend.
    ''')


def get_input(text):
    user_input = input(text)
    if user_input == "wyjscie":
        print("<< Opuszczasz grę >>")
        global LOOP_FLAG
        LOOP_FLAG = False
    verify_input(user_input)


def verify_input(user_input):
    if Command(user_input).check_command() is False:
        print("Nie obsługuje tej komendy.")
    else:
        Command(user_input).run()
