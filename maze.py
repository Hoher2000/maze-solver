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
    ):        
        self._x1, self._y1 = x1, y1        
        self._num_rows, self._num_cols = num_rows, num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._create_cells()

    def _create_cells(self):
        self._cells = [[None for j in range(self._num_rows)] for i in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        filling_cell = Cell(
            i * self._cell_size_x + self._x1,
            j * self._cell_size_y + self._y1,
            (i + 1) * self._cell_size_x + self._x1,
            (j + 1) * self._cell_size_y + self._y1,
            self._window
        )
        self._cells[i][j] = filling_cell
        if self._window:
            filling_cell.draw()
            self._animate()

    def _animate(self):
        self._window.redraw()
        sleep(0.05)