from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height) -> None:
        self._root = Tk()
        self._root.title('Maze solver')
        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._isrun = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._isrun = True
        while self._isrun:
            self.redraw()
        print('window closed')

    def close(self):
        self._isrun = False

    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)


class Point:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y


class Line:
    def __init__(self, dot1, dot2) -> None:
        self._dot1 = dot1
        self._dot2 = dot2

    def draw(self, Canvas, fill_color):
        Canvas.create_line(
            self._dot1._x, self._dot1._y, self._dot2._x, self._dot2._y,
            fill=fill_color, width=2
        )


class Cell:
    def __init__(self, x1, y1, x2, y2, window=None):
        # x1, y1 - top left corner, x2, y2 - bottom right corner
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._visited = False
        self._top_left_dot = Point(x1, y1)
        self._top_right_dot = Point(x2, y1)
        self._bottom_left_dot = Point(x1, y2)
        self._bottom_right_dot = Point(x2, y2)
        x_center, y_center = x1 + (x2-x1)/2, y1 + (y2-y1)/2        
        self._center = Point(x_center, y_center)
        self._window = window

    def draw(self):
        left_wall = Line(self._top_left_dot, self._bottom_left_dot)
        right_wall = Line(self._top_right_dot, self._bottom_right_dot)
        top_wall = Line(self._top_right_dot, self._top_left_dot)
        bottom_wall = Line(self._bottom_right_dot, self._bottom_left_dot)
        sides = ['left', 'right', 'top', 'bottom']
        for side in sides:
            color = 'black' if eval(f'self.has_{side}_wall') else 'white'
            eval(f'self._window.draw_line({side}_wall, color)')
        
    def draw_move(self, to_cell, undo=False):
        if self._window is not to_cell._window:
            raise Exception('Cells are in different windows')
        color = 'gray' if undo else 'red'
        move_line = Line(self._center, to_cell._center)
        self._window.draw_line(move_line, color)