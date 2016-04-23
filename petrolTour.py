class PetrolPump:
    def __init__(self,p,d):
        self.petrol = p
        self.distance = d

def petrol_tour(stns):
    left_petrol = 0
    distance = 0
    pos = len(stns)
    start = -1
    collect_petrol = 0
    for st in reversed(stns):
        left_petrol += st.petrol - st.distance
        if left_petrol > 0:
            start = pos
        pos -= 1
    print (start)

petrol_stations=[]
petrol_stations.append(PetrolPump(4,6))
petrol_stations.append(PetrolPump(6,5))
petrol_stations.append(PetrolPump(7,3))
petrol_stations.append(PetrolPump(4,5))


petrol_tour(petrol_stations)