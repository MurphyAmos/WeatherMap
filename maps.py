import webbrowser, folium
from citiesReader import pullCityData

class mapReturn:
        ##pulling the forecast data: latlong, cityName, temp, forecast, and rain
        pullCityObj = pullCityData
        global latLong
        latLong = pullCityObj.readnReturn()
        global cityName 
        cityName = pullCityObj.returnCity() 
        global temp
        temp = pullCityObj.returnTemp()        
        global forecast
        forecast = pullCityObj.returnForecast()        
        global rain
        rain = pullCityObj.returnRain()

        ###start of making folium map
        global foliumMapHtml
        def makeMap():
            def makeMarker(mapHolder):
                #using HTML to show variables in popup "Marker"
                markerHTML ="""
                    <h1>{firstHeader}</h1>
                    <p>Temp: {temp}
                       Rain: {rain}%
                       forecast: {forecast}                            
                    </p>"""
                #forming Circle in and around city area 
                folium.Circle(
                    #circle features
                    location = latLong,
                    radius = 15000,
                    color = "black",
                    opacity = 1,
                    fill_opacity=.3,
                    fill_color = "green",
                    weight =1,
                    #calling popup
                    popup = markerHTML.format(firstHeader = cityName.upper(), temp = temp, rain = rain, forecast =forecast ),
                ).add_to(mapHolder) #adding map to html holder

            #if all else fails look at texas
            if(bool(latLong)!=True):
                #making folium map at location with bounds
                foliumMapPull = folium.Map(location=[31.968600,-99.901800],
                zoom_start=6,
                max_bounds =True,
                min_lat = (31.968600-20),
                max_lat = (31.968600+20),
                min_lon = (-99.901800+20),
                max_lon = (-99.901800-20),)
            else:       
                #else make a map based upon location pulled from citiesReader
                foliumMapPull = folium.Map(location=(latLong))

            #add maker to map
            makeMarker(foliumMapPull)
            #save folium ap as html file      
            foliumMapPull.save(f"{cityName} Map.html")
            #set foliumMap as something and open it!
            foliumMapHTml = webbrowser.open(f"{cityName} Map.html")
        makeMap()
