# SanFranciscoWeather

A program that utilizes matplotlib to create a graph using data taken from a csv file.

Csv file scrapped from Weather Underground. Csv data is based on San Francisco's Weather 1948-2015.

## What I would do differently next time:
* More menu options for User to use to get specific time frames rather than print all data points and manually zoom in.
* Being more time and memory efficient such as:
* Use a generator function to process rows from the csv file, filter the data, and plot in one go vs storing values in a list then ploting.  
* Use NumPy arrays or array.array to handle large amounts of data for size, functionality, and performance. (Instead of using lists)
* Use Pandas to read and to manipulate large csv file.
  

