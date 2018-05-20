#_*_ coding:utf_8 _*_

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.figure(dpi=100,figsize=(12,6))  #调整表格视图大小

    point_numbers = list(range(rw.num_points))
    #plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
                #edgecolors='none',s=1)
    plt.plot(rw.x_values,rw.y_values,linewidth=1)

    #设置起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #隐藏xy轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = raw_input('Make another walk?(y/n):')
    if keep_running == 'n':
        break
