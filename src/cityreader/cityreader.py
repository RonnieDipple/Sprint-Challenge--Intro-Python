# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)

#Repr returns a represntation of name, lat, lon
    def __repr__(self):
        return f'city: {self.name} | lat: {self.lat} | long: {self.lon}'


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv


# TODO Implement the functionality to read from the 'cities.csv' file
# For each city record, create a new City instance and add it to the
# `cities` list
def cityreader(cities=[]):
    cities = []
    #was not taught what with open does found it in the magical land of google lol
    with open('cities.csv') as csvfile:# int his case it is opening csv
        readCSV = csv.reader(csvfile, delimiter=',') #it is comma seperating everything to make it readable
        next(readCSV)#was not taught about next essentially it just calls next as in move on repeatedly, in short it iterates through the file
        for field in readCSV:#Usual for loop shennanigans
            cities.append(City(field[0], field[3], field[4]))#adds what is in the file to the cities list
    return cities #returns the list


cities = cityreader() #instantiates the function cityreader so we get a nice terminal print out


 #Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []#empty list
    lat = [min(lat1, lat2), max(lat1, lat2)]#takes the min and max lat
    lon = [min(lon1, lon2), max(lon1, lon2)]#takes the min and max lon
    for city in cities:
        # so if the city's lat is greater or equal to the lat in the 0 postion above
        # and city lat is below or equal to the lat in the 1 position above
        # and city lon is above or equal to the lon in position 0 above
        # and city lon is below the lon in position 1 above
        # it then adds that city to the empty list
        if city.lat >= lat[0] and city.lat <= lat[1] and city.lon >= lon[0] and city.lon <= lon[1]:
            within.append(city)

    #need a float check
    # Go through each city and check to see if it falls within
    # the specified coordinates.

    return within
