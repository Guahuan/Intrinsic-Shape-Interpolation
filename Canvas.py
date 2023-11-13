import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backend_bases import MouseButton

from IntrinsicShapeInterpolation import *
from TurtleGeometry import *
from Struct import *


class Canvas:
    def __init__(self, frame=10):
        self.fig, self.ax = plt.subplots()
        self.scatter, = self.ax.plot([], [], marker='o', color='green')
        self.all_frame = frame
        self.animation = None
        self.fig.canvas.mpl_connect("button_press_event", self.onMousePress)
        self.fig.canvas.mpl_connect("motion_notify_event", self.onMouseMove)
        self.fig.canvas.mpl_connect("key_press_event", self.onKeyPress)

        self.init()

    def init(self):
        self.ax.cla()
        self.ax.set_title('Intrinsic Shape Interpolation')
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_xlim(-20, 20)
        self.ax.set_ylim(-20, 20)
        self.fig.canvas.draw()

        if self.animation:
            self.animation.pause()
            self.animation = None

        self.model = "darw_A"
        self.polygon_A = Polygon([])
        self.turtle_A = Turtle(None, [], [])
        self.polygon_B = Polygon([])
        self.turtle_B = Turtle(None, [], [])

    def drawPolygon(self):
        self.ax.cla()
        self.ax.set_title('Intrinsic Shape Interpolation')
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_xlim(-20, 20)
        self.ax.set_ylim(-20, 20)

        x_A = [p.x for p in self.polygon_A.points]
        y_A = [p.y for p in self.polygon_A.points]
        if len(x_A) >= 3:
            x_A.append(x_A[0])
            y_A.append(y_A[0])
        self.ax.plot(x_A, y_A, marker='o', color='red')

        x_B = [p.x for p in self.polygon_B.points]
        y_B = [p.y for p in self.polygon_B.points]
        if len(x_B) >= 3:
            x_B.append(x_B[0])
            y_B.append(y_B[0])
        self.ax.plot(x_B, y_B, marker='o', color='blue')

        self.fig.canvas.draw()

    def drawAnimation(self):
        self.ax.cla()
        self.ax.set_title('Intrinsic Shape Interpolation')
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_xlim(-20, 20)
        self.ax.set_ylim(-20, 20)

        self.turtle_A = polygon2Turtle(self.polygon_A)
        self.turtle_B = polygon2Turtle(self.polygon_B)

        self.animation = FuncAnimation(self.fig, self.update, frames=range(
            0, self.all_frame + 1), interval=200, repeat=True)

        self.fig.canvas.draw()

    def onMousePress(self, event):
        if event.inaxes:
            if event.button is MouseButton.LEFT:
                if self.model == "darw_A":
                    self.polygon_A.points.append(
                        Point(event.xdata, event.ydata))
                    self.drawPolygon()
                elif self.model == "darw_B":
                    self.polygon_B.points.append(
                        Point(event.xdata, event.ydata))
                    self.drawPolygon()
                elif self.model == "darw_C":
                    pass

    def onMouseMove(self, event):
        if event.inaxes:
            if self.model == "darw_A":
                if len(self.polygon_A.points) > 0:
                    self.polygon_A.points.pop()
                self.polygon_A.points.append(
                    Point(event.xdata, event.ydata))
                self.drawPolygon()
            elif self.model == "darw_B":
                if len(self.polygon_B.points) > 0:
                    self.polygon_B.points.pop()
                self.polygon_B.points.append(
                    Point(event.xdata, event.ydata))
                self.drawPolygon()
            elif self.model == "darw_C":
                pass

    def onKeyPress(self, event):
        if event.key == 'enter':
            if self.model == "darw_A":
                if len(self.polygon_A.points) > 0:
                    self.polygon_A.points.pop()
                self.model = "darw_B"
            elif self.model == "darw_B":
                if len(self.polygon_B.points) > 0:
                    self.polygon_B.points.pop()
                if len(self.polygon_A.points) == 0 or len(self.polygon_A.points) == 0:
                    print("Error: Not draw polygon A or B")
                    self.init()
                if len(self.polygon_A.points) == 1 or len(self.polygon_A.points) == 1:
                    print("Error: Too few points")
                    self.init()
                elif len(self.polygon_A.points) != len(self.polygon_B.points):
                    print("Error: The number of points is not equal")
                    self.init()
                else:
                    self.drawAnimation()
                    self.model = "darw_C"
            elif self.model == "darw_C":
                self.init()
                self.model = "darw_A"

        if event.key == 'backspace':
            if self.model == "darw_A":
                self.polygon_A.points.pop()
                self.drawPolygon()
            elif self.model == "darw_B":
                self.polygon_B.points.pop()
                self.drawPolygon()
            elif self.model == "darw_C":
                pass

        if event.key == ' ':
            if self.model == "darw_C":
                self.animation.save('animation.gif')

    def update(self, frame):
        self.ax.cla()
        self.ax.set_title('Intrinsic Shape Interpolation')
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_xlim(-20, 20)
        self.ax.set_ylim(-20, 20)

        t = frame / self.all_frame
        turtle_C = intrinsicShapeInterpolation(t, self.turtle_A, self.turtle_B)
        polygon_C = turtle2Polygon(turtle_C)
        x_C = [point.x for point in polygon_C.points]
        y_C = [point.y for point in polygon_C.points]

        self.ax.plot(x_C, y_C, marker='o', color='green')
        self.fig.canvas.draw()
