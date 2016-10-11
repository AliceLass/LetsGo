# -*-coding:Utf-8 -*

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
    chaine='http://opendata.paris.fr/api/records/1.0/search/?dataset=stations_et_espaces_autolib_de_la_metropole_parisienne&facet=ville&facet=type&facet=cp&refine.ville=Paris&geofilter.distance='+str(point.longitude)+'%2C+'+str(point.latitude)+'%2C'+str(d)
    return chaine

#Retourne le JSON avec les stations autolib correspondant à URL
def get_autolib(point,d):
    return requests.get(_url(point,d))

def autolib(point,d):
    autolib_json=get_autolib(point,d).json()
    dmin = int(d)
    station_min = []

    for i in range(0, int(autolib_json['nhits'])):
        if int(autolib_json['records'][i]['fields']['dist']) < dmin:
            dmin = int(autolib_json['records'][i]['fields']['dist'])
            station_min = autolib_json['records'][i]['fields']['xy']
        else:
            i += 1
    return station_min