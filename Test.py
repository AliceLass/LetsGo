import autolib
import velib
import Itinerary
import ItineraryDispatch
import Point
import requests
import MetaItinerary
import Exemple


depart=Point.Point()
depart.FromAddress("5 place du cardinal Amette")

Meta=MetaItinerary.MetaItinerary(Exemple.OriginExemple,Exemple.ArrivalExemple)
print(Meta.min_durationAT())

