import unittest
from maze import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        m._break_walls_r(0, 0)     
        self.assertEqual(
            m._cells[5][5]._visited,
            1,
        )
        m._reset_cells_visited()
        self.assertEqual(
            m._cells[0][9]._visited,
            0,
        )

if __name__ == "__main__":
    unittest.main()      