
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
    person['relation'] = []

for relation in relationships:
    id1, id2 = relation
    populations[id1]['relation'].append(relation)
    populations[id2]['relation'].append(relation)

print("==== Ajout de la clé relation ====\n", populations)

# question 2
def average():
    sum = 0
    for person in populations:
        sum += len(person["relation"])
    return round(sum / len(populations), 2)

print("===== moyenne ====== \n", average())

#question 3
idList = [{"id": person["id"], "nb_relations" : len(person["relation"])} for person in populations]
maxPerson = max(idList, key=lambda x: x['nb_relations'])
print("===== list de id et nombre de relations ====== \n", idList)
print("===== utilisteur qui a le plus de relations ====== \n", maxPerson, populations[maxPerson['id']]['name'])

#question 4
for person in populations:
    person["fof"] = []
for person in populations:
    for id1, id2 in person["relation"]:
        # Ajouter les amis des amis dans une liste
        person["fof"].extend(fof for fof in populations[id1]["relation"] if person["id"] not in fof)
        person["fof"].extend(fof for fof in populations[id2]["relation"] if person["id"] not in fof)

# Afficher les amis des amis de chaque utilisateur
def friendsOfFriends():
    for person in populations:
        yield {"person": person["name"], "fof": list(set([(id, populations[id]["name"]) for relation in person["fof"] for id in relation]))}
friends = friendsOfFriends()
print("==== Amis d'amis ====")
print(next(friends))