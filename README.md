# SanFranciscoWeather
A program that utilizes matplotlib to create a graph using data taken from a csv file.
Csv file scrapped from Weather Underground. Csv data is based on San Francisco's Weather.
What to do differently:
   More menu options for User to use to get specific time frames rather than print all data points and manually zoom in.
   Being more time and memory efficient:
    -Using a generator function to process rows from the csv files, filter data, and plot them. 
    -Using NumPy arrays to handle large types of data. (Super Fast)
    <br />-Using Pandas to read CSV file (to manipulate large csv files)
  

