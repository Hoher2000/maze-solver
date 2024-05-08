from gui import *

def main():
    win = Window(800, 600)     
    cell1 = Cell(10,10,30, 30, win)   
    cell2 = Cell(30, 10, 50, 30, win)
    cell1.has_bottom_wall = 0
    cell2.has_top_wall = 0
    cell1.draw()
    cell2.draw()   
    cell1.draw_move(cell2, undo=0)
    win.wait_for_close()
   
if __name__ == '__main__':
    main()
