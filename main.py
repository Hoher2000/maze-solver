from gui import *

def main():
    win = Window(800, 600)
    dot1, dot2, dot3 = Point(10, 100), Point(400, 400), Point(100, 100)
    win.draw_line(Line(dot1, dot2), 'red')
    win.draw_line(Line(dot3, dot2), 'blue')
    win.wait_for_close()
    
if __name__ == '__main__':
    main()
