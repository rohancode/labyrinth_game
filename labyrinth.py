import cells
from random import randint

def initialize_special_cells():
    special_cells = [cells.CellWormhole(1, 5),
                     cells.CellWormhole(2, 5),
                     cells.CellWormhole(3, 5),
                     cells.CellWormhole(4, 5),
                     cells.CellWormhole(5, 5),
                     cells.CellTreasure(),
                     cells.CellStart()]
    return special_cells

def generate_random_exit(size):
    exit_x = randint(1, size) * 2 - 1
    exit_y = randint(1, size) * 2 - 1
    if randint(0, 1) == 0:
        exit_x = randint(0, 1) * (size * 2)
    else:
        exit_y = randint(0, 1) * (size * 2)
    return exit_x, exit_y

def generate_walls(exit_x, exit_y, grid_size, row, i, j):
    if exit_x == j and exit_y == i:
        row.append(cells.CellNoWall())
    elif i == 0 or i == grid_size - 1 or j == 0 or j == grid_size - 1:  # monolith
        row.append(cells.CellMonolith())
    elif i % 2 == 0 or j % 2 == 0:
        if randint(1, 10) < 4:
            row.append(cells.CellWall())
        else:
            row.append(cells.CellNoWall())
    else:
        return False
    return True


def make(size):
    lib = []
    special_cells = initialize_special_cells()
    exit_x, exit_y = generate_random_exit(size)
    start_x, start_y = -1, -1
    grid_size = size * 2 + 1
    number_of_active_cells = size * size
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            is_wall_space = generate_walls(exit_x, exit_y, grid_size, row, i, j)
            if not is_wall_space:
                if randint(0,100) < int((float(len(special_cells)) / number_of_active_cells)*100):
                    index = randint(0, len(special_cells)-1)
                    row.append(special_cells[index])
                    if special_cells[index].get_cell_type() == cells.CellType.STARTING_CELL:
                        start_x = (j - 1) / 2
                        start_y = (i - 1) / 2
                    special_cells.pop(index)
                else:
                    row.append(cells.CellEmpty())
                number_of_active_cells -= 1

        lib.append(row)
    return lib, start_x, start_y
