import csv
from matplotlib import pyplot as plt
from datetime import datetime

def get_weather_data(filename, dates, highs, lows):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
                
            except ValueError:
                print(current_date, "missing data")
                
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
                
fig = plt.figure(dpi=128, figsize=(10, 6))

filename = 'death_valley_2014.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows)
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.5)

filename = 'sitka_weather_2014.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows)
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.5)

plt.title("Daily high and low temperatures - 2014\nDeath Valley - Sitka, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.ylim()

plt.show()