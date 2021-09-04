"""San Francisco's temperature module"""

import csv
import io
from datetime import datetime
from matplotlib import pyplot as plt


def print_all_temperature() -> None:
    """Print all San Francisco's Temperatures min to max
    ranging from 1948 to 2015, information recieved from csv file"""
    filename = "sanfrancisco.csv"

    # (io.open) Py2/3 compatible, RAM optimization
    with io.open(filename, encoding="utf8") as f_obj:
        reader = csv.reader(f_obj)
        next(reader)

        date_list, max_temps, min_temps = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[1], "%Y-%m-%d")
            try:
                max_ = int(row[2])
                min_ = int(row[3])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                date_list.append(current_date)
                max_temps.append(max_)
                min_temps.append(min_)

    # Plot max and low temperatures.
    plt.style.use("classic")
    fig, axl = plt.subplots()
    axl.plot(date_list, max_temps, c="red", alpha=0.7)
    axl.plot(date_list, min_temps, c="blue", alpha=0.7)

    # Format plot.
    title = "Daily Min/Max Temperatures - 1948 - 2015\nSan Francisco, CA"
    plt.title(title, fontsize=20)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()
