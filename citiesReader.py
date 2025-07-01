import csv
import json, requests, time
from pullLocation import *
class pullCityData:
    #return space for calling later
    def returnCity():
        return cityName
    def returnTemp():
        return temperatureAfternoon
    def returnForecast():
        return shortForecastAfternoon
    def returnRain():
        return percipChance

   
    #location variables    
    global stateName, cityName, countyName
    stateName =str(input("\tState: "))    
    cityName =str(input("\tCity: "))
    countyName =str(input("\tCounty:"))
    def readnReturn():  
        global defaultCity 
        global cityName
        #open the csv.. if it doesnt open found is equal to true
        found  = False
        with open('us_cities.csv','r') as f:
            reader = csv.reader(f)
            for i in reader:
                #making latitude and longitude values in string and tuple(?) value
                global latnLong 
                global latnLongArray
                #identify index
                stateIndex = i[2]
                cityIndex = i[3]
                countyIndex = i[4]
                lata = i[5]
                longa =i[6]
                #if found set lat n long and make found true
                if(stateIndex.lower() == stateName.lower()  and (cityIndex.lower() == cityName.lower()) and countyIndex.lower() == countyName.lower()):
                    latnLong = (f"{float(lata)},{float(longa)}")
                    latnLongArray  = [float(lata),float(longa)]
                    found = True
                    return(latnLongArray)
        #if not found in file then make default city obj and find long and lat of users computer
        if not found:
            defaultCity = defaultLocation.findDefault()
            latnLong = defaultCity.strip("'")
            latNlongArray = [float(i) for i in defaultCity.split(",")]
            cityName = defaultLocation.getCityName()
        return latNlongArray 
           
    def forecastPull():
        def pullGrid(latNlong):
	    #pulling grid points and returning them
            gridInfo=requests.get(f"https://api.weather.gov/points/{latNlong}")
            gridInfoJson = json.loads(gridInfo.text)
            gridXPoint=gridInfoJson["properties"]["gridX"]
            gridYPoint=gridInfoJson["properties"]["gridY"]
            gridXnY = (f"{gridXPoint},{gridYPoint}")
            return gridXnY
        gridPoints =pullGrid(latnLong)
        #request the JSON; grid and office are static for Houston texas
        forecastInfo=requests.get(f"https://api.weather.gov/gridpoints/HGX/{gridPoints}/forecast")
        #turn it in to text
        forecastInfoJson = json.loads(forecastInfo.text)
	#might make variables and hold them or just directly pull them in text message sender thingy	

	###in this half of the function i will hold the info in some global variables
        global temperatureAfternoon
        global shortForecastAfternoon
        global percipChance
        
	#here we are just using json and oulling the temp,short forecast, and rain%
	#yes this is hard to read, but i dont really care as it wont change 
        temperatureAfternoon = forecastInfoJson["properties"]["periods"][0]["temperature"]
        shortForecastAfternoon= forecastInfoJson["properties"]["periods"][0]["shortForecast"]
        percipChance = forecastInfoJson["properties"]["periods"][0]["probabilityOfPrecipitation"]["value"]
        ####end of forecastPull()
    readnReturn()
    forecastPull()
