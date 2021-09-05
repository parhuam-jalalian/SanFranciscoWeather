# SanFranciscoWeather
A program that utilizes matplotlib to create a graph using data taken from a csv file.
<br />Csv file scrapped from Weather Underground. Csv data is based on San Francisco's Weather 1948-2015.
<br />**What to do differently**:
  <br /> More menu options for User to use to get specific time frames rather than print all data points and manually zoom in.
  <br /> Being more time and memory efficient:
   <br /> -Using a generator function to process rows from the csv files, filter data, and plot them. 
<br />-Using NumPy arrays to handle large types of data. (Super Fast)
<br />-Using Pandas to read CSV file (to manipulate large csv files)
  

