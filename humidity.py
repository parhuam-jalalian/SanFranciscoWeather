"""San Francisco's humidity module"""

import csv
import io
from datetime import datetime
from matplotlib import pyplot as plt


def print_all_humidity() -> None:
    """Print all San Francisco's Temperatures min to max
    ranging from 1948 to 2015, information recieved from csv file"""
    filename = "sanfrancisco.csv"

    # (io.open) Py2/3 compatible, RAM optimization
    with io.open(filename, encoding="utf8") as f_obj:
        reader = csv.reader(f_obj)
        next(reader)

        date_list, max_humidity, min_humidity = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[1], "%Y-%m-%d")
            try:
                max_ = int(row[8])
                min_ = int(row[10])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                date_list.append(current_date)
                max_humidity.append(max_)
                min_humidity.append(min_)

    # Plot max and low temperatures.
    plt.style.use("classic")
    fig, axl = plt.subplots()
    axl.plot(date_list, max_humidity, c="red", alpha=0.7)
    axl.plot(date_list, min_humidity, c="blue", alpha=0.7)

    # Format plot.
    title = "Daily Min/Max Humidity - 1948 - 2015\nSan Francisco, CA"
    plt.title(title, fontsize=20)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Humidity (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()
