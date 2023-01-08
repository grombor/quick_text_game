from qtgame.commands import Command

AVAIABLE_COMMANDS = {
    "pomoc",
}

AVAIABLE_EXITS = {
    "kuchnia",
    "schody"
}

AVAIABLE_EQUIPMENT = set()

FLAG_level02 = True

class Strange_Forest_Class:

    def __init__(self) -> None:
        self._exits = []

    def load_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()


    def prolog(self):
        return self.load_file("qtgame/levels/level02/prolog.txt")  


    def kuchnia(self):
        return self.load_file("qtgame/levels/level02/kuchnia.txt")  


    def schody(self):
        return self.load_file("qtgame/levels/level02/schody.txt")    


    def pokoj(self):
        return self.load_file("qtgame/levels/level02/pokoj.txt")                


    def las(self):
        return self.load_file("qtgame/levels/level02/las.txt") 


    def pomoc(self):
        return self.load_file("qtgame/pomoc.txt")


    def exits(self):
        print(f"\nDostępne wyjścia: ", end='')
        [print(e, end=', ') for e in AVAIABLE_EXITS]


    def backpack(self):
        print(f"\nRzeczy w plecaku: ", end='')  
        [print(e, end=', ') for e in AVAIABLE_EQUIPMENT]
        print("\n")


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
            case "kuchnia":
                print(f"\n{self.kuchnia()}\n")  
            case "opisz":
                print(f"\n{self.prolog()}\n")      
            case "schody":
                AVAIABLE_EXITS.clear()
                AVAIABLE_EXITS.add("pokoj")
                print(f"\n{self.pokoj()}\n")
            case "pokoj":
                print(f"\n{self.pokoj()}\n")
                self.backpack()
                user_input = input("Jeśli chcesz przyjżeć się przedmiotowi, wpisz 'zabierz przedmiot'.\n")
                if user_input == 'zabierz przedmiot':
                    AVAIABLE_EQUIPMENT.add("tajemniczy przedmiot")
                    print("Trzymasz w ręku tajemniczy przedmiot")
                    user_input = input("Jeśli chcesz przyjżeć się przedmiotowi, wpisz 'uzyj przedmiot'. Jeśli chcesz daje rozglądać się po pokoju, wpisz 'rozgladaj sie'.\n")
                    if user_input == 'uzyj przedmiot':
                        AVAIABLE_EQUIPMENT.clear()
                        AVAIABLE_EXITS.clear()
                        print(f"\n{self.las()}\n")
                        print("<< Opuszczasz ten świat... >>")
                        raise SystemExit 
            case other:
                pass


    def start(self):
        print(self.prolog())
        while FLAG_level02:
            print("\n\n:: Wpisz 'pomoc', aby zobaczyc liste dostępnych komend.")
            self.exits()
            self.get_input(">>> ")
