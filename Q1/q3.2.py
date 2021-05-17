import pickle
import googlemaps
import gmplot

# read distionary from q3_distance.pkl
import polyline

a_file = open("q3_distance.pkl", "rb")
distance = pickle.load(a_file)
a_file.close()

hub = ["City-link Express", "Pos Laju", "GDEX", "J&T", "DHL"]

cus_distance = []

# convert from dictionary to list
for i in range(1, 4):
    companyDistance = {}
    for j in range(0, len(hub)):
        companyDistance[hub[j]] = distance[('Customer ' + str(i), hub[j])]
    cus_distance.append(companyDistance)

# sort according to result
for i in range(len(cus_distance)):
    cus_distance[i] = {k: v for k, v in sorted(cus_distance[i].items(), key=lambda item: item[1])}

print(cus_distance)

# print result
for i in range(1, 4):
    print('The best choice for customer ' + str(i), 'is ', list(cus_distance[i - 1].items())[0])

hubLocation = [["City-link Express", "Port Klang", (3.0319924887507144, 101.37344116244806)],
               ["Pos Laju", "Petaling Jaya", (3.112924170027219, 101.63982650389863)],
               ["GDEX", "Batu Caves", (3.265154613796736, 101.68024844550233)],
               ["J&T", "Kajang", (2.9441205329488325, 101.7901521759029)],
               ["DHL", "Sungai Buloh", (3.2127230893650065, 101.57467295692778)]]

customer = [
    ['Rawang', (3.3615395462207878, 101.56318183511695), 'Bukit Jelutong', (3.1000170516638885, 101.53071480907951)],
    ['Subang Jaya', (3.049398375759954, 101.58546611160301), 'Puncak Alam', (3.227994355250716, 101.42730357605375)],
    ['Ampang', (3.141855957281073, 101.76158583424586), 'CyberJaya', (2.9188704151716256, 101.65251821655471)]]

color = ['blue', 'red', 'green']

apikey = 'AIzaSyAVVnomYZhH6Z8zvfckBg3l_iHuujD1aqc'


k = 0

for i in range(0, 3):
    gmaps = googlemaps.Client(key=apikey)
    gmap = gmplot.GoogleMapPlotter(3.1133, 101.6116, 10, apikey=apikey)
    gmap.marker(customer[i][1][0], customer[i][1][1])
    gmap.marker(customer[i][3][0], customer[i][3][1], color="green")
    for j in range(0, 5):

        res_1 = gmaps.directions(origin=customer[i][1], destination=hubLocation[j][2], mode="driving")

        route_1 = zip(*polyline.decode(res_1[0]['overview_polyline']['points']))

        res_2 = gmaps.directions(origin=hubLocation[j][2], destination=customer[i][3], mode="driving")

        route_2 = zip(*polyline.decode(res_2[0]['overview_polyline']['points']))

        if hubLocation[j][0] == list(cus_distance[i - 1].items())[0][0]:
            gmap.marker(hubLocation[j][2][0], hubLocation[j][2][1], color="yellow")
            gmap.plot(*route_1, color=color[k], edge_width=7)
            gmap.plot(*route_2, color=color[k+1], edge_width=7)

    gmap.draw("Customer_" + str(i+1) + ".html")


def sorted_distance():
    return cus_distance
