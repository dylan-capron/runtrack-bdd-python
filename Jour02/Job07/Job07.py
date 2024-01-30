import mysql.connector

class Salarie:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost', 
            user='root',  # Remplacez par le nom d'utilisateur approprié
            password='Quiqui06--&&',  # Remplacez par le mot de passe approprié
            database='entreprise'
        )
        self.cursor = self.conn.cursor()

    def get_employes_with_high_salary(self):
        query = "SELECT * FROM employe WHERE salaire > 3000"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def get_employes_with_service(self):
        query = "SELECT e.nom, e.prenom, e.salaire, s.nom AS service FROM employe e INNER JOIN service s ON e.id_service = s.id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

salarie = Salarie()
# Récupérer les employés avec un salaire supérieur à 3000 €
high_salary_employes = salarie.get_employes_with_high_salary()
print("Employés avec un salaire supérieur à 3000 €:")
for employe in high_salary_employes:
    print(employe)

# Récupérer les employés avec leur service respectif
employes_with_service = salarie.get_employes_with_service()
print("\nEmployés avec leur service respectif:")
for employe in employes_with_service:
    print(employe)

# Fermer la connexion à la base de données
salarie.conn.close()
