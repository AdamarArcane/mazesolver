from point import Point
from line import Line
from window import Window

class Cell():
    def __init__(self, x1, y1, x2, y2, win=None, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
        if self.has_left_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x1, self._y2)
            line = Line(point_1, point_2)
            line.draw(self._win.canvas)
        if not self.has_left_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x1, self._y2)
            line = Line(point_1, point_2)
            line.draw(self._win.canvas, "black")
        if self.has_right_wall:
            point_1 = Point(self._x2, self._y1)
            point_2 = Point(self._x2, self._y2)
            line = Line(point_1, point_2)
            line.draw(self._win.canvas)
        if not self.has_right_wall:
            point_1 = Point(self._x2, self._y1)
            point_2 = Point(self._x2, self._y2)
            line = Line(point_1, point_2)
            line.draw(self._win.canvas, "black")
        if self.has_top_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x2, self._y1)
            line = Line(point_1, point_2)
            line.draw(self._win.canvas)
        if not self.has_top_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x2, self._y1)
            line = Line(point_1, point_2)
            line.draw(self._win.canvas, "black")
        if self.has_bottom_wall:
            point_1 = Point(self._x1, self._y2)
            point_2 = Point(self._x2, self._y2)
            line = Line(point_1, point_2)
            line.draw(self._win.canvas)
        if not self.has_bottom_wall:
            point_1 = Point(self._x1, self._y2)
            point_2 = Point(self._x2, self._y2)
            line = Line(point_1, point_2)
            line.draw(self._win.canvas, "black")
    
    def draw_move(self, to_cell, undo=False):
        middle_x_1 = abs(self._x1 - self._x2) / 2 + min(self._x1, self._x2)
        middle_y_1 = abs(self._y1 - self._y2) / 2 + min(self._y1, self._y2)
        middle_x_2 = abs(to_cell._x1 - to_cell._x2) / 2 + min(to_cell._x1, to_cell._x2)
        middle_y_2 = abs(to_cell._y1 - to_cell._y2) / 2 + min(to_cell._y1, to_cell._y2)
        point_1 = Point(middle_x_1, middle_y_1)
        point_2 = Point(middle_x_2, middle_y_2)
        line = Line(point_1, point_2)
        if undo:
            line.draw(self._win.canvas, "black")
        else:
            line.draw(self._win.canvas, "green2")
