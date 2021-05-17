import googlemaps
import pickle
import polyline
import gmplot

apikey = 'AIzaSyAVVnomYZhH6Z8zvfckBg3l_iHuujD1aqc'
gmaps = googlemaps.Client(key=apikey)

hubLocation = [["City-link Express", "Port Klang", (3.0319924887507144, 101.37344116244806)],
               ["Pos Laju", "Petaling Jaya", (3.112924170027219, 101.63982650389863)],
               ["GDEX", "Batu Caves", (3.265154613796736, 101.68024844550233)],
               ["J&T", "Kajang", (2.9441205329488325, 101.7901521759029)],
               ["DHL", "Sungai Buloh", (3.2127230893650065, 101.57467295692778)]]

customer = [
    ['Rawang', (3.3615395462207878, 101.56318183511695), 'Bukit Jelutong', (3.1000170516638885, 101.53071480907951)],
    ['Subang Jaya', (3.049398375759954, 101.58546611160301), 'Puncak Alam', (3.227994355250716, 101.42730357605375)],
    ['Ampang', (3.141855957281073, 101.76158583424586), 'CyberJaya', (2.9188704151716256, 101.65251821655471)]]

color = ['red', 'blue', 'green', 'black', 'pink']

distance_res = {}
final_res = {}
gmap = gmplot.GoogleMapPlotter(3.1133, 101.6116, 10, apikey=apikey)

# calculate distance using Google Matrix API
gmap.marker(3.0319924887507144, 101.37344116244806, color="yellow")
gmap.marker(3.112924170027219, 101.63982650389863, color="yellow")
gmap.marker(3.265154613796736, 101.68024844550233, color="yellow")
gmap.marker(2.9441205329488325, 101.7901521759029, color="yellow")
gmap.marker(3.2127230893650065, 101.57467295692778, color="yellow")


for j in range(0, len(customer)):
    gmap.marker(customer[j][1][0], customer[j][1][1])
    gmap.marker(customer[j][3][0], customer[j][3][1], color="green")
    for i in range(0, len(hubLocation)):
        res_1 = gmaps.directions(origin=customer[j][1], destination=hubLocation[i][2], mode="driving")
        distance_1 = res_1[0]['legs'][0]['distance']['value']

        route = zip(*polyline.decode(res_1[0]['overview_polyline']['points']))
        gmap.plot(*route, color=color[j], edge_width=7)

        res_2 = gmaps.directions(origin=hubLocation[i][2], destination=customer[j][3], mode="driving")
        distance_2 = res_2[0]['legs'][0]['distance']['value']

        route = zip(*polyline.decode(res_2[0]['overview_polyline']['points']))
        gmap.plot(*route, color=color[j], edge_width=7)
        distance_res[(customer[j][0], hubLocation[i][1])] = distance_1
        distance_res[(hubLocation[i][1], customer[j][2])] = distance_2
        distance_res[("Customer " + str(j + 1), hubLocation[i][0])] = distance_1 + distance_2

gmap.draw("Routes.html")

# save dictionary as q3_distance.pkl
a_file = open("q3_distance.pkl", "wb")
pickle.dump(distance_res, a_file)
pickle.dump(final_res, a_file)
a_file.close()
