from enum import Enum
from abc import ABCMeta, abstractmethod
from player_dependency import Treasure

class ICell(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self) -> str: pass

    @abstractmethod
    def execute_action(self, labyrinth, player): pass


class CellType(Enum):
    EMPTY = "empty"
    STARTING_CELL = "starting_cell"
    TREASURE = "treasure"
    WALL = "wall"
    MONOLITH = "monolith"
    NO_WALL = "no_wall"
    WORMHOLE = "wormhole"

class Cell:
    """Mother class of cells, each class will have get_cell_type """

    def __init__(self, cell_type: CellType):
        self.__cell_type = cell_type

    def get_cell_type(self):
        return self.__cell_type

class CellWormhole(Cell, ICell):
    """Wormhole cell class, to teleport the player"""

    def __init__(self, hole_number: int, total_holes: int):
        super().__init__(CellType.WORMHOLE)
        self.__number = hole_number
        self.__total_holes = total_holes

    def __str__(self):
        return str(self.__number)

    def get_number(self):
        """Each wormhole is represented by a number that is returned by this function"""
        return self.__number

    def execute_action(self, labyrinth, player):
        """When the action is triggered, this function teleport the player to the next workmhole (next number)"""
        full_size = len(labyrinth)
        for y in range(full_size):
            for x in range(full_size):
                if labyrinth[y][x].get_cell_type() == CellType.WORMHOLE:
                    if labyrinth[y][x].get_number() % self.__total_holes == (self.__number + 1) % self.__total_holes:
                        player.set_pos(int((x-1)/2), int((y - 1) / 2))
        print("*pow* -> Teleported to WormHole number " + str((self.__number + 1) % self.__total_holes))

class CellTreasure(Cell, ICell):
    """Treasure Cell, when the player goes on this cell, he takes the treasure in his inventory"""

    def __init__(self):
        super().__init__(CellType.TREASURE)

    def __str__(self):
        return "T"

    def execute_action(self, labyrinth,  player):
        """adds up the treasure to the player's inventory"""
        player.add_object(Treasure())
        p_x, p_y = player.get_pos()
        labyrinth[p_x * 2 + 1][p_y * 2 + 1] = CellEmpty()

class CellStart(Cell, ICell):
    """This is the starting cell, the place where the player starts the game"""

    def __init__(self):
        super().__init__(CellType.STARTING_CELL)

    def __str__(self):
        return "S"

    def execute_action(self, labyrinth, player): pass


class CellNoWall(Cell, ICell):
    """Cell that represent an empty space between other cells. The player can cross this cell while moving."""

    def __init__(self):
        super().__init__(CellType.NO_WALL)

    def __str__(self):
        return "-"

    def execute_action(self, labyrinth, player): pass

class CellMonolith(Cell, ICell):
    """Cell Monolith, it is an uncrossable cell placed all around the labyrinth"""

    def __init__(self):
        super().__init__(CellType.MONOLITH)

    def __str__(self):
        return "M"

    def execute_action(self, labyrinth, player): pass

class CellWall(Cell, ICell):
    """ Cell class that represent a wall that th player cannot cross while moving"""

    def __init__(self):
        super().__init__(CellType.WALL)

    def __str__(self):
        return "W"

    def execute_action(self, labyrinth, player): pass


class CellEmpty(Cell, ICell):
    """Empty cell where the player can walk"""

    def __init__(self):
        super().__init__(CellType.EMPTY)

    def __str__(self):
        return "*"

    def execute_action(self, labyrinth, player): pass
