import os, pymysql, sqlite3, getpass

# Fonction pour ajouter de la couleur au texte
class colors:
    green = '\033[92m'
    red = '\033[91m'
    reset = '\033[0m' 
    blue = '\x1b[38;5;27m'

# Fonction pour récupérer le login ainsi que le mot de passe de l'utilisateur pour se connecter à la base de donnée

while True :
    try :
        os.system('cls' if os.name == 'nt' else 'clear')
        print("    Création de la base de donnée : dbpiscine")
        print("    Merci de remplir les instructions suivantes\n")
        login = input(">>> Veuillez saisir votre nom d'utilisateur phpMyAdmin : ")
        password = getpass.getpass(">>> Veuillez saisir votre mot de passe phpMyAdmin (le mot de passe reste invisible): ")
        db = pymysql.connect(
            host = "localhost",
            user = login,      
            password = password
        )
        break
    except pymysql.err.OperationalError:
        print(f">>> {colors.red}***Erreur, le saisi est incorrect !***{colors.reset}")
        input("(Appuyez sur entrée pour recommencer)")
        continue 
    except KeyboardInterrupt :
        print(f"\n \n{colors.blue} Vous venez de stopper le script (CTRL + C), à la prochaine !{colors.reset}")
        exit(0)

cur = db.cursor()

cur.execute("DROP DATABASE IF EXISTS dbpiscine;")

cur.execute("CREATE DATABASE IF NOT EXISTS dbpiscine;")

def dbConnect(sqlite3=False,fich="",base=""):
    if sqlite3 :
        db = sqlite3.connect(fich)
    else :
        db = pymysql.connect(host="localhost", charset="utf8", user=login, passwd=password, db="dbpiscine")
    return (db,db.cursor())


#Création de la table piscine
cur.execute("""
CREATE TABLE IF NOT EXISTS dbpiscine.piscines ( Nom VARCHAR(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL , 
Adresse VARCHAR(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL , 
NbBassin ENUM('1', '2', '3', '4', '5', '6', '7', '8', '9', '10') NOT NULL ,
Tarif FLOAT NOT NULL ,
HoraireO VARCHAR(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
HoraireF VARCHAR(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
ID_Piscine INT NOT NULL AUTO_INCREMENT ,
PRIMARY KEY (ID_Piscine)) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_general_ci; """)



#Création de la table avis          
cur.execute("""
CREATE TABLE IF NOT EXISTS dbpiscine.avis ( NomPiscine VARCHAR(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
Jour DATE NOT NULL , 
Heure VARCHAR(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
Duree VARCHAR(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
Commentaire VARCHAR(250) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL , 
ID_Avis INT NOT NULL AUTO_INCREMENT ,
PRIMARY KEY (ID_Avis)) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_general_ci;""") 



#Création de la table RDV
cur.execute("""
CREATE TABLE IF NOT EXISTS dbpiscine.rdv( Pseudo VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
NomPiscine VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
Adresse VARCHAR (50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
Jour DATE NOT NULL,
Heure VARCHAR(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
Mess VARCHAR(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
DureeRDV VARCHAR(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
ID_RDV INT NOT NULL AUTO_INCREMENT ,
PRIMARY KEY (ID_RDV)) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_general_ci;""")



#Création de la table events
cur.execute ("""
CREATE TABLE IF NOT EXISTS dbpiscine.events( EventID INT NOT NULL AUTO_INCREMENT ,
Participant VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
email VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
Niveau VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
RDVID INT NOT NULL ,
PRIMARY KEY (EventID),
FOREIGN KEY (RDVID) REFERENCES rdv(ID_RDV)) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_general_ci;""")