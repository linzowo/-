#_*_ coding:utf_8 _*_
import matplotlib.pyplot as plt

#squares = [1,4,9,16,25]
#input_value =[1,2,3,4,5]
#plt.plot(input_value,squares,linewidth=5)  #linewidth控制线段的宽度

#plt.title('Square Numbers',fontsize=24) #绘制标题，设置宽度
#plt.xlabel('Value',fontsize=14)  #设置x轴的标题和字体大小
#plt.ylabel('Square of Value',fontsize=14) #设置y轴的标题和大小

#plt.tick_params(axis='both',labelsize=14) #影响坐标轴上的刻度，设置坐标轴的字体大小

#plt.show()

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,edgecolors='none',s=40)

plt.title('Cube Numbers',24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Cube of Value',fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,5100,0,135000000000])
plt.show()