from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800,600)

    m1 = Maze(250, 50, 3, 3, 50, 50, win)

    m1._create_cells()
    m1._draw_cell(0,1)
    m1._draw_cell(0,2)
    m1._draw_cell(1,1)
    m1._draw_cell(2,1)
    m1._draw_cell(2,2)
    m1._draw_cell(1,0)
    m1._draw_cell(2,0)
    m1._draw_cell(1,2)
    m1._break_walls_r(0,0)
    m1._break_entrance_and_exit()

    win.wait_for_close()
main()