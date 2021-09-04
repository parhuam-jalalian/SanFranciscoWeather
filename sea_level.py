"""San Francisco's sea level module"""

import csv
import io
from datetime import datetime
from matplotlib import pyplot as plt


def print_all_sea_level() -> None:
    """Print all San Francisco's Sea levels min to max
    ranging from 1948 to 2015, information recieved from csv file"""
    filename = "sanfrancisco.csv"

    # (io.open) Py2/3 compatible, RAM optimization
    with io.open(filename, encoding="utf8") as f_obj:
        reader = csv.reader(f_obj)
        next(reader)

        date_list, max_sea_levels, min_sea_levels = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[1], "%Y-%m-%d")
            try:
                max_ = float(row[11])
                min_ = float(row[13])
            except ValueError:
                # Commented out, too much data mising for sea level
                print(f"Missing data for {current_date}")
                # pass
            else:
                date_list.append(current_date)
                max_sea_levels.append(max_)
                min_sea_levels.append(min_)

    # Plot max and low sea levels.
    plt.style.use("classic")
    fig, axl = plt.subplots()
    axl.plot(date_list, max_sea_levels, c="red", alpha=0.7)
    axl.plot(date_list, min_sea_levels, c="blue", alpha=0.7)

    # Format plot.
    title = "Daily Min/Max Sea Levels - 1948 - 2015\nSan Francisco, CA"
    plt.title(title, fontsize=20)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Sea level (mm)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()
