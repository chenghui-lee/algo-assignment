import pickle

# read distionary from q3_distance.pkl
a_file = open("q3_distance.pkl", "rb")
distance = pickle.load(a_file)
a_file.close()


hub = ["City-link Express", "Pos Laju", "GDEX", "J&T", "DHL"]

cus_distance = []

for i in range(1,4):
    companyDistance = {}
    for j in range(0, len(hub)):
        companyDistance[hub[j]] = distance[('Customer '+str(i), hub[j])]
    cus_distance.append(companyDistance)

for i in range(len(cus_distance)):
    cus_distance[i] = {k: v for k, v in sorted(cus_distance[i].items(), key=lambda item: item[1])}

print(cus_distance)