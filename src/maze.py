from cell import Cell
import time
from window import Window
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed != None:
            self._seed = random.seed(seed)
        else:
            self._seed = 0

    def _create_cells(self):
        for i in range(self.num_cols):
            cols = []
            for j in range(self.num_rows):
                cell = Cell(0, 0, 0, 0, self.win)
                cols.append(cell)
            self._cells.append(cols)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell._x1 = self.x1 + self.cell_size_x * i
        cell._y1 = self.y1 + self.cell_size_y * j
        cell._x2 = self.x1 + self.cell_size_x * i + self.cell_size_x
        cell._y2 = self.y1 + self.cell_size_y * j + self.cell_size_y
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        cell_1 = self._cells[0][0]
        cell_2 = self._cells[self.num_cols - 1][self.num_rows - 1]
        cell_1.has_top_wall = False
        self._draw_cell(0,0)
        cell_2.has_bottom_wall = False
        self._draw_cell(self.num_cols - 1,self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])
                
    def _reset_cells_visited(self):
        for cell_row in self._cells:
            for cell in cell_row:
                cell.visited = False

    def solve(self):
        test = self.solve_r(0, 0)
        if test:
            return True
        return False

    def solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        # left
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            result = self.solve_r(i - 1, j)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        # right
        if i < self.num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            result = self.solve_r(i + 1, j)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        # up
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            result = self.solve_r(i, j - 1)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        # down
        if j < self.num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            result = self.solve_r(i, j + 1)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        else:
            return False
