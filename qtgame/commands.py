class Command():
    __commands = {"pomoc", "wyjscie"}

    def __init__(self, content):
        self._content = content

    def check_command(self):
        if self._content not in self.__commands:
            return False
        return True

    def run(self):
        match self._content:
            case "pomoc":
                print("Wybrałeś pomoc")
            case other:
                pass