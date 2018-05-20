#_*_ coding: utf_8 _*_
import pygal
from die import Die

die = Die()

#生成投掷结果
results=[]
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#统计结果分布情况
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果可视化
hist = pygal.Bar()

hist.title = "Results of Rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

#print frequencies