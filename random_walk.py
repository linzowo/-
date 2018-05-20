#_*_ coding:utf_8 _*_

from random import choice

class RandomWalk(object):
    """随机漫步的类"""
    def __init__(self,num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步生成的所有的点"""
        while len(self.x_values) < self.num_points:
            #生成移动方向和距离
            x_step = self.get_step()
            y_step = self.get_step()

            #保证不停留在原地
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个 x 和 y 值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([-1,1])
        distance = choice([0,1,2,3,4])
        step= direction * distance
        return step
