import csv
from datetime import datetime

import matplotlib.pyplot as plt


def get_weather(file, dates, highs, lows, date_index, high_index, low_index):
    with open(file) as x:
        reader = csv.reader(x)
        header_row = next(reader)

        for row in reader:
            converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print("Missing data for", converted_date)
            else:
                dates.append(converted_date)
                highs.append(high)
                lows.append(low)


# Sitka Weather
file = "sitka_weather_2018_simple.csv"

dates = []
highs = []
lows = []

get_weather(file, dates, highs, lows, date_index=2, high_index=5, low_index=6)

# Plot Sitka
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle(
    "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
    + "\n"
    + "SITKA AIRPORT, AK US"
)
ax1.plot(dates, highs, c="red", alpha=0.5)
ax1.plot(dates, lows, c="blue", alpha=0.5)
ax1.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


# Death Valley Weather
file = "death_valley_2018_simple.csv"

dates = []
highs = []
lows = []

get_weather(file, dates, highs, lows, date_index=2, high_index=4, low_index=5)

# Plot Death Valley
ax2.plot(dates, highs, c="red", alpha=0.5)
ax2.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.title("DEATH VALLEY, CA US", fontsize=12)
plt.ylim(30, 130)

# Format Overall Plot
plt.xlabel("", fontsize=12)
plt.tick_params(axis="both", labelsize=12)
fig.autofmt_xdate()

# Graph
plt.show()
