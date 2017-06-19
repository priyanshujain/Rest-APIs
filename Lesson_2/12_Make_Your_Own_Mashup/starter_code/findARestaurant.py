from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "PASTE_YOUR_ID_HERE"
foursquare_client_secret = "YOUR_SECRET_HERE"


def findARestaurant(mealType,location):
	meal = mealType.replace(" ", "+");
	lat, lng = getGeocodeLocation(location)
	url = ('https://api.foursquare.com/v2/venues/search?ll={},{}&query={}'.format(lat, lng, location))
	h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1]['vanues'])
	res = [];
	for i in range(len(result)):
		name = result[i]['name']
		addr = result[i]['location']['address']
		addrUrl = result[i]['url']
		restaurant ={'name':name, 'address':addr, 'Url':addrUrl}
		res.append(restaurant);

	return res
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.

	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi

	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")
