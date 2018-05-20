#_*_ coding:utf_8 _*_

import csv
from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获取最高气温
#获取锡特卡的数据
filename_1 = 'sitka_weather_2014.csv'
with open(filename_1) as f_1:
        reader = csv.reader(f_1)
        header_row = next(reader)
        
        dates_1,highs_1,lows_1 = [],[],[]
        for row in reader:
            try:
                current_date = datetime.strptime(row[0],'%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print current_date,'missing date'
            else:
                dates_1.append(current_date)
                highs_1.append(high)
                lows_1.append(low)

#获取死亡谷的数据
filename_2 = 'death_valley_2014.csv'
with open(filename_2) as f_2:
        reader = csv.reader(f_2)
        header_row = next(reader)
        
        dates_2,highs_2,lows_2 = [],[],[]
        for row in reader:
            try:
                current_date = datetime.strptime(row[0],'%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print current_date,'missing date'
            else:
                dates_2.append(current_date)
                highs_2.append(high)
                lows_2.append(low)

#根据数据绘制图形                

#通用设置
y_locks = [i*10 for i in range(1,13)]
fig = plt.figure(dpi=80,figsize=(10,6))

#加载数据1
plt.plot(dates_1,highs_1,c='red',alpha=0.5)
plt.plot(dates_1,lows_1,c='blue',alpha=0.5)

#加载数据2
plt.plot(dates_2,highs_2,c='y',alpha=0.5)
plt.plot(dates_2,lows_2,c='g',alpha=0.5)

#控制数据1和2之间的区域显示颜色
plt.fill_between(dates_1,highs_1,lows_1,facecolor='blue',alpha=0.1)
plt.fill_between(dates_2,highs_2,lows_2,facecolor='red',alpha=0.1)

plt.ylim(10,120) #设置y轴的取值范围
plt.yticks(y_locks) #设置y轴的刻度

#设置图形格式
plt.title('Daily high and low temperatures - 2014\nDeath Valley',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate() #绘制一个斜的标签
plt.ylabel("Temperature (F)",fontsize=16)

plt.show()
