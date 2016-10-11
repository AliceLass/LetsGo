import os
os.chdir("D:/Documents/Centrale/3A/OSY/PA/LetsGo")

import autolib
import velib
import Itinerary
import ItineraryDispatch
import Point



depart=Point.Point()
depart.FromAddress("5 place du cardinal Amette")

print(depart.printcoordinates())
print(depart.latitude,depart.longitude)

print(velib.velib(depart))
print(autolib.autolib(depart))


