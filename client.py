import os
from base_donnee import  dbToTable, tarifToString, tarifdeToString, PiscToString, dbToString2, avisToString, newPiscine, newAvis, Chargetable, Chargetable1, SupprPiscine, SupprAvis, Supp, Vide_db, updatePiscine, updateAvis

# Fonction pour ajouter de la couleur au texte
class colors:
    green = '\033[92m'
    red = '\033[91m'
    reset = '\033[0m' 
    blue = '\x1b[38;5;27m'

# Fonction pour afficher les informations de la base de donnée
# Fonction d'affichage pour la table piscines
def printCollec():
    print(dbToTable())

def printTarif():
    print(tarifToString())

def printTarifde():
    print(tarifdeToString())

def printAffichePisc():
    print(PiscToString())

# Fonction d'affichage pour la table avis
def printCollec1():
    print(dbToString2())
    
# Fonction pour ajouter des éléments dans une table précise
def addPiscine():
    newPiscine()

def addAvis():
    newAvis()

# Fonction pour ajouter des éléments dans une table précise via un fichier CSV
def ChargetablePisc():
    Chargetable()

def ChargetableAv():
    Chargetable1()

# Fonction pour supprimer des éléments dans une table précise
def removePisc():
    SupprPiscine()

def removeAvis():
    SupprAvis()

# Fonction pour vider la base manga dans une table précise
def resetDB():
    Vide_db()

# Fonction pour supprimer (drop) la base manga
def DropBase():
    Supp()

# Fonction pour afficher le menu de requêtes
os.system('cls' if os.name == 'nt' else 'clear')
print(" +------------------------------------------------------+")
print(f"{colors.blue}    _____         _             ______                   {colors.reset}")
print(f"{colors.blue}   / ____|       |_|           |  ____|                  {colors.reset}")
print(f"{colors.blue}  | |_____      ___ _ __ ___   | |__   __ _ ___ _   _    {colors.reset}")
print(f"{colors.blue}   \___ \ \ /\ / | | '_ ` _ \  |  __| / _` / __| | | |   {colors.reset}")
print(f"{colors.blue}   ____| \ V  V /| | | | | | | | |___| |_| \__ | |_| |   {colors.reset}")
print(f"{colors.blue}  |_____/ \_/\_/ |_|_| |_| |_| |______\__,_|___/\__, |   {colors.reset}")
print(f"{colors.blue}                                                 __/ |   {colors.reset}")
print(f"{colors.blue}                                                |___/    {colors.reset}")
print(" +------------------------------------------------------+\n")

#-----------------------------------------------------------------
#Fonction qui affiche le menu principal
def afficheMenu(choixActions):
    input(" (Continuer)")
    print("\n Actions possibles :")
    print(" +---------------------------------------------------------------------+")
    for ch  in choixActions:
        print (" |  {} |  {}  |".format(str(choixActions.index(ch)+1).ljust(2), ch[0].ljust(59)))
    print(" |  {} |  {}  |".format(len(choixActions)+1, "Quitter".ljust(59)))
    print(" +---------------------------------------------------------------------+")

#Fonction qui affiche le sous menu d'affichage pour les piscines
def afficheMenu2():
    while True:
        input(" (Continuer)")
        print("\n\n Actions possibles pour afficher les piscines :")
        print(" +---------------------------------------------------------------------+")
        for i, ch in enumerate(listeChoix2):
            print(" | {} | {} |".format(str(i+1).ljust(2), ch[0].ljust(62)))
        print(" | {}  | {} |".format(len(listeChoix2)+1, "Revenir au menu principal".ljust(62)))
        print(" +---------------------------------------------------------------------+")
        try:
            choix = int(input("\n Votre choix ? : "))
            if choix == len(listeChoix2) + 1:
                break
            elif 1 <= choix and choix <= len(listeChoix2):
                label, fct = listeChoix2[choix-1]
                fct()
            else:
                print(f"{colors.red}*** Choix non valide, veuillez recommencer. ***{colors.reset}")
        except ValueError:
            print(f"{colors.red}*** Veuillez saisir un entier. ***{colors.reset}")

#Fonction qui affiche les sous menu d'affichage des avis
def afficheMenu3():
    while True:
        input(" (Continuer)")
        print("\n\n Actions possibles pour afficher les avis :")
        print(" +---------------------------------------------------------------------+")
        for i, ch in enumerate(listeChoix3):
            print(" |  {} | {}  |".format(str(i+1).ljust(2), ch[0].ljust(60)))
        print(" |  {}  | {}  |".format(len(listeChoix3)+1, "Revenir au menu principal".ljust(60)))
        print(" +---------------------------------------------------------------------+")
        try:
            choix = int(input("\n Votre choix ? : "))
            if choix == len(listeChoix3) + 1:
                break
            elif 1 <= choix and choix <= len(listeChoix3):
                label, fct = listeChoix3[choix-1]
                fct()
            else:
                print(f"{colors.red}*** Choix non valide, veuillez recommencer. ***{colors.reset}")
        except ValueError:
            print(f"{colors.red}*** Veuillez saisir un entier. ***{colors.reset}")

#Fonction qui affiche les sous menu de suppression
def afficheMenu4():
    while True:
        input(" (Continuer)")
        print("\n\n Actions possibles de suppresion :")
        print(" +---------------------------------------------------------------------+")
        for i, ch in enumerate(listeChoix4):
            print(" |  {} | {} |".format(str(i+1).ljust(2), ch[0].ljust(61)))
        print(" |  {}  | {}|".format(len(listeChoix4)+1, "Revenir au menu principal".ljust(62)))
        print(" +---------------------------------------------------------------------+")
        try:
            choix = int(input("\n Votre choix ? : "))
            if choix == len(listeChoix4) + 1:
                break
            elif 1 <= choix and choix <= len(listeChoix4):
                label, fct = listeChoix4[choix-1]
                fct()
            else:
                print(f"{colors.red}*** Choix non valide, veuillez recommencer. ***{colors.reset}")
        except ValueError:
            print(f"{colors.red}*** Veuillez saisir un entier. ***{colors.reset}")

if __name__ == '__main__':
    print(" Fichiers présents dans le répertoire courant : {}".format(os.listdir()))

    listeChoix = [ 
             ("Menu d'affichage des piscines", afficheMenu2),
             ("Menu d'affichage des avis ", afficheMenu3),
             ("Insérer une piscine", addPiscine),
             ("Insérer un avis", addAvis),
             ("Insérer des piscines via fichier CSV",ChargetablePisc),
             ("Insérer des avis via fichier CSV",ChargetableAv),
             ("Menu de suppression", afficheMenu4),
             ("Modifier piscine", updatePiscine),
             ("Modifier avis", updateAvis)
             ]
    
    listeChoix2 = [
        ("Afficher toutes les piscines ", dbToTable),
        ("Afficher les piscines par ordre de tarif croissant", printTarif),
        ("Afficher les piscines par ordre de tarif décroissant", printTarifde),
        ("Afficher les informations d'une seule piscine", printAffichePisc),
        ]
    
    listeChoix3 = [
        ("Afficher tous les avis ", dbToString2),
        ("Afficher les avis d'une piscine précise ", avisToString),
        ]    

    listeChoix4 = [
        ("Supprimer une piscine", removePisc),
        ("Supprimer un avis", removeAvis),
        ("Supprimer le contenu des tables", resetDB),
        ("Supprimer la base", DropBase),
        ]

    while True :
        afficheMenu(listeChoix)
        try :
            choix = int(input("\n Votre Choix ? : "))
            if ( choix == len(listeChoix) + 1 ):
                    break
            elif 1 <= choix and choix <= len(listeChoix):
                label, fct = listeChoix[choix-1] # récupère adresse fct associée
                fct()
            else :
                print (f"{colors.red}*** Choix non valide, veuillez recommencer. ***{colors.reset}")
        except IndexError as e:
            print(e)
            print (f"{colors.red}*** Choix non valide, veuillez recommencer. ***{colors.reset}")
        except ValueError as e :
            print(e)
            print (f"{colors.red}*** Veuillez saisir un entier. ***{colors.reset}")
        except KeyboardInterrupt :
            print(f"\n \n{colors.blue} Vous venez de stopper le script (CTRL + C), à la prochaine !{colors.reset}")
            exit(0)
    print (f"{colors.blue} À bientôt !{colors.reset}")