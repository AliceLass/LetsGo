"""Module permettant de trouver la station autolib la plus proche en prenant en entrée un pointde la classe Point"""

import Point
import requests
import json
import pprint
from lxml import etree
from geopy.distance import vincenty





#Créer l'URL avec les coordonnées GPS long,lat et une distance d
def _url(point):
    d=500
    chaine='http://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel&facet=banking&facet=bonus&facet=status&facet=contract_name&geofilter.distance='+str(point.latitude)+'%2C+'+str(point.longitude)+'%2C'+str(d)

    return chaine

#Retourne le JSON avec les stations autolib correspondant à URL
def get_velib(point):
    return requests.get(_url(point))

#Va chercher la station la plus proche et ses coordonnées dans le JSON
def velib(point):
    velib_json=get_velib(point).json()
    dmin = 500
    station_min = []

    for i in range(0, int(velib_json['nhits'])):
        if vincenty(velib_json['records'][i]['fields']['position'],point.printcoordinates()).meters < dmin:
            dmin = vincenty(velib_json['records'][i]['fields']['position'],point.printcoordinates()).meters
            station_min = velib_json['records'][i]['fields']['position']

        else:
            i += 1
    return station_min