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

    # Récupération des étudiants
    cursor.execute("SELECT * FROM etudiant")
    etudiants = cursor.fetchall()

    # Affichage des étudiants
    print("Liste des étudiants :")
    for etudiant in etudiants:
        print(etudiant)

    # Fermeture du curseur et de la connexion
    cursor.close()
    conn.close()

except mysql.connector.Error as e:
    print(f"Erreur lors de la connexion à la base de données : {e}")