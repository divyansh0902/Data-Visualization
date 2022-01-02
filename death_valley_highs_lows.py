import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], [] #created 3 empty list
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')#convert data containing date info (row[2]) to a datetime object
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#plot high temp
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha= 0.5) #alpha controls color's transparency, red line appear lighter
ax.plot(dates, lows, c='blue', alpha = 0.5) #alpha controls color's transparency, blue line appear lighter
plt.fill_between(dates, highs,lows, facecolor= 'blue', alpha = 0.1) #facecolr determines color of shaded region

#format plot
plt.title("Daily high and low temperarure, 2018\nDeath Valley", fontsize=20)
plt.xlabel("" , fontsize=16)
fig.autofmt_xdate() 
plt.ylabel("Temperature(F)", fontsize= 16)
plt.tick_params(axis='both', which= 'major', labelsize= 16)

plt.show()

