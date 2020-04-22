from abc import ABCMeta, abstractmethod


class IPlayer(metaclass=ABCMeta):
    @abstractmethod
    def move_up(self, labyrinth): pass

    @abstractmethod
    def move_down(self, labyrinth): pass

    @abstractmethod
    def move_left(self, labyrinth): pass

    @abstractmethod
    def move_right(self, labyrinth): pass

class LabyrinthObject:
    def __init__(self):
        pass

class Treasure(LabyrinthObject):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "T"
