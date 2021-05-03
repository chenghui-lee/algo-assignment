from geopy.distance import great_circle
import googlemaps

lst = [['Rawang', 3.3615395462207878, 101.56318183511695, 'Bukit Jelutong', 3.1000170516638885, 101.53071480907951],
       ['Subang Jaya', 3.049398375759954, 101.58546611160301, 'Puncak Alam', 3.227994355250716, 101.42730357605375],
       ['Ampang', 3.141855957281073, 101.76158583424586, 'Cyberjaya', 2.9188704151716256, 101.65251821655471]]

ori_1 = (3.3615395462207878, 101.56318183511695)
des_1 = (3.1000170516638885, 101.53071480907951)
print(great_circle(ori_1, des_1).km, 'km')

ori_2 = (3.049398375759954, 101.58546611160301)
des_2 = (3.227994355250716, 101.42730357605375)
print(great_circle(ori_2, des_2).km, 'km')

ori_3 = (3.141855957281073, 101.76158583424586)
des_3 = (2.9188704151716256, 101.65251821655471)
print(great_circle(ori_3, des_3).km, 'km')

# Google Distance Matrix API
# gmaps = googlemaps.Client(key='AIzaSyAVVnomYZhH6Z8zvfckBg3l_iHuujD1aqc')
# distance_result = gmaps.distance_matrix(origins=ori_1, destinations=des_1, mode="driving")
# distance_result = gmaps.distance_matrix(origins=ori_2, destinations=des_2, mode="driving")
# distance_result = gmaps.distance_matrix(origins=ori_3, destinations=des_3, mode="driving")
