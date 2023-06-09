import os
import cherrypy
from ConnectionFinale import dbConnect, colors
from tabulate import tabulate # Module tabulate pour faire apparaître le contenu en tableau

#-----------------------------------------------------------------
# On initialise les requêtes SQL, qu'on uilisera ensuite dans différentes fonctions

Requete = {
    "getAllPiscine" : "select * from piscines;",
    "getAllAvis" : "select * from avis;",
    "getAllRDV" : "select * from rdv order by ID_RDV desc;",
    
    "getByTarif" : "select * from piscines order by tarif",
    "getByTarifde" : "select * from piscines order by tarif desc",

    "getByNomAvis" : "select * from piscines order by nomPiscine;",

    "InsertPart" : "insert into events(Participant, email, Niveau, RDVID) values ('{}', '{}', '{}', '{}');",
    "InsertPiscine" : "insert into piscines (Nom, Adresse, NbBassin, Tarif, HoraireO, HoraireF) values ('{}','{}','{}','{}','{}','{}');",
    "InsertAvis" : "insert into avis (NomPiscine, Jour, Heure, Duree, Commentaire) values('{}','{}','{}','{}','{}');",
    "InsertRDV" : "insert into rdv (Pseudo, NomPiscine, Adresse, Jour, Heure, Mess, DureeRDV) values('{}','{}','{}','{}','{}','{}','{}');",

    "getByID" : "select * from piscines order by ID_Piscine;",
    "getByIDA" : "select * from avis order by ID_Avis;",
    "getByemail" : "select * from events order by email;",
    "getByIDRDV" : "select * from rdv order by ID_RDV;",

    "getPiscine" : "select * from piscines where Nom = '{}';",
    "getonePiscine" : "select ID_Piscine, Nom from piscines;",
    "getoneAvis" : "select ID_Avis, NomPiscine from avis;",
    "getPiscinebyID" : "select * from piscines where ID_Piscine = '{}';",
    "getAvis" : "select * from avis where NomPiscine = '{}';",
    "getAvisbyID" : "select * from avis where ID_Avis = '{}';",

    "DeletePiscine" : "delete from piscines where ID_Piscine = '{}';" ,
    "DeleteAvis" : "delete from avis where ID_Avis = '{}';" ,
    "DeletePart" : "delete from events where email = '{}';" ,
    "DeleteRDV" : "delete from rdv where ID_RDV = '{}';",

    "ModifPiscine" : "update piscines set Nom = '{}', Adresse = '{}', NbBassin = '{}', Tarif = '{}', HoraireO = '{}', HoraireF = '{}' where ID_Piscine = '{}';",
    "ModifAvis" : "update avis set NomPiscine = '{}', Jour = '{}', Heure = '{}', Duree = '{}', Commentaire = '{}', where ID_Avis = '{}';",

    "Modif1Piscine" : "update piscines set Nom = '{}', Adresse = '{}', NbBassin = '{}', Tarif = '{}', HoraireO = '{}', HoraireF = '{}' where Nom = '{}' ;",
    "Modif1Avis" : "update avis set NomPiscine = '{}', Jour = '{}', Heure = '{}', Duree = '{}', Commentaire = '{}' where NomPiscine = '{}' ;",

    "drop" : "drop database dbpiscine"
}

def execute(request) :
    _dbsae, _cursorsae = dbConnect(False)
    res = _cursorsae.execute(request)
    if "select" in request :
        res = _cursorsae.fetchall()
    else :
        _dbsae.commit()
    return res 


#-----------------------------------------------------------------
# Fonction d'affichage de toutes les données de la table 'piscines'

# Première partie qui va récupérer toutes les informations des piscines sans ordre précis
# Un script qui utiliser la requête SQL et la deuxième pour l'afficher sous forme de tableau en CLI
def affichePiscine():
    req=Requete["getAllPiscine"]
    listepisc=[]
    for pisc in execute(req) :
           listepisc.append([pisc[6], pisc[0], pisc[1], pisc[2], pisc[3], pisc[4], pisc[5]])
    return listepisc

def dbToTable():
    """ Rend le contenu de la table sous forme d'une chaîne de caractères """
    piscines = affichePiscine()
    headers = ["ID", "nom", "adresse", "nb bassin", "tarif (en €)", "ouverture", "fermeture"]
    print("""\n Voici les différentes piscines enregistrées :""")
    print(tabulate(piscines, headers=headers, tablefmt="fancy_grid"))
    return""

def getPiscinesStr()-> list :
    """ getEtudiantsStr() -> liste de chaînes
    Rend le contenu de la base sous forme d'une liste de chaînes """
    req = Requete["getAllPiscine"]
    pisc = []
    for t in execute(req) :
        pisc.append(piscToString(t))
    return pisc

def piscToString(pisc : tuple) -> str :
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"""{pisc[6]}. Nom : {pisc[0]} <br><br> Adresse : {pisc[1]}  -  nombre de bassin : {pisc[2]}  -   tarif : {pisc[3]}€ <br> Horaire ouverture {pisc[4]} - Horaire fermeture {pisc[5]}"""

# Deuxième partie qui va récupérer toutes les informations des piscines rangées par ordre croissant / décroissant du tarif
# Affichage croissant par rapport au tarif d'entrée
def getByTarif():
    """Rend le contenu de la table piscines sous forme d'une liste de tuples """
    req=Requete["getByTarif"]
    listetarif=[]
    for pisc in execute(req) :
           listetarif.append([pisc[6], pisc[0], pisc[1], pisc[2], pisc[3], pisc[4], pisc[5]])
    return listetarif

def tarifToString():
    """ Rend le contenu de la table sous forme d'une chaîne de caractères """
    piscines = getByTarif()
    headers = ["ID", "nom", "adresse", "nb bassin", "tarif (en €)", "ouverture", "fermeture"]
    print("""\n Voici les piscines triées par ordre croissant du tarif :""")
    print(tabulate(piscines, headers=headers, tablefmt="fancy_grid"))
    return""

def getCroissant() -> list :
    """ Rend le contenu de la base sous forme d'une liste de tuples, rangés par ordre d'âge """
    req = Requete["getByTarif"]
    pisc=[]
    for t in execute(req) :
        pisc.append(piscToString(t))
    return pisc

# Affichage décroissant par rapport au tarif d'entrée
def getByTarif2():
    """Rend le contenu de la table piscines sous forme d'une liste de tuples """
    req=Requete["getByTarifde"]
    listetarif=[]
    for pisc in execute(req) :
           listetarif.append([pisc[6], pisc[0], pisc[1], pisc[2], pisc[3], pisc[4], pisc[5]])
    return listetarif

def tarifdeToString():
    """ Rend le contenu de la table sous forme d'une chaîne de caractères """
    piscines = getByTarif2()
    headers = ["ID", "nom", "adresse", "nb bassin", "tarif (en €)", "ouverture", "fermeture"]
    print("""\n Voici les piscines triées par ordre décroissant du tarif :""")
    print(tabulate(piscines, headers=headers, tablefmt="fancy_grid"))
    return""

def getDecroissant() -> list :
    """ Rend le contenu de la base sous forme d'une liste de tuples, rangés par ordre d'âge """
    req = Requete["getByTarifde"]
    pisc=[]
    for t in execute(req) :
        pisc.append(piscToString(t))
    return pisc

# Affichage précis en sélectionnant le nom d'une piscine

def CheckPisc() :
    Name_Piscine = input("\n Saisir le nom de la piscine : ")
    req = Requete["getPiscine"].format(Name_Piscine)
    listePisc=[]
    for pisc in execute(req):
        listePisc.append([pisc[6], pisc[0], pisc[1], pisc[2], pisc[3], pisc[4], pisc[5]])
    return listePisc

def PiscToString():
    """ Rend le contenu de la base sous forme d'une chaîne de caractères """
    piscines = CheckPisc()
    headers = ["ID", "nom", "adresse", "nb bassin", "tarif (en €)", "ouverture", "fermeture"]
    print("""\n Voici les information de la piscine choisie :""")
    print(tabulate(piscines, headers=headers, tablefmt="fancy_grid"))
    return""

    
def CheckPiscWeb()-> list :
    """ getEtudiantsStr() -> liste de chaînes
    Rend le contenu de la base sous forme d'une liste de chaînes """
    req = Requete["getPiscine"]
    pisc = []
    for t in execute(req) :
        pisc.append(opiscToString(t))
    return pisc

def opiscToString(pisc : tuple) -> str :
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"""{pisc[6]}. Nom : {pisc[0]} <br><br> Adresse : {pisc[1]}  -  nombre de bassin : {pisc[2]}  -   tarif : {pisc[3]}€ <br> Horaire ouverture {pisc[4]} - Horaire fermeture {pisc[5]}"""




#-----------------------------------------------------------------    



#-----------------------------------------------------------------
# Fonction qui affiche toutes les données de la table 'avis'

def afficheAv():
    req=Requete["getAllAvis"]
    listeAvis=[]
    for av in execute(req) :
           listeAvis.append([av[5], av[0], av[1], av[2], av[3], av[4]])
    return(listeAvis)

def dbToString2():
    """ Rend le contenu de la base sous forme d'une chaîne de caractères """
    avis = afficheAv()
    headers = ["ID", "nom piscine", "Jour", "Heure de visite", "Durée", "Commentaire"]
    print(""" \n Voici les différentes piscines enregistrées :""")
    print(tabulate(avis, headers=headers, tablefmt="fancy_grid"))
    return""

def getAvisStr()-> list :
    req = Requete["getAllAvis"]
    avis = []
    for t in execute(req) :
        avis.append(avissToString(t))
    return avis

def avissToString(avis : tuple) -> str :
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"Nom de la piscine : {avis[0]} <br> Jour : {avis[1]}  Heure de visite : {avis[2]}  Durée de la visite : {avis[3]} <br>  Commentaire : {avis[4]}"


#Fonction qui affiche les avis d'une piscine précise
def CheckAvis() :
    Name_Piscine = input("\n Saisir le nom de la piscine : ")
    req = Requete["getAvis"].format(Name_Piscine)
    listePisc=[]
    for av in execute(req):
        listePisc.append([av[5], av[0], av[1], av[2], av[3], av[4]])
    return listePisc

def avisToString():
    """ Rend le contenu de la table sous forme d'une chaîne de caractères """
    avis = CheckAvis()
    headers = ["ID", "nom piscine", "Jour", "Heure de visite", "Durée", "Commentaire"]
    print("""\n Voici les avis de la piscine choisie : """)
    print(tabulate(avis, headers=headers, tablefmt="fancy_grid"))
    return""

def CheckAvisWeb()-> list :
    """ getEtudiantsStr() -> liste de chaînes
    Rend le contenu de la base sous forme d'une liste de chaînes """
    req = Requete["getAvis"]
    av = []
    for t in execute(req) :
        av.append(oavisToString(t))
    return av

def oavisToString(avis : tuple) -> str :
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"Nom de la piscine : {avis[0]} <br> Jour : {avis[1]}  Heure de visite : {avis[2]}  Durée de la visite : {avis[3]} <br>  Commentaire : {avis[4]}"

#-----------------------------------------------------------------


#-----------------------------------------------------------------
# Fonction qui affiche toutes les données de la table 'rdv'
def getRDVStr()-> list :
    req = Requete["getAllRDV"]
    avis = []
    for t in execute(req) :
        avis.append(RDVToStr(t))
    return avis

def RDVToStr(rdv):
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"""Pseudo : {rdv[0]} <br> Nom de la piscine : {rdv[1]} - Adresse : {rdv[2]} <br> Jour : {rdv[3]} - Heure de réunion: {rdv[4]} - Durée : {rdv[5]} <br> Commentaire : {rdv[6]}"""


#-----------------------------------------------------------------




#-----------------------------------------------------------------



#-----------------------------------------------------------------
# Fonction qui supprime la base entière

def Supp():
    reponse = input(" Êtes-vous sûr de vouloir supprimer la base de donnée ? (saisir 'oui' ou 'non') : ")
    if reponse == 'oui' :
        s = Requete["drop"]
        print(f"\n{colors.red} La base 'dbPiscine' a été supprimé avec succès.{colors.reset}")
        execute(s)
    elif reponse == 'non' :
        print(f"\n{colors.green} Annulation de la suppression des données. {colors.reset}")
    else :
        print(f"\n{colors.green} Annulation de la suppression des données. {colors.reset}")
#-----------------------------------------------------------------


#-----------------------------------------------------------------
# Fonction qui ajoute des données dans la table piscine

def newPiscine():
    print()
    Nom = input(" Saisir le nom : ")
    Adresse = input(" Saisir l'adresse : ")
    NbdeBassin = input(" Nombre de bassin (compris entre 1 et 10) : ")
    Tarif = input(" Saisir le tarif (un réel) : ")
    HoraireO = input(" Saisir l'heure d'ouverture (format HHhMM): ")
    HoraireF = input(" Saisir l'heure de fermeture (format HHhMM): ")
    print()
    try :
        NewsPiscine(Nom, Adresse, NbdeBassin, Tarif, HoraireO, HoraireF)
        print(f"{colors.green} CRÉATION RÉUSSIE{colors.reset}")
    except :
        print(f"{colors.red} Erreur de saisi, merci de bien vouloir recommencer.{colors.reset}")
        input()

def NewsPiscine(Nom, Adresse, NbdeBassin, Tarif, HoraireO, HoraireF):
    s = Requete["InsertPiscine"].format(Nom, Adresse, NbdeBassin, Tarif, HoraireO, HoraireF)
    execute(s)



def mkInsertPisc(Nom, Adresse, NbdeBassin, Tarif, HoraireO, HoraireF) :
    s= Requete["InsertPiscine"].format(Nom.capitalize(),Adresse,NbdeBassin, Tarif, HoraireO, HoraireF)
    return s

def insertPiscine( Nom : str, Adresse : str, NbdeBassin, Tarif, HoraireO, HoraireF)-> None :
    """ Insertion d'une piscine dans la base"""
    req = mkInsertPisc(Nom.capitalize(),Adresse,NbdeBassin,Tarif,HoraireO,HoraireF)
    execute(req)
#-----------------------------------------------------------------


#-----------------------------------------------------------------
# Fonction qui ajoute des infos dans la table avis

def newAvis():
    print()
    NomPiscine = input(" Saisir le nom de la piscine visitée : ")
    Jour = input(" Saisir le jour de visite (format 'AAAA-MM-JJ') : ")
    Heure = input(" L'heure d'arrivée : ")
    Duree = input(" Saisir la durée de votre visite : ")
    Commentaire = input(" Votre avis : ")
    print()
    try :
        Newsava( NomPiscine, Jour, Heure, Duree, Commentaire)
        print(f"{colors.green} CRÉATION RÉUSSIE{colors.reset}")
    except :
        print(f"{colors.red} Erreur de saisi, merci de bien vouloir recommencer.{colors.reset}")

def Newsava( NomPiscine, Jour, Heure, Duree, Commentaire):
    s = Requete["InsertAvis"].format( NomPiscine, Jour, Heure, Duree, Commentaire)
    execute(s)



def mkInsertAvis(nom, jour, heure, duree, commentaire) :
    s= Requete["InsertAvis"].format(nom.capitalize(),jour,heure, duree, commentaire)
    return s

def insertAvis( nom : str, jour : str, heure, duree, commentaire)-> None :
    """ Insertion d'une piscine dans la base"""
    req = mkInsertAvis(nom.capitalize(), jour, heure, duree, commentaire)
    execute(req)
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Fonction qui ajoute des rdv dans la table rdv

def mkInsertRDV(Pseudo, NomPiscine, Adresse, Jour, Heure, Mess, DureeRDV) :
    s= Requete["InsertRDV"].format(Pseudo.capitalize(), NomPiscine, Adresse, Jour, Heure, Mess, DureeRDV)
    return s

def insertRDV( Pseudo : str, NomPiscine : str, Adresse, Jour, Heure, Mess, DureeRDV)-> None :
    """ Insertion d'une piscine dans la base"""
    req = mkInsertRDV(Pseudo.capitalize(), NomPiscine, Adresse, Jour, Heure, Mess, DureeRDV)
    execute(req)
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Fonction qui ajoute des participants dans la table events

def mkInsertPart(Participant, email, Niveau, RDVID) :
    s= Requete["InsertPart"].format(Participant.capitalize(), email, Niveau, RDVID)
    return s

def insertPart( Participant : str, email : str, Niveau : str, RDVID)-> None :
    """ Insertion d'une piscine dans la base"""
    req = mkInsertPart(Participant.capitalize(), email, Niveau, RDVID)
    execute(req)
#-----------------------------------------------------------------



#-----------------------------------------------------------------
# Fonction qui permet de vider la base de donnée

def Vide_db():
    while True :
        reponse = input(" Voulez-vous vider la base de donnée ? (Saisir 'oui' ou 'non') : ")
        if reponse == 'oui' :
            z = ["piscines","avis"]
            y = 0
            execute("SET FOREIGN_KEY_CHECKS=0;")
            while y < 2:
                execute("DELETE FROM %s " % (z[y]))
                y = y + 1
            execute(" SET FOREIGN_KEY_CHECKS=1;")
            print(f"\n{colors.red} Vous venez de vider les tables de la base 'dbpiscine'.{colors.reset}")
            break
        elif reponse == 'non' :
            print(f"\n{colors.green} Vous avez annulé la procédure pour vider la base de donnée.{colors.reset}")
            break
#-----------------------------------------------------------------


#-----------------------------------------------------------------
# Fonction qui permet de supprimer une pisine en donnant son ID

def SupprPiscine():
    print("")
    ID_Piscine = input(" Merci de saisir l'ID de la piscine à supprimer : ")
    while True :
        print("")
        a = input(" Voulez-vous vraiment supprimer toutes les infos de cette piscine ? ('oui' ou 'non') : ")
        if a == "non":
            print(f"\n{colors.green} La suppresion a été annulée !{colors.reset}")
            break
        elif a == "oui" :
            SupprimePisc(ID_Piscine)
            break
        else :
            print("\n La réponse est incorrect")

def SupprimePisc(ID_Piscine) :
    s = Requete["DeletePiscine"].format(ID_Piscine)
    print(f"{colors.red} La piscine, portant l'ID : {ID_Piscine}, a bien été supprimé.{colors.reset}")
    input()
    execute(s)

def getByIDP(ID_Piscine) :
    s= Requete["getByID"].format(ID_Piscine)
    return s

def DeletePiscine(ID_Piscine) :
    s= Requete["DeletePiscine"].format(ID_Piscine)
    return s

def deletePiscine(ID_Piscine):
    """ Suppression d'une piscine dans la base"""
    t = ID_Piscine
    reqVerif = getByIDP(t)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = DeletePiscine(t)
    execute(req)
#-----------------------------------------------------------------


#-----------------------------------------------------------------
# Fonction qui permet de supprimer un avis en donnant son ID

def SupprAvis():
    print("")
    ID_Avis = input(" Merci de saisir l'ID de l'avis à supprimer : ")
    while True :
        print("")
        a = input(" Voulez-vous vraiment supprimer cet avis ? ('oui' ou 'non') : ")
        if a == "non":
            print("")
            print(f"{colors.green} La suppresion a été annulée !{colors.reset}")
            input()
            break
        elif a == "oui" :
            print("")
            SupprimeAvis(ID_Avis)
            break
        else :
            print("\n La réponse entrée est incorrect")

def SupprimeAvis(ID_Avis) :
    s = Requete["DeleteAvis"].format(ID_Avis)
    print(f"{colors.red} L'avis n° {ID_Avis} a bien été supprimé.{colors.reset}")
    execute(s)

def getByAvis(ID_Avis) :
    s= Requete["getByIDA"].format(ID_Avis)
    return s

def Deleteavis(ID_Avis) :
    s= Requete["DeleteAvis"].format(ID_Avis)
    return s

def deleteAvis(ID_Avis):
    """ Suppression d'un avis dans la base"""
    t = ID_Avis
    reqVerif = getByAvis(t)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = Deleteavis(t)
    execute(req)
#-----------------------------------------------------------------

#Se désinscrire
def getByemail(email) :
    s= Requete["getByemail"].format(email)
    return s

def DeletePart(email) :
    s= Requete["DeletePart"].format(email)
    return s

def deletePart(email):
    """ Suppression d'un avis dans la base"""
    t = email
    reqVerif = getByemail(t)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = DeletePart(t)
    execute(req)
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#Supprimer un rdv

def getByRDV(ID_RDV) :
    s= Requete["getByIDRDV"].format(ID_RDV)
    return s

def DeleteRDV(ID_RDV) :
    s= Requete["DeleteRDV"].format(ID_RDV)
    return s

def deleteRDV(ID_RDV):
    """ Suppression d'un avis dans la base"""
    t = ID_RDV
    reqVerif = getByRDV(t)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = DeleteRDV(t)
    execute(req)

#-----------------------------------------------------------------








#-----------------------------------------------------------------
# Fonction qui permet d'importer un fichier de type CSV pour le CLI

def Chargetable():
    fichier = input(" Saisir le fichier qui comporte les informations des piscines (format csv) : ")
    try :
        x = 0
        while x <= 11 :
            with open(fichier) as f:
                firstline = f.readlines()[x].rstrip()
                y = firstline.split(';')
                execute("INSERT INTO piscines (Nom, Adresse, NbBassin, Tarif, HoraireO, HoraireF, ID_Piscine) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(y[0], y[1], y[2], y[3], y[4], y[5], y[6]))
                x = x + 1
        print(f"{colors.green} INSERTION RÉUSSIE{colors.reset}")
    except :
        print(f"{colors.red} Erreur de saisi, merci de bien vouloir recommencer.{colors.reset}")

def Chargetable1():
    fichier = input(" Saisir le fichier qui comporte les avis (format csv) : ")
    try :
        x = 0
        while x <= 9 :
            with open(fichier) as f:
                firstline = f.readlines()[x].rstrip()
                y = firstline.split(';')
                execute("INSERT INTO avis (NomPiscine, Jour, Heure, Duree, Commentaire, ID_Avis) VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(y[0], y[1], y[2], y[3], y[4], y[5]))                
                x = x + 1
        print(f"{colors.green} INSERTION RÉUSSIE{colors.reset}")
    except :
        print(f"{colors.red} Erreur de saisi, merci de bien vouloir recommencer.{colors.reset}")
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Fonction qui permet d'importer un fichier de type CSV au format WEB !!!

def Chargetableweb(fichierCSV):
    fichier = fichierCSV
    try:
        x = 0
        while x <= 11 :
            with open(fichier) as f:
                firstline = f.readlines()[x].rstrip()
                y = firstline.split(';')
                execute("INSERT INTO piscines (Nom, Adresse, NbBassin, Tarif, HoraireO, HoraireF, ID_Piscine) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(y[0], y[1], y[2], y[3], y[4], y[5], y[6]))
                x = x + 1
        print(f"{colors.green} INSERTION RÉUSSIE{colors.reset}")
    except:
        print(f"{colors.red} Erreur de saisie, merci de bien vouloir recommencer.{colors.reset}")


def Chargetableweb2(fichierCSV):
    fichier = fichierCSV
    try :
        x = 0
        while x <= 9 :
            with open(fichier) as f:
                firstline = f.readlines()[x].rstrip()
                y = firstline.split(';')
                execute("INSERT INTO avis (NomPiscine, Jour, Heure, Duree, Commentaire, ID_Avis) VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(y[0], y[1], y[2], y[3], y[4], y[5]))                
                x = x + 1
        print(f"{colors.green} INSERTION RÉUSSIE{colors.reset}")
    except :
        print(f"{colors.red} Erreur de saisi, merci de bien vouloir recommencer.{colors.reset}")


def Chargetableweb3(fichierCSV):
    fichier = fichierCSV
    try :
        x = 0
        while x <= 5 :
            with open(fichier) as f:
                firstline = f.readlines()[x].rstrip()
                y = firstline.split(';')
                execute("INSERT INTO rdv (Pseudo, NomPiscine, Adresse, Jour, Heure, Mess, DureeRDV) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(y[0], y[1], y[2], y[3], y[4], y[5], y[6]))                
                x = x + 1
        print(f"{colors.green} INSERTION RÉUSSIE{colors.reset}")
    except :
        print(f"{colors.red} Erreur de saisi, merci de bien vouloir recommencer.{colors.reset}")
#-----------------------------------------------------------------



#-----------------------------------------------------------------
#Fonction pour modifier des données de la table piscines
def updatePiscine():
    print()
    id_piscine = input(" Saisir l'ID de la piscine à modifier : ")
    
    # Vérification de l'existence de l'ID de la piscine
    s = Requete["getPiscinebyID"].format(id_piscine)
    result = execute(s)
    if len(result) == 0:
        print(f"{colors.red} Erreur : la piscine avec l'ID {id_piscine} n'existe pas.{colors.reset}")
        return
    elif len(result) != 0 :
        print(f"{colors.blue} Vous allez modifier la piscine possédant l'ID {id_piscine}.{colors.reset}")

    Nom = input(" Saisir le nouveau nom : ")
    Adresse = input(" Saisir la nouvelle adresse : ")
    NbdeBassin = input(" Saisir le nouveau nombre de bassins (compris entre 1 et 10) : ")
    Tarif = input(" Saisir le nouveau tarif (un réel) : ")
    HoraireO = input(" Saisir la nouvelle heure d'ouverture (format HHhMM): ")
    HoraireF = input(" Saisir la nouvelle heure de fermeture (format HHhMM): ")
    print()
    try:
        modifyPiscine(id_piscine, Nom, Adresse, NbdeBassin, Tarif, HoraireO, HoraireF)
        print(f"{colors.green} MODIFICATION RÉUSSIE{colors.reset}")
    except:
        print(f"{colors.red} Erreur de saisie, merci de bien vouloir recommencer.{colors.reset}")
        input()

def modifyPiscine(id_piscine, Nom, Adresse, NbdeBassin, Tarif, HoraireO, HoraireF):
    s = Requete["ModifPiscine"].format(Nom, Adresse, NbdeBassin, Tarif, HoraireO, HoraireF, id_piscine)
    execute(s)

#Fonction pour modifier des donnes de la table avis
def updateAvis():
    print()
    id_avis = input(" Saisir l'ID de l'avis à modifier : ")
    
    # Vérification de l'existence de l'ID de l'avis
    s = Requete["getAvisbyID"].format(id_avis)
    result = execute(s)
    if len(result) == 0:
        print(f"{colors.red} Erreur : l'avis avec l'ID {id_avis} n'existe pas.{colors.reset}")
        return

    Nom = input(" Saisir le nom de la piscine : ")
    Jour = input(" Saisir le jour de la visite : ")
    Heure = input(" Saisir l'heure d'arrivée : ")
    Duree = input(" Saisir la durée de la visite : ")
    Commentaire = input(" Saisir votre nouveau commentaire : ")
    print()
    try:
        modifyAvis(id_avis, Nom, Jour, Heure, Duree, Commentaire)
        print(f"{colors.green} MODIFICATION RÉUSSIE{colors.reset}")
    except:
        print(f"{colors.red} Erreur de saisie, merci de bien vouloir recommencer.{colors.reset}")
        input()

def modifyAvis(id_avis, Nom, Jour, Heure, Duree, Commentaire):
    s = Requete["ModifAvis"].format(Nom, Jour, Heure, Duree, Commentaire, id_avis)
    execute(s)
#-----------------------------------------------------------------





#----------------------------------------------------------------- 
#Modif version web, modif piscines :
#-----------------------------------------------------------------
#Fonction pour modifier des données de la table piscines

def ModifPiscine(nom, adresse, bas, tarif, horairo, horairf):
    if not piscine_existe(nom):
        raise ValueError("La piscine spécifiée n'existe pas.")
    
    s = Requete["Modif1Piscine"].format(nom, adresse, bas, tarif, horairo, horairf, nom)
    execute(s)
    return True

def piscine_existe(nom):
    s = Requete["getPiscine"].format(nom)
    result_tuple = execute(s)
    if result_tuple:
        return True
    else:
        return False

def getPiscStr()-> list :
    req = Requete["getonePiscine"]
    pisc = []
    for t in execute(req) :
        pisc.append(oneToString(t))
    return pisc

def oneToString(pisc : tuple) -> str :
    return f"""{pisc[0]}. Nom : {pisc[1]} <br>"""

#-----------------------------------------------------------------
#Fonction pour modifier des données de la table piscines

def ModifAvis(nom, jour, heure, duree, commentaire) :
    if not avis_existe(nom) :
        raise ValueError("L'avis spécifiée n'existe pas.")
    s = Requete["Modif1Avis"].format(nom, jour, heure, duree, commentaire, nom)
    execute(s)
    return True

def avis_existe(nom) :
    s = Requete["getAvis"].format(nom)
    result_tuple = execute(s)
    if result_tuple:
        return True
    else :
        return False

def getOneAvisStr()-> list :
    req = Requete["getoneAvis"]
    av = []
    for t in execute(req) :
        av.append(oneToString2(t))
    return av

def oneToString2(av : tuple) -> str :
    return f"""{av[0]}. Nom : {av[1]} <br>"""

#---------------------------------------------------------------