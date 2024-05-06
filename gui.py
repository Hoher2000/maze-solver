from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title('Maze solver')
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__isrun = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__isrun = True
        while self.__isrun:
            self.redraw()
        print('window closed')

    def close(self):
        self.__isrun = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, dot1, dot2) -> None:
        self.dot1 = dot1
        self.dot2 = dot2

    def draw(self, Canvas, fill_color):
        Canvas.create_line(
            self.dot1.x, self.dot1.y, self.dot2.x, self.dot2.y,
            fill=fill_color, width=2
        )