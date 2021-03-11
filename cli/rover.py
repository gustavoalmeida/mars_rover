from cli.parser import parse_command, split_commands


class Rover:
    def __init__(self, initial_position=None):
        self._position = initial_position or (0, 0, "EAST")
    
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    def move(self, command):
        next_position = parse_command(self.position, command)
        self._position = next_position

    def goto(self, commands):
        for command in split_commands(commands):
            self.move(command)
