# -*-coding:Utf-8 -*

import Itinerary
import velib
import autolib
import Point

class ItineraryAutolib:
	def __init__(self,Origin,Arrival):
	#On definit les points intermediaires
		self.StationOrigin=Point()
		self.StationOrigin.FromCoord(autolib(Origin))
		self.StationArrival=Point()
		self.StationArrival.FromCoord(autolib(Arrival))
		#On crée les 3 itineraires
		self.WalkToStation=Itinerary(Origin,StationOrigin,walking)
		self.Driving=Itinerary(StationOrigin,StationArrival,driving)
		self.WalkToArrival=Itinerary(StationArrival,Arrival,walking)
		self.walking_duration=self.WalkToStation.duration+self.WalkToArrival.duration
		self.duration=self.WalkToStation.duration+self.Driving.duration+self.WalkToArrival.duration
		
	def DispatchDuration(self):
	#envoie le dispatch des temps de transit sous forme d'une liste.
		Walking1=self.WalkToStation.duration
		Walking1=Walking1//60
		Walking2=self.WalkToArrival.duration
		Walking2=Walking1//60
		DriveDuration=self.Driving.duration
		DriveDuration=DriveDuration//60
		return[Walking1,DriveDuration,Walking2]
		
class ItineraryVelib:
	def __init__(self,Origin,Arrival):
	#On definit les points intermediaires
		self.StationOrigin=Point()
		self.StationOrigin.FromCoord(velib(Origin))
		self.StationArrival=Point()
		self.StationArrival.FromCoord(velib(Arrival))
		#On crée les 3 itineraires
		self.WalkToStation=Itinerary(Origin,StationOrigin,walking)
		self.Biking=Itinerary(StationOrigin,StationArrival,bicycling)
		self.WalkToArrival=Itinerary(StationArrival,Arrival,walking)
		self.walking_duration=self.WalkToStation.duration+self.WalkToArrival.duration
		self.duration=self.WalkToStation.duration+self.Biking.duration+self.WalkToArrival.duration
		
	def DispatchDuration(self):
	#envoie le dispatch des temps de transit sous forme d'une liste.
		Walking1=self.WalkToStation.duration
		Walking1=Walking1//60
		Walking2=self.WalkToArrival.duration
		Walking2=Walking1//60
		BikeDuration=self.Drive.duration
		BikeDuration=DriveDuration//60
		return[Walking1,BikeDuration,Walking2]
		
class ItineraryWalk:
	def __init__(self,Origin,Arrival):
		self.WalkToArrival=Itinerary(Origin,Arrival,walking)
		self.walking_duration=self.WalkToArrival.duration
		self.duration=self.WalkToArrival.duration
		
	def DispatchDuration(self):
	#envoie le dispatch des temps de transit sous forme d'une liste.
		Walking1=self.WalkToStation.duration
		Walking1=Walking1//60
		return[Walking1]
		
class ItineraryTransit:
	def __init__(self,Origin,Arrival):
		self.Transit=Itinerary(Origin,Arrival,transit)
		steps=self.Transit.itinerary["routes"][0]["legs"][0]["steps"]
		self.walking_duration=0
		self.transit_duration=0
		self.nb_liaisons=-1
		for i in steps:
			if i["travel_mode"]=="WALKING":
				self.walking_duration+=i["duration"]
			elif i["travel_mode"]=="TRANSIT":
				self.transit_duration+=i["duration"]
				self.nb_liaisons+=1
		self.duration=self.Transit.duration
		
	def DispatchDuration(self):
	#envoie le dispatch des temps de transit sous forme d'une liste.
		return([self.walking_duration//60,self.transit_duration//60])