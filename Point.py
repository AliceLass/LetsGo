import geopy
from geopy.geocoders import Nominatim

class Point:
"Classe contenant les coordonées des points"
	def __init__(self,address):
		self.location=geolocator.geocode(str(address))
		self.latitude=self.location.latitude
		self.longitude=self.location.longitude
		self.coordinates=(self.latitude,self.longitude)
		
	def printcoordinates(self):
		return((self.latitude,self.longitude))
	
	def disttocoordinates(self,dist):
		return((self.latitude,self.longitude,dist))
	
		

	
