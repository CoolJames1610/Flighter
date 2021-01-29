import json
from haversine import haversine, Unit

with open("Flighter/airports.json", "r") as f:
  data = json.load(f)

class Flighter:
  def __init__(self, plane=None, speed=0, icao1=None, icao2=None):
    self.plane = plane
    self.speed = speed
    self.icao1 = icao1
    self.icao2 = icao2
  
  def __str__(self):
    return f"Plane: {self._plane}\nSpeed: {self._speed}\nICAO1 (dep airport): {self._icao1}\nICAO2 (arv airport): {self._icao2}"


  @property
  def plane(self):
    return self._plane
  
  @plane.setter
  def plane(self, plane):
    self._plane = plane
  
  @property
  def speed(self):
    return self._speed
  
  @speed.setter
  def speed(self, speed):
    self._speed = speed
  
  @property
  def icao1(self):
    return self._icao1
  
  @icao1.setter
  def icao1(self, icao1):
    self._icao1 = icao1
  
  @property
  def icao2(self):
    return self._icao2
  
  @icao2.setter
  def icao2(self, icao2):
    self._icao2 = icao2

  def __airport(icao):
    i = icao.upper()
    ye = None
    for icao, lat in data.items():
      if icao == i:
        ye = True
        break
      else:
        ye = False
    if ye == True:
      latitiude = (lat["lat"])
      longitude = (lat["lon"])
      xc = (lat["city"])
      city = (latitiude, longitude)
      return city, xc
    else:
      Errors.invalidICAO(i)
  
  def __distance(x, y):
    nm = round((haversine(x, y, unit=Unit.NAUTICAL_MILES)))
    return nm

  def __convert(self, kn, nm):
    hrs = round((nm / kn), 2)
    mins = round(hrs * 60)
    secs = round(mins * 60)
    if mins < 60:
      x = {
          "Flight": f"{self._icao1} to {self._icao2}",
          "Plane": f"{self._plane}",
          "Approx. Speed": f"{self._speed}",
          "Approx. Time": f"{mins} minutes"
          }
      return x
    else:
      x = {
          "Flight": f"{self._icao1} to {self._icao2}",
          "Plane": f"{self._plane}",
          "Approx. Speed": f"{self._speed}",
          "Approx. Time": f"{hrs} hours"
          }
      return x

  def checkICAO(self, icao):
    i = icao.upper()
    ye = None
    for icao, lat in data.items():
      if icao == i:
        ye = True
        break
      else:
        ye = False
    if ye == True:
      return True
    else:
      return False

  def checkIATA(self, iata):
    i = iata.upper()
    ye = None
    for icao, lat in data.items():
      if lat["iata"] == i:
        ye = True
        break
      else:
        ye = False
    if ye == True:
      return True
    else:
      return False

  def checkFlight(self):
    a1, a1n = Flighter.__airport(str(self._icao1))
    a2, a2n = Flighter.__airport(str(self._icao2))
    nm = Flighter.__distance(a1, a2)
    return Flighter.__convert(self, int(self._speed), nm)

  def airportInfo(self, name):
    icao = Flighter.checkICAO(self, name)
    if icao != True:
      iata = Flighter.checkIATA(self, name)
      if iata != True:
        Errors._invalidICAO(name)
      else:
        i = name.upper()
        ye = None
        for icao, lat in data.items():
          if lat["iata"] == i:
            ye = True
            break
        city = (lat["city"])
        name = (lat["name"])
        country = (lat["state"])
        iata = (lat["iata"])
        el = (lat["elevation"])
        latt = (lat["lat"])
        lon = (lat["lon"])
        tz = (lat["tz"])
        x = {
          "Name": f"{name}",
          "Country/State": f"{country}",
          "City": f"{city}",
          "ICAO": f"{icao}",
          "IATA": f"{iata}",
          "Elevation": f"{el}m",
          "Latitude": f"{latt}",
          "Longitude": f"{lon}",
          "Timezone": f"{tz}"
        }
        return x
    else:
      i = name.upper()
      ye = None
      for icao, lat in data.items():
        if icao == i:
          ye = True
          break
      city = (lat["city"])
      name = (lat["name"])
      country = (lat["state"])
      iata = (lat["iata"])
      el = (lat["elevation"])
      latt = (lat["lat"])
      lon = (lat["lon"])
      tz = (lat["tz"])
      x = {
        "Name": f"{name}",
        "Country/State": f"{country}",
        "City": f"{city}",
        "ICAO": f"{icao}",
        "IATA": f"{iata}",
        "Elevation": f"{el}m",
        "Latitude": f"{latt}",
        "Longitude": f"{lon}",
        "Timezone": f"{tz}"
      }
      return x


class Errors(Flighter):

  def _invalidICAO(ICAO):
    yo = False
    class AirportNotFound(Exception): pass
    err = ICAO[0:3]
    for icao, lat in data.items():
      if icao.startswith(err):
        yo = True
        break
      else:
        yo = False
    if yo == True:
      if len(ICAO) != 4:
        raise AirportNotFound(f"'{ICAO}' is an invalid ICAO. ICAO's can only be 4 characters in size. Perhaps you meant '{icao}'?")
      else:
        raise AirportNotFound(f"'{ICAO}' is an invalid ICAO. Perhaps you meant '{icao}'?")
    else:
      if len(ICAO) == 3:
        Errors._invalidIATA(ICAO)
      elif len(ICAO) != 4:
        raise AirportNotFound(f"'{ICAO}' is an invalid ICAO. ICAO's can only be 4 characters in size.")
      else:
        raise AirportNotFound(f"'{ICAO}' is an invalid ICAO.")

  def _invalidIATA(IATA):
    yo = False
    class AirportNotFound(Exception): pass
    err = IATA[0:2]
    for icao, lat in data.items():
      if str(lat["iata"]).startswith(err):
        yo = True
        iata = str(lat["iata"])
        break
      else:
        yo = False
    if yo == True:
      raise AirportNotFound(f"'{IATA}' is an invalid IATA. Perhaps you meant '{iata}'?")
    else:
      raise AirportNotFound(f"'{IATA}' is an invalid IATA.")