from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800,600)

    cell_1 = Cell(2, 2, 100, 100, win, True, False)
    cell_2 = Cell(100,2,198,100, win, False)

    cell_1.draw()
    cell_2.draw()


    win.wait_for_close()
main()