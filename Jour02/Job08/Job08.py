import mysql.connector

class Zoo:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Quiqui06--&&",
            database="zoo"
        )
        self.cursor = self.conn.cursor()

    def creer_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cage (id INT AUTO_INCREMENT PRIMARY KEY, superficie INT, capacite_max INT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS animal (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), race VARCHAR(255), id_cage INT, FOREIGN KEY (id_cage) REFERENCES cage(id))")

    def ajouter_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Cage ajoutée avec succès.")

    def ajouter_animal(self, nom, race, id_cage):
        query = "INSERT INTO animal (nom, race, id_cage) VALUES (%s, %s, %s)"
        values = (nom, race, id_cage)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Animal ajouté avec succès.")

    def calculer_superficie_totale(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        superficie_totale = self.cursor.fetchone()[0]
        return superficie_totale

    def afficher_animaux(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("Animaux dans le zoo :")
        for animal in result:
            print(animal)

if __name__ == "__main__":
    zoo = Zoo()
    zoo.creer_tables()
    
    zoo.ajouter_cage(100, 5)
    zoo.ajouter_cage(200, 10)
    
    zoo.ajouter_animal("Lion", "Félin", 1)
    zoo.ajouter_animal("Tigre", "Félin", 1)
    zoo.ajouter_animal("Ours", "Ursidé", 2)
    
    print("Superficie totale des cages :", zoo.calculer_superficie_totale())
    zoo.afficher_animaux()
