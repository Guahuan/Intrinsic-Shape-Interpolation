import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle(self, other):
        return math.acos(self.dot(other) / (self.norm() * other.norm()))

    # 有向夹角
    def angle_signed(self, other):
        return math.atan2(self.cross(other), self.dot(other))


class Polygon:
    # 点按照从左下角、顺时针方向保存
    def __init__(self, points: list):
        self.points = points

    def __repr__(self):
        return f"Polygon({self.points})"

    def __str__(self):
        return f"{self.points}"


class Turtle:
    def __init__(self, p_0: Point, theta: list, L: list):
        self.p_0 = p_0
        self.theta = theta
        self.L = L

    def __repr__(self):
        return f"Turtle({self.p_0}, {self.theta}, {self.L})"

    def __str__(self):
        return f"{self.p_0}, {self.theta}, {self.L}"
