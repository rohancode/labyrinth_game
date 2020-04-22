from abc import *


class IUserCommand(metaclass = ABCMeta):
    @abstractmethod
    def get_command_tag(self): pass

    @abstractmethod
    def get_args_count(self): pass

    @abstractmethod
    def evaluate(self, args, labyrinth, player): pass

class GoUp(IUserCommand):
    def get_command_tag(self):
        return "go-up"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_up(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoDown(IUserCommand):
    def get_command_tag(self):
        return "go-down"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_down(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoLeft(IUserCommand):
    def get_command_tag(self):
        return "go-left"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_left(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoRight(IUserCommand):
    def get_command_tag(self):
        return "go-right"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_right(labyrinth)
        player.execute_cell_action(labyrinth)

        return won, str(success) + ": " + str(above_cell)


class Skip(IUserCommand):
    def get_command_tag(self):
        return "skip"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        player.execute_cell_action(labyrinth)
        return False, "step executed"


class ShowLabyrinth(IUserCommand):
    def get_command_tag(self):
        return "show"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        for i in labyrinth:
            for j in i:
                print(j, end="")
            print("")
        return False, "labyrinth shown"

class CommandManager:

    def __init__(self):
        self.__supported_commands = CommandManager.make_commands_dict(
            [GoDown(),
             GoUp(),
             GoLeft(),
             GoRight(),
             Skip(),
             ShowLabyrinth()
             ])

    def parse_user_input(self, user_input):
        tokens = user_input.strip().split(" ")

        if len(tokens) == 0:
            return None, None, ""

        norm_cmd = tokens[0].lower()

        if norm_cmd in self.__supported_commands:
            cmd = self.__supported_commands[norm_cmd]
            return cmd, tokens[1:10], ""

        return None, None, "Command not supported: "

    @staticmethod
    def eval_command(cmd: IUserCommand, args, labyrinth, player):
        if cmd.get_args_count() != len(args):
            return (False, "Invalid number of args. Expected: "
                    + str(cmd.get_args_count()) + ", " + "got: " + str(len(args)))
        return cmd.evaluate(args, labyrinth, player)

    @staticmethod
    def make_commands_dict(cmd_lst):
        cmd_dict = dict()
        for cmd in cmd_lst:
            cmd_dict[cmd.get_command_tag().lower().strip()] = cmd
        return cmd_dict
