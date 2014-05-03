import pygeocoder
import requests
import sys

args = len(sys.argv) - 1

i = 1
address = ''
coords = ''

while i <= args:
    if i <= 1: 
        address = address + sys.argv[i]
    else: 
        address = address + ' ' + sys.argv[i]
    i += 1

results = pygeocoder.Geocoder.geocode(address)
coords = results[0].coordinates
latitude = coords[0]
longitude = coords[1]

fcc_lookup = 'http://data.fcc.gov/api/speedtest/find?latitude=' + str(latitude) + '&longitude=' + str(longitude) + '&format=json'

r = requests.get(fcc_lookup)

full_data = r.json()

data = full_data['SpeedTestCounty']

print 
print 'Results for ' + str(results[0])
print 
print '(' + str(latitude) + ' ' + str(longitude) + ')'
print 
print 'Max Wire Download: ' + str(data['wirelineMaxDownload'])
print 'Max Wire Upload: ' + str(data['wirelineMaxUpload'])
print 'Average Wire Download: ' + str(data['wirelineAvgDownload'])
print 'Average Wire Upload: ' + str(data['wirelineAvgUpload'])
print 'Max Wireless Download: ' + str(data['wirelessMaxDownload'])
print 'Max Wireless Upload: ' + str(data['wirelessMaxUpload'])
print 'Average Wireless Download: ' + str(data['wirelessAvgDownload'])
print 'Average Wireless Upload: ' + str(data['wirelessAvgUpload'])
