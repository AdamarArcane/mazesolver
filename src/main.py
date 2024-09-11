from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800,600)

    m1 = Maze(5, 5, 12, 10, 40, 40, win)

    m1._create_cells()
    for i in range(m1.num_cols):
        for j in range(m1.num_rows):
            m1._draw_cell(i,j)
    m1._break_walls_r(0,0)
    m1._reset_cells_visited()
    m1._break_entrance_and_exit()
    m1.solve()

    win.wait_for_close()
main()