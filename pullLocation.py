import subprocess, json, requests
class defaultLocation:
    #return space
    def getCityName():
            #return city name
            return cityNamed
    def findDefault():
        def pullIp():
            #use subprocess to look up ip address using myip.com, capture text and as value            
            global ipOutput
            ip = subprocess.run("nslookup myip.opendns.com. resolver1.opendns.com", shell=True,text =True,capture_output=True)
            #strip all extra chars and return the IP 
            ipOutput = ip.stdout.split(" ")[2].strip("\n")
            return ipOutput
        #call pullIp
        pullIp()
        ##using ip.com to return ip attributes: cityName, Lat Long 
        ipInfo = requests.get(f"http://ip-api.com/json/{ipOutput}")
        ipInfoJson = json.loads(ipInfo.text)
        
        #pull lat nlong, and cityName
        global cityNamed
        cityNamed = ipInfoJson["city"]
        lat = ipInfoJson["lat"]
        lon = ipInfoJson["lon"]
        #format and return
        cords = f"{lat},{lon}"
        return cords  
