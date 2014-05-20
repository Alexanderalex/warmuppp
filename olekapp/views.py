from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import Template, Context

from olekapp.geocoding import Geocoder

import requests

def home(request):
    location = request.GET.get('location','Jaśminów 21 Tychy')
   
    par = { 'location': location, 'size': '600x400', 'sensor': 'false', 'key': 'AIzaSyBL_vK5AkscECZTxwsgmjMBCJORMw74dE0' }
    data = requests.post('http://maps.googleapis.com/maps/api/streetview',params=par)
    img = open('olekapp/static/test.jpg','wb')
    img.write(data.content)
    img.close()

    latlng = Geocoder.get_coordinates(location)

    template = Template("""
    <!DOCTYPE html>
    <html>
    
    	<head>
    		<title>streetview and latlng</title>
    	</head>
    	<body>
            <span>
            <form>{% csrf_token %}
                Change city: <input type="text" name="location"><br>
                <input type="submit" value="Show">
            </form>
            
            
            <h2>Longitude {{ lng }}</h2>
            <h2>Latitude {{ lat }}</h2>
            </span>
            <span>
    		<h1>Google streetview for {{ location }} </h1>
    		{% load staticfiles %}
    		<img src="{% static "test.jpg" %}" alt="Jasminowa"/>
            </span>
    	</body>

    </html>

    """)
    latlng['location'] = location
    ctx = Context(latlng)
    return HttpResponse(template.render(ctx))