import random
from time import sleep
from gui import *


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None
    ):        
        self._x1, self._y1 = x1, y1        
        self._num_rows, self._num_cols = num_rows, num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        if seed != None:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = [[None for j in range(self._num_rows)] for i in range(self._num_cols)]
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                x1 = col * self._cell_size_x + self._x1
                y1 = row * self._cell_size_y + self._y1
                x2 = (col + 1) * self._cell_size_x + self._x1
                y2 = (row + 1) * self._cell_size_y + self._y1
                self._cells[col][row] = Cell(x1, y1, x2, y2, self._window)
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        if self._window:
            self._cells[col][row].draw()
            self._animate()

    def _animate(self):
        self._window.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

    def break_walls(self):
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    
    def _break_walls_r(self, col, row):
        self._cells[col][row]._visited = True
        while True:
            to_visit = []
            shift = (0, 1, 0, -1)
            for k in range(4):
                if (
                    0 <= col + shift[k] < self._num_cols 
                    and 0 <= row + shift[3-k] < self._num_rows
                    and not self._cells[col+shift[k]][row+shift[3-k]]._visited
                ):
                    to_visit.append((shift[k], shift[3-k]))
            if not to_visit:
                if self._window != None:
                    self._cells[col][row].draw()
                return
            delta_col, delta_row = random.choice(to_visit)
            new_col, new_row = col + delta_col, row + delta_row
            auto_index = [delta_row == -1, delta_col == 1, delta_row == 1, delta_col == -1].index(1)
            sides = ['top', 'right', 'bottom', 'left']
            side = sides[auto_index]
            # neighbor_side = sides[auto_index-2]
            exec(f'self._cells[col][row].has_{side}_wall = False')
            # exec(f'self._cells[new_col][new_row].has_{neighbor_side}_wall = False')
            self._break_walls_r(new_col, new_row)

    def _reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row]._visited = False

    def solve(self):
        self._reset_cells_visited()
        return self._solve_r(0, 0)
    
    def _solve_r(self, col, row):
        self._animate()
        self._cells[col][row]._visited = True
        if col == self._num_cols - 1 and row == self._num_rows - 1:
            return True
        shift = (0, 1, 0, -1)
        sides = ['top', 'right', 'bottom', 'left']
        for k in range(4):
            delta_col, delta_row = shift[k], shift[3-k]
            new_col = col + delta_col
            new_row = row + delta_row
            side = sides[k]
            if (
                0 <= new_col < self._num_cols 
                and 0 <= new_row < self._num_rows
                and not eval(f'self._cells[col][row].has_{side}_wall')                
                and not self._cells[new_col][new_row]._visited
            ):
                to_cell = self._cells[new_col][new_row]
                self._cells[col][row].draw_move(to_cell, undo=False)
                if self._solve_r(new_col, new_row):
                    return True
                self._cells[col][row].draw_move(to_cell, undo=True)
        return False
            

        