from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title('Maze solver')
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()
        self.__isrun = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__isrun = True
        while self.__isrun:
            self.redraw()

    def close(self):
        self.__isrun = False
