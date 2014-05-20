import json
import requests

class Geocoder:
	def get_coordinates(address):
	    par = { 'address': address , 'sensor': 'false', 'key': 'AIzaSyBL_vK5AkscECZTxwsgmjMBCJORMw74dE0' }
	    received = requests.post('https://maps.googleapis.com/maps/api/geocode/json',params=par)
	    jsonobj = json.loads(received.content.decode("utf-8"))

	    return jsonobj['results'][0]['geometry']['location']


