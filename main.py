from gui import *
from maze import *

def main():
    win = Window(800, 600)     
    cell1 = Cell(10,10,30, 30, win)   
    cell2 = Cell(300, 100, 500, 300, win)    
    num_cols = 5
    num_rows = 5
    m1 = Maze(10, 10, num_rows, num_cols, 30, 30, win, 102)
    m1._break_entrance_and_exit()
    m1._break_walls_r(0, 0)
    m1._reset_cells_visited()
    win.wait_for_close()
   
if __name__ == '__main__':
    main()
