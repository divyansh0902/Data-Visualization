import csv 
import matplotlib.pyplot as plt
from datetime import datetime

#filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) #reader object processes first line of csv in file and stores each as an item in a list
    header_row = next(reader) #csv module contains next() func which returns next line in file when passed resder object

    #get dates and high temp from list
    dates, highs = [], [] #created 2 empty list
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')#convert data containing date info (row[2]) to a datetime object
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

#plot high temp
plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.plot(highs, c='red')
ax.plot(dates, highs, c='red') #pass dates and high temp values to plot()

#format plot
plt.title("Daily high temperarure, 2018", fontsize=24)
plt.xlabel("" , fontsize=16)
fig.autofmt_xdate() #call to it draws date labels diagonally to prevent them from overlapping
plt.ylabel("Temperature(F)", fontsize= 16)
plt.tick_params(axis='both', which= 'major', labelsize= 16)

plt.show()










#print(highs)

    #for index, column_header in enumerate(header_row): 
     #   print(index, column_header)































