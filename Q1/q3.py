import googlemaps
import json

gmaps = googlemaps.Client(key='AIzaSyAVVnomYZhH6Z8zvfckBg3l_iHuujD1aqc')

hubLocation = [["City-link Express", "Port Klang", (3.0319924887507144, 101.37344116244806)],
               ["Pos Laju", "Petaling Jaya", (3.112924170027219, 101.63982650389863)],
               ["GDEX", "Batu Caves", (3.265154613796736, 101.68024844550233)],
               ["J&T", "Kajang", (2.9441205329488325, 101.7901521759029)],
               ["DHL", "Sungai Buloh", (3.2127230893650065, 101.57467295692778)]]

customer = [
    ['Rawang', (3.3615395462207878, 101.56318183511695), 'Bukit Jelutong', (3.1000170516638885, 101.53071480907951)],
    ['Subang Jaya', (3.049398375759954, 101.58546611160301), 'Puncak Alam', (3.227994355250716, 101.42730357605375)],
    ['Ampang', (3.141855957281073, 101.76158583424586), 'CyberJaya', (2.9188704151716256, 101.65251821655471)]]

distance_res = {}

# calculate distance using Google Matrix API
for i in range(0, len(hubLocation) - 1):
    for j in range(0, len(customer) - 1):
        distance_res[(customer[j][0], hubLocation[i][1])] = gmaps.distance_matrix(origins=customer[j][1],
                                                                                  destinations=hubLocation[i][2],
                                                                                  mode="driving")['rows'][0]['elements'][0]['distance']['value']
        distance_res[(hubLocation[i][1], customer[j][2])] = gmaps.distance_matrix(origins=hubLocation[i][2],
                                                                                  destinations=customer[j][3],
                                                                                  mode="driving")['rows'][0]['elements'][0]['distance']['value']


print(distance_res, file=open("q3_output.txt", "a"))