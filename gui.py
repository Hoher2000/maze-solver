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


class Cell:
    def __init__(self, x1, y1, x2, y2, window):
        # x1, y1 - top left corner, x2, y2 - bottom right corner
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__top_left_dot = Point(x1, y1)
        self.__top_right_dot = Point(x2, y1)
        self.__bottom_left_dot = Point(x1, y2)
        self.__bottom_right_dot = Point(x2, y2)
        x_center, y_center = x1 + (x2-x1)/2, y1 + (y2-y1)/2        
        self.__center = Point(x_center, y_center)
        self.__window = window

    def draw(self):
        if self.has_left_wall:
            left_wall = Line(self.__top_left_dot, self.__bottom_left_dot)
            self.__window.draw_line(left_wall, 'black')
        if self.has_right_wall:
            right_wall = Line(self.__top_right_dot, self.__bottom_right_dot)
            self.__window.draw_line(right_wall, 'black')
        if self.has_top_wall:
            top_wall = Line(self.__top_right_dot, self.__top_left_dot)
            self.__window.draw_line(top_wall, 'black')
        if self.has_bottom_wall:
            bottom_wall = Line(self.__bottom_right_dot, self.__bottom_left_dot)
            self.__window.draw_line(bottom_wall, 'black')

    def draw_move(self, to_cell, undo=False):
        if self.__window is not to_cell.__window:
            raise Exception('Cells are in different windows')
        color = 'gray' if undo else 'red'
        move_line = Line(self.__center, to_cell.__center)
        self.__window.draw_line(move_line, color)