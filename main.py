from gui import *
from maze import *

def main():
    win = Window(800, 600)     
    cell1 = Cell(10,10,30, 30, win)   
    cell2 = Cell(300, 100, 500, 300, win)    
    num_cols = 10
    num_rows = 9
    m1 = Maze(10, 10, num_rows, num_cols, 30, 30, win, 10268610102)
    m1.break_walls()
    m1.solve()
    win.wait_for_close()
   
if __name__ == '__main__':
    main()
