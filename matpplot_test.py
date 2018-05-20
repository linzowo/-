 #_*_ coding: utf_8 _*_
import matplotlib.pyplot as plt

from die import Die

die_1 = Die()
die_2 = Die()

#掷骰子的结果
roll_times = 100000
results = [die_1.roll()+die_2.roll() for roll_num in range(roll_times)]

#统计结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(1,max_result+1)]

#x轴标签
x_label = [value for value in range(1,max_result+1)]

#plt.scatter(x_label,frequencies,c=frequencies,cmap=plt.cm.Reds,
#            edgecolors='none',s=15)

#plt.plot(x_label,frequencies,linewidth=10)

plt.bar(x_label,frequencies,color='r')

plt.title('Results of Rolling two D6 '+str(roll_times)+' times.')
plt.xlabel('Value',fontsize=14)
plt.ylabel('Frequency of results',fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()
