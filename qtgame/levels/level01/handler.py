import threading
from qtgame.commands import Command

AVAIABLE_COMMANDS = {
    "pomoc",
}

AVAIABLE_EXITS = {
    "pokoj",
    "hol"
}

AVAIABLE_EQUIPMENT = set()

FLAG_level01 = True

class Strange_House_Class:

    def __init__(self) -> None:
        self._exits = []

    def load_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()


    def prolog(self):
        return self.load_file("qtgame/levels/level01/prolog.txt")


    def hol(self):
        return self.load_file("qtgame/levels/level01/hol.txt")


    def pokoj(self):
        return self.load_file("qtgame/levels/level01/pokoj.txt")        


    def pomoc(self):
        return self.load_file("qtgame/pomoc.txt")


    def exits(self):
        print(f"\nDostępne wyjścia: ", end='')
        [print(e, end=', ') for e in AVAIABLE_EXITS]


    def backpack(self):
        print(f"\nRzeczy w plecaku: ", end='')  
        [print(e, end=', ') for e in AVAIABLE_EQUIPMENT]
        print("\n")


    def handlePicture(self):
        if "rysunek" in AVAIABLE_EQUIPMENT:
            AVAIABLE_EQUIPMENT.clear()
        user_input = input("Jeśli chcesz przyjżeć się rysunkowi, wpisz 'zabierz rysunek'\n")
        if user_input == 'zabierz rysunek':
            AVAIABLE_EQUIPMENT.add("rysunek")
            print("Trzymasz w ręku tajemniczy rysunek")
            user_input = input("Jeśli chcesz przyjżeć się rysunkowi, wpisz 'uzyj rysunek'. Jeśli chcesz daje rozglądać się po pokoju, wpisz 'rozgladaj sie'.\n")
            if user_input == 'uzyj rysunek':
                self.load_file("qtgame/levels/level01/rysunek.txt")
                if "rysunek" in AVAIABLE_EQUIPMENT:
                    AVAIABLE_EQUIPMENT.clear()
                    global FLAG_level01
                    FLAG_level01 = False


    def verify_input(self, user_input):
        if Command(user_input, AVAIABLE_COMMANDS).check_command() is False:
            print("Nie obsługuje tej komendy.")
        else:
            self.run(user_input)


    def verify_exit(self, user_input):
        if Command(user_input, AVAIABLE_EXITS).check_command() is False:
            print("Nie możesz tam iść.")
        else:
            self.run(user_input)


    def get_input(self, text):
        user_input = input(text)
        if user_input == "wyjscie":
            print("<< Opuszczasz grę >>")
            raise SystemExit 
        self.run(user_input)

    
    def run(self, content):
        match content.lower():
            case "pomoc":
                print(f"\n{self.pomoc()}\n")
            case "hol":
                print(f"\n{self.hol()}\n")  
            case "opisz":
                print(f"\n{self.prolog()}\n")                 
            case "pokoj":
                AVAIABLE_EQUIPMENT.clear()
                print(f"\n{self.pokoj()}\n")
                self.exits()
                self.backpack()
                self.handlePicture()                   
            case other:
                pass


    def start(self):
        print(self.prolog())
        while FLAG_level01:
            print("\n\n:: Wpisz 'pomoc', aby zobaczyc liste dostępnych komend.")
            self.exits()
            self.get_input(">>> ")
