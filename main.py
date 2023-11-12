from IntrinsicShapeInterpolation import *
from TurtleGeometry import *
from Struct import *
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation


polygon_A = Polygon([Point(0, 0), Point(0, 1),
                    Point(1, 1), Point(1, 0)])
turtle_A = polygon2Turtle(polygon_A)
polygon_B = Polygon([Point(0, 0.5), Point(0.5, 1),
                    Point(1, 0.5), Point(0.5, 0)])
turtle_B = polygon2Turtle(polygon_B)


# # 提取点的坐标
# x_values = [point.x for point in polygon_A.points]
# y_values = [point.y for point in polygon_A.points]

# # 创建散点图
# fig, ax = plt.subplots()
# scatter = ax.scatter(x_values, y_values, c='blue', marker='o', label='Points')
# ax.set_title('Dynamic Scatter Plot of 2D Points')
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.legend()

# # 初始坐标范围
# initial_xlim = ax.get_xlim()
# initial_ylim = ax.get_ylim()

# # 更新函数，用于每一帧的数据更新


# def update(frame):
#     t = frame / 10
#     turtle_C = intrinsicShapeInterpolation(t, turtle_A, turtle_B)
#     polygon_C = turtle2Polygon(turtle_C)
#     # 提取点的坐标
#     x = [point.x for point in polygon_C.points]
#     y = [point.y for point in polygon_C.points]
#     scatter.set_offsets(list(zip(x, y)))

#     # 扩大坐标系的视野
#     ax.set_xlim(initial_xlim[0] - 5, initial_xlim[1] + 5)
#     ax.set_ylim(initial_ylim[0] - 5, initial_ylim[1] + 5)


# # 创建动画
# animation = FuncAnimation(fig, update, frames=range(
#     1, 10), interval=100, repeat=True)

# # 显示动画
# plt.show()
