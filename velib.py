"""Module permettant de trouver la station autolib la plus proche en prenant en entrée un pointde la classe Point"""

import Point
import requests
import json
import pprint
from lxml import etree

#Rayon du périmètre maximal dans lequel on recherche
d=500

#Créer l'URL avec les coordonnées GPS long,lat et une distance d
def _url(point,d):
    chaine='http://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel&facet=banking&facet=bonus&facet=status&facet=contract_name&geofilter.distance='+str(point.longitude)+'%2C+'+str(point.latitude)+'%2C'+str(d)

    return chaine

#Retourne le JSON avec les stations autolib correspondant à URL
def get_velib(point,d):
    return requests.get(_url(point,d))

#Va chercher la station la plus proche et ses coordonnées dans le JSON
def velib(point,d):
    velib_json=get_velib(point,d).json()
    dmin = int(d)
    station_min = []

    for i in range(0, int(velib_json['nhits'])):
        if int(velib_json['records'][i]['fields']['dist']) < dmin:
            dmin = int(velib_json['records'][i]['fields']['dist'])
            station_min = velib_json['records'][i]['fields']['xy']
        else:
            i += 1
    return station_min