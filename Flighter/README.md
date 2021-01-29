# Flighter 

Flighter is an easy-to-use Python module that allows users to explore aviation using Python
Features include: flight time from airport A to airport B; full functionality for both ICAO and IATA codes ; checks whether a particular airport exists per ICAO/IATA; airport details per ICAO/IATA. 
Data is returned in a json format, so extracting data has never been easier!

***

#### Version 1.0.0
> Module released

***

### Installation
```
pip install Flighter
```

### Quickstart
You can initialise the attributes directly via Flighter:
```py
from Flighter import Flighter
x = Flighter(
  plane="F18",
  speed=1000,
  icao1="EGLL",
  icao2="LFPG"
)
print(x.checkFlight())

# Returns in a json format with:
# Flight, Plane, Approx. Speed, Approx. Time (in mins or hrs)
```
Or, by initialising them one by one:
```py
from Flighter import Flighter
x = Flighter()
x.plane = "F18"  # Defualt=None
x.speed = 1000   # Default=0
x.icao1 = "EGLL" # Default=None
x.icao2 = "LFPG" # Default=None
print(x.checkFlight())

# Returns in a json format with:
# Flight, Plane, Approx. Speed, Approx. Time (in mins or hrs)
```
You can also check whether an ICAO or IATA exists:
```py
from Flighter import Flighter
x = Flighter()
print(x.checkICAO("EGLL"))
print(x.checkIATA("LHR"))

# Returns True or False
```
And by using an ICAO or IATA, you can find out an airport's details
```py
from Flighter import Flighter
x = Flighter()
print(x.airportInfo("EGLL")) #or print(x.airportInfo("LHR"))

# Returns in a json format with:
# Name, Country/State, City, ICAO, IATA (if it has one), Elevation, Latitude, Longitude and Timezone
```

***

### Contributing
You can open a PR on Github :D

### Help
You can [email me](https://mail.google.com/mail/u/1/#inbox?compose=GTvVlcSGLrTGkHMrJKfHBhNsdmbbBGPSqMcrQgNQSDQtLQfSKQzxLNHhpzzDrpGrjWcgrMNSgSDGg) or send a friend request via Discord to Zeliktric#4282.

Thank you! :D