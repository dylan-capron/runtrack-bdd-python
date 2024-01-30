import mysql.connector

# Paramètres de connexion à la base de données
host = "localhost"
user = "root"
password = "Quiqui06--&&"
database = "LaPlateforme"

# Connexion à la base de données
try:
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()

    # Récupération des noms et des capacités des salles
    cursor.execute("SELECT nom, capacite FROM salle")
    salles = cursor.fetchall()

    # Affichage des résultats en console
    print("Noms et capacités des salles :")
    for salle in salles:
        print("Nom :", salle[0], "- Capacité :", salle[1])

    # Fermeture du curseur et de la connexion
    cursor.close()
    conn.close()

except mysql.connector.Error as e:
    print(f"Erreur lors de la connexion à la base de données : {e}")
