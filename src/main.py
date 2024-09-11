from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800,600)

    cell_1 = Cell(100, 100, 2, 2, win)
    cell_2 = Cell(200, 200, 50, 67, win)

    cell_1.draw()
    cell_2.draw()

    cell_1.draw_move(cell_2, True)


    win.wait_for_close()
main()