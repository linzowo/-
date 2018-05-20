#_*_ coding: utf_8 _*_
import pygal
from die import Die

die_1 = Die()
die_2 = Die()

#生成投掷结果
#result = die_1.roll() + die_2.roll()
results = [die_1.roll() * die_2.roll() for roll_num in range(50000)]

#统计结果分布情况
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1,max_result+1)
               if results.count(value) != 0]
labels = [str(value) for value in range(1,max_result+1) if results.count(value) != 0]

#对结果可视化
hist = pygal.Bar()

hist.title = "Results of Rolling a D6 and a D10 50,000 times."
hist.x_labels = labels
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6',frequencies)
hist.render_to_file('dice_visual.svg')

