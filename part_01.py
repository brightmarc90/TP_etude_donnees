
populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 12, "name" : "Ian" }
]

relationships = [
    (0,1), (0,2), (1,2), (1,4),(2,3), (2,5),
    (3,4), (3,7), (4,5),(4,8), (4,9), (5,7),
    (5,9), (6,7), (6,8), (7,1), (7,8), (8,9),
    (10,1),(10,2),(10,3),(11,12),(11,2),(11,5)
]

# question 1

for person in populations:
    person["relation"] = []

for person in populations:
    for relation in relationships:
        if person["id"] == relation[0] or person["id"] == relation[1]:
            person["relation"].append(relation)

print(populations)

# question 2
def average():
    sum = 0
    for person in populations:
        sum += len(person["relation"])
    return round(sum / len(populations), 2)

print("===== moyenne ====== \n", average())

#question 3
idList = []
current = populations[0]
for person in populations:
    idList.append({"id" : person["id"], "nb_relations" : len(person["relation"])})
    if len(person["relation"]) > len(current["relation"]):
        current = person
print("===== list de id et nombre de relations ====== \n", idList)
print("===== utilisteur qui a le plus de relations ====== \n",current["name"])

def friendsOfFriends():
    for person in populations:
        listOfFriends = {}
        for i in range(len(person["relation"])):
            if person["relation"][i][0] != person["id"]:
                id = person["relation"][i][0]
                for j in range(len(populations[id]["relation"])):
                    if populations[id]["relation"][j][0] != id and populations[id]["relation"][j][0] != person["id"]:
                        friendId = populations[id]["relation"][j][0]
                        listOfFriends[friendId] = populations[friendId]["name"]
                    else:
                        friendId = populations[id]["relation"][j][1]
                        listOfFriends[friendId] = populations[friendId]["name"]
            else:
                id = person["relation"][i][1]
                for j in range(len(populations[id]["relation"])):
                    if populations[id]["relation"][j][0] != id and populations[id]["relation"][j][0] != person["id"]:
                        friendId = populations[id]["relation"][j][0]
                        listOfFriends[friendId] = populations[friendId]["name"]
                    else:
                        friendId = populations[id]["relation"][j][1]
                        listOfFriends[friendId] = populations[friendId]["name"]
        yield listOfFriends

friends = friendsOfFriends()
print(next(friends))