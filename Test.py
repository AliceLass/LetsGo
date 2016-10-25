import ItineraryDispatch
import Point


#print(Exemple.OriginExemple.coordinates)

#IT=ItineraryDispatch.ItineraryTransit(Exemple.OriginExemple,Exemple.ArrivalExemple)
#print(IT.Transit.itinerary)
#steps=[]
#for i in IT.Transit.itinerary["routes"][0]["legs"][0]["steps"]:
#    if i['travel_mode']=="TRANSIT":
#        step={}
#        step['departure_stop']=i['transit_details']['departure_stop']['name']
#        step['line']=i['transit_details']['line']['short_name']
#        step['direction']=i['transit_details']['headsign']
#        step['type']=i['transit_details']['line']['vehicle']['name']
#        step['arrival_stop']=i['transit_details']['arrival_stop']['name']
#        steps.append(step)

#print(steps)

steps=meta.transititinerary.ItinerarySteps()

