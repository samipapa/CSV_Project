import csv
from datetime import datetime

import matplotlib.pyplot as plt

open_file = open("sitka_weather_2018_simple.csv", "r")
open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
print(type(header_row))

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)
    print(index, column_header)

highs = []
dates = []
lows = []

for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print("Missing data for {converted_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)


fig, ax = plt.subplots(2, 2)
fig = plt.figure()
ax.plot(dates, highs, c="red")
ax.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.show()
plt.title("Daily high and low temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

plt.show()
####
# fig = plt.figure()

# plt.plot(dates, highs, c="red")
# plt.plot(dates, lows, c="blue")

# fig.autofmt_xdate()

# plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# plt.title("Daily high and low temperatures - 2018", fontsize=16)
# plt.xlabel("", fontsize=12)
# plt.ylabel("Temperature (F)", fontsize=12)
# plt.tick_params(axis="both", labelsize=12)

# fig, ax = plt.subplots(2, 2)

# ax[0].plot(dates, highs, c="red")
# ax[1].plot(dates, lows, c="blue")

# plt.show()
