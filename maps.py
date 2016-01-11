# AIzaSyBaPdoEdmstM0_h1dAcC-Nh22EHNpXiia8
from geolocation.main import GoogleMaps
import logging
logging.captureWarnings(True)

address = "BMSCE, Basavanagudi Bengaluru"
google_maps = GoogleMaps(api_key='AIzaSyBaPdoEdmstM0_h1dAcC-Nh22EHNpXiia8')

location = google_maps.search(location=address) # sends search to Google Maps.

print location.all() # returns all locations.

my_location = location.first() # returns only first location.
# for my_location in location.all():
print my_location.city
print my_location.route
print my_location.formatted_address
print my_location.postal_code
print str(my_location.lat) + "," + str(my_location.lng)
for administrative_area in my_location.administrative_area:
    print("{}: {}".format(administrative_area.area_type, administrative_area.name))

print(my_location.country)
print(my_location.country_shortcut)
print "\n\n"
