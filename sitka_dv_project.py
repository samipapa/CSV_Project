def main():
    # Imports
    import csv
    from matplotlib import pyplot as plt
    from datetime import datetime

    # Open and read Sitka file
    filename = open("sitka_weather_2018_simple.csv", "r")
    place_name = ""

    reader = csv.reader(filename, delimiter=",")
    header_row = next(reader)
    print(header_row)

    # Indexes for Sitka
    date_index = header_row.index("DATE")
    high_index = header_row.index("TMAX")
    low_index = header_row.index("TMIN")
    name_index = header_row.index("NAME")

    # Get dates, highs, and lows
    dates = []
    highs = []
    lows = []

    for row in reader:
        # Get the place name
        if not place_name:
            place_name = str(row[name_index])
            print(place_name)
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        except ValueError:
            print("Missing data for" + converted_date)

        else:
            highs.append(high)
            dates.append(converted_date)
            lows.append(low)

    fig, a = plt.subplots(2, 1)

    # Plot Sitka
    a[0].set_title(place_name)
    a[0].plot(dates, highs, c="red")
    a[0].plot(dates, lows, c="blue")
    a[0].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    # Open and read Death Valley file
    filename = open("death_valley_2018_simple.csv", "r")
    place_name2 = ""

    reader = csv.reader(filename, delimiter=",")
    header_row = next(reader)
    print(header_row)

    # Indexes for Sitka
    date_index = header_row.index("DATE")
    high_index = header_row.index("TMAX")
    low_index = header_row.index("TMIN")
    name_index = header_row.index("NAME")

    # Get dates, highs, and lows
    dates = []
    highs = []
    lows = []

    for row in reader:
        # Get the place name
        if not place_name2:
            place_name2 = str(row[name_index])
            print(place_name2)
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        except ValueError:
            print("Missing data for", converted_date)

        else:
            highs.append(high)
            dates.append(converted_date)
            lows.append(low)

    # Plot Death Valley
    a[1].set_title(place_name2)
    a[1].plot(dates, highs, c="red")
    a[1].plot(dates, lows, c="blue")
    a[1].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    # Format the overall graph
    fig.suptitle("Temperature Comparison Between " + place_name + " and " + place_name2)
    plt.xlabel("", fontsize=12)
    plt.tick_params(axis="both", labelsize=12)
    fig.autofmt_xdate()

    # Show the graph
    plt.show()


# Call the main function
main()