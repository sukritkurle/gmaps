import logging
logging.captureWarnings(True)

from geopy.geocoders import Nominatim
from geopy.distance import vincenty

geolocator = Nominatim(country_bias='India')

student_address = geolocator.geocode("ITI Colony, Bangalore")
loc1 = (student_address.latitude, student_address.longitude)

distances = []
coll_dist = {}
colleges = ['BMS College of Engineering',
            'Dayanand Sagar',
            'PES College',
            'Cambridge College',
            'REVA College',
            'CMRIT',
            'APS College',
            'ACS College',
            'Alliance university',
            'AMC college'
            ]

#Amruta college, Cyrus Intec
# college = "Don bosco institute of technology"
# print geolocator.geocode(college + ", Bangalore")
for college in colleges:
    college_address = geolocator.geocode(college + ", Bangalore")
    loc2 = college_address.latitude, college_address.longitude
    distance = vincenty(loc1, loc2)
    coll_dist.update({college:distance})
    distances.append(distance)

minimum = min(distances)

print "College: ", coll_dist.keys()[coll_dist.values().index(minimum)]
print "Distance: ", minimum

# for k, v in coll_dist.iteritems():
#     print k, v
#     print "\n"
print "------------------------\n\n"
