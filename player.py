import player_dependency
import cells

class new(player_dependency.IPlayer):

    def __init__(self, pos_x: int, pos_y: int):
        self.__objects = []
        self.__pos_x = pos_x
        self.__pos_y = pos_y

    def add_object(self, obj):
        self.__objects.append(obj)

    def remove_object(self, obj):
        self.__objects.pop(self.__objects.index(obj))

    def get_objects(self):
        return self.__objects

    def set_objects(self, objects):
        self.__objects = objects

    def get_current_cell(self, labyrinth):
        return labyrinth[(self.__pos_y * 2 + 1)][self.__pos_x * 2 + 1]

    def get_pos(self):
        return self.__pos_x, self.__pos_y

    def set_pos(self, x, y):
        self.__pos_x = x
        self.__pos_y = y

    def execute_cell_action(self, labyrinth):
        current_cell = self.get_current_cell(labyrinth)
        current_cell.execute_action(labyrinth, self)

    def move_up(self, labyrinth):
        above_cell = labyrinth[(self.__pos_y * 2 + 1) - 1][self.__pos_x * 2 + 1].get_cell_type()
        if above_cell == cells.CellType.WALL or above_cell == cells.CellType.MONOLITH:
            return "step impossible", above_cell.value, False
        elif above_cell == cells.CellType.NO_WALL and self.__pos_y == 0 and self.player_has_treasure():
            return "step executed", "out of labyrinth", True
        elif above_cell == cells.CellType.NO_WALL and self.__pos_y == 0 and not self.player_has_treasure():
            return "step impossible", "no treasure in inventory", False
        else:
            self.__pos_y -= 1
            return "step executed", self.get_current_cell(labyrinth).get_cell_type().value, False

    def move_down(self, labyrinth):
        underneath__cell = labyrinth[(self.__pos_y * 2 + 1) + 1][self.__pos_x * 2 + 1].get_cell_type()
        if underneath__cell == cells.CellType.WALL or underneath__cell == cells.CellType.MONOLITH:
            return "step impossible", underneath__cell.value, False
        elif underneath__cell == cells.CellType.NO_WALL and self.__pos_y == len(labyrinth) - 1 and self.player_has_treasure():
            return "step executed", "out of labyrinth", True
        elif underneath__cell == cells.CellType.NO_WALL and self.__pos_y == len(labyrinth) - 1 and not self.player_has_treasure():
            return "step impossible", "no treasure in inventory", False
        else:
            self.__pos_y += 1
            return "step executed", self.get_current_cell(labyrinth).get_cell_type().value, False

    def move_left(self, labyrinth):
        left_cell = labyrinth[(self.__pos_y * 2 + 1)][(self.__pos_x * 2 + 1) - 1].get_cell_type()
        if left_cell == cells.CellType.WALL or left_cell == cells.CellType.MONOLITH:
            return "step impossible", left_cell.value, False
        elif left_cell == cells.CellType.NO_WALL and self.__pos_x == 0 and self.player_has_treasure():
            return "step executed", "out of labyrinth", True
        elif left_cell == cells.CellType.NO_WALL and self.__pos_x == 0 and not self.player_has_treasure():
            return "step impossible", "no treasure in inventory", False
        else:
            self.__pos_x -= 1
            return "step executed", self.get_current_cell(labyrinth).get_cell_type().value, False

    def move_right(self, labyrinth):
        right_cell = labyrinth[(self.__pos_y * 2 + 1)][(self.__pos_x * 2 + 1) + 1].get_cell_type()
        if right_cell == cells.CellType.WALL or right_cell == cells.CellType.MONOLITH:
            return "step impossible", right_cell.value, False
        elif right_cell == cells.CellType.NO_WALL and self.__pos_x == len(labyrinth) - 1 and self.player_has_treasure():
            return "step executed", "out of labyrinth", True
        elif right_cell == cells.CellType.NO_WALL and self.__pos_x == len(labyrinth) - 1 and not self.player_has_treasure():
            return "step impossible", "no treasure in inventory", False
        else:
            self.__pos_x += 1
            return "step executed", self.get_current_cell(labyrinth).get_cell_type().value, False

    def player_has_treasure(self):
        return True in [isinstance(obj, player_dependency.Treasure) for obj in self.__objects]
