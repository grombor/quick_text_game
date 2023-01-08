class Command():
    def __init__(self, content, commands = {"pomoc", "wyjscie", "start"}):
        self._content = content
        self._commands = commands

    def check_command(self):
        if self._content not in self._commands:
            return False
        return True

