from window import Window
from point import Point
from line import Line

def main():
    win = Window(800,600)

    point_1 = Point(0,0)
    point_2 = Point(800,600)
    line = Line(point_1, point_2)
    win.draw_line(line, "black")

    point_3 = Point(350,0)
    point_4 = Point(600, 400)
    line2 = Line(point_3,point_4)
    win.draw_line(line2, "black")

    win.wait_for_close()
main()