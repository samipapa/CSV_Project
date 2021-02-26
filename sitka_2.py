import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))
# The enumerate() function returns both the index of each item and
# the value of each item as you loop through a list.

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)
    print(index, column_header)

highs = []
dates = []


# An example
# mydate = "2018-07-01"
# converted_date = datetime.strptime(mydate, "%Y-%m-%d")
# print(converted_date)

# We call the method strptime() using the string containing the dataa we want to work with
# as its first argument. The second argument tells Python how the date is formatted.
# In this example, Python interprets "%Y-" to mean the part of the string before the first
# dash is a four-digit year; "%m-" means the part of the string before the second dash is
# the number representing the month; and "%d-" means the last part of te string is the day of
# the month from 1 to 31.

for row in csv_file:
    highs.append(int(row[5]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)

# print(highs)

# Plot highs on a chart

import matplotlib.pyplot as plt

# Matplotlib's pyplot API has a convenience function called subplots() which acts as a
# utility wrapper and helps in creating common layouts of subplots, including the
# enclosing figure object, in a single cell.

# ax = plt.subplots()

fig = plt.figure()


plt.plot(dates, highs, c="red")

# The cell to fig.autofmt_xdate() draws the date labels diagonally to prevent them from
# overlapping.

fig.autofmt_xdate()

plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)


plt.show()
