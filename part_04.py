import part_01
import json

class Population:
    # initialisation de l'objet avec le chemin du fichier
    def __init__(self, filePath):
        self.filePath = filePath

    def saveData(self, data):
        # ouverture d'un stream en écriture et création/écriture des données
        with open(self.filePath, 'w') as file: 
            json.dump(data, file, indent=2)

    def loadData(self):
        try:
            # ouverture du stream pour la lecture du fichier
            with open(self.filePath, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"Le fichier '{self.filePath}' n'existe pas.")
            return None

# Exemple d'utilisation
pop = Population("populations.txt")

# Sauvegarder les données dans le fichier
pop.saveData(part_01.populations)

# Charger les données depuis le fichier
data = pop.loadData()

if data:
    print(data)
else:
    ("Pas de données  afficher")
