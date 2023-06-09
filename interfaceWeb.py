import cherrypy, os, os.path
import webbrowser as wb
import cherrypy
from ConnectionFinale import dbConnect
from mako.template import Template
from mako.lookup import TemplateLookup
from base_donnee import getPiscinesStr, CheckPiscWeb, getPiscStr, getDecroissant, getCroissant, insertPiscine, Chargetableweb, ModifPiscine, deletePiscine, getAvisStr, CheckAvisWeb, ModifAvis, getOneAvisStr, insertAvis, Chargetableweb2, deleteAvis, getRDVStr, deleteRDV, insertRDV, insertPart, deletePart, Chargetableweb3

mylookup = TemplateLookup(directories=['res/templates'], input_encoding='utf-8', module_directory='res/tmp/mako_modules')
class InterfaceWebPiscines(object):
    
    ###### Page d'accueil #############
    
    @cherrypy.expose
    def index(self):
        mytemplate = mylookup.get_template("index.html")
        return mytemplate.render()
    
    ###### Pages d'affichages ###########
    ###### Affichage des piscines #######
    @cherrypy.expose
    def affPiscines(self, pisc=None):
        mytemplate = mylookup.get_template("aff_piscines.html")
        if pisc:
            return mytemplate.render(piscines=getPiscinesStr(pisc), pisc=CheckPiscWeb())
        else:
            return mytemplate.render(piscines=getPiscinesStr(), pisc=CheckPiscWeb())

    ###### Affichage des rdv ######
    @cherrypy.expose
    def affrdv(self):
        mytemplate = mylookup.get_template("aff_rdv.html")
        return mytemplate.render(rdv=getRDVStr())

    ###### Affichage des piscines par ordre de tarif croissant #######
    @cherrypy.expose
    def affPiscinesCroi(self):
        mytemplate = mylookup.get_template("aff_piscines_croi.html")
        return mytemplate.render(piscines=getCroissant())

    ###### Affichage des piscines par ordre de tarif décroissant #######
    @cherrypy.expose
    def affPiscinesDe(self):
        mytemplate = mylookup.get_template("aff_piscines_decroi.html")
        return mytemplate.render(piscines=getDecroissant())

    ###### Affichage des avis #######
    
    @cherrypy.expose
    def affAvis(self, av=None):
        mytemplate = mylookup.get_template("aff_avis.html")
        if av:
            return mytemplate.render(avis=getAvisStr(av), av=CheckAvisWeb())
        else:
            return mytemplate.render(avis=getAvisStr(), av=CheckAvisWeb())



    ###### Pages d'insertion ###########
    ###### Insertion des piscines ######        
    @cherrypy.expose
    def insertPage(self):        
        mytemplate = mylookup.get_template("insert_piscines.html")        
        return mytemplate.render(type="info")
    
    @cherrypy.expose
    def insertDone(self, nom=None, adresse=None, bas=None, tarif=None, horairo=None, horairf=None, fichierCSV=None):
        if fichierCSV:
            try:
                Chargetableweb(fichierCSV.filename)
                message = "Importation réussie !"
                typ = "success"
            except Exception as e:
                message = "Echec de l'importation."
                typ = "danger"
        else:
            if nom and adresse and bas and tarif and horairo and horairf:
                try:
                    insertPiscine(nom, adresse, bas, tarif, horairo, horairf)
                    message = "Insertion réussie !"
                    typ = "success"
                except Exception as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis."
                typ = "warning"
        
        mytemplate = mylookup.get_template("insert_piscines.html")        
        return mytemplate.render(piscines=getPiscinesStr(), message=message, type=typ)
    
    
    ###### Insertion des avis ######   
    @cherrypy.expose
    def insertPage2(self):        
        mytemplate = mylookup.get_template("insert_avis.html")        
        return mytemplate.render(message="", type="info")

    @cherrypy.expose
    def insertDone2(self, nom=None, jour=None, heure=None, duree=None, commentaire=None, fichierCSV=None):
        if fichierCSV:
            try:
                Chargetableweb2(fichierCSV.filename)
                message = "Importation réussie !"
                typ = "success"
            except Exception as e:
                message = str(e)
                typ = "danger"
        else:
            if nom and jour and heure and duree and commentaire :
                try:
                    insertAvis(nom, jour, heure, duree, commentaire)
                    message = "Insertion réussie !"
                    typ = "success"
                except Exception as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis."
                typ = "warning"
        
        mytemplate = mylookup.get_template("insert_avis.html")        
        return mytemplate.render(avis=getAvisStr(), message=message, type=typ)


    ###### Page des RDV ######
    ###### Insertion des rdv ######    
    
    @cherrypy.expose
    def rdvPage(self, Pseudo=None, NomPiscine=None, Adresse=None, Jour=None, Heure=None, DureeRDV=None, Mess=None, fichierCSV=None):
        if fichierCSV :
            try:
                Chargetableweb3(fichierCSV.filename)
                message = "Importation réussi !"
                typ = "success"
            except Exception as e :
                message = str(e)
                typ = "danger"
        else :
            if Pseudo and NomPiscine and Adresse and Jour and Heure and DureeRDV and Mess:
                try:
                    insertRDV(Pseudo, NomPiscine, Adresse, Jour, Heure,  DureeRDV, Mess)
                    message = "Rendez-vous envoyé !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis."
                typ = "warning"
        rdv = getRDVStr() 
        mytemplate = mylookup.get_template("rdv.html")
        return mytemplate.render(message=message, type=typ, rdv=rdv)

    ###### Insertion des participants ######   
    @cherrypy.expose
    def insertPage4(self):        
        mytemplate = mylookup.get_template("participants.html")        
        return mytemplate.render(message="", type="info")
    
    @cherrypy.expose
    def insertDone4(self, Participant=None, email=None, Niveau=None, RDVID=None):
        if Participant and email and Niveau and RDVID:
            try:
                insertPart(Participant, email, Niveau, RDVID)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis."
            typ = "warning"
        mytemplate = mylookup.get_template("participants.html")        
        return mytemplate.render( message=message, type=typ)
        
    ###### Se désinscrire ###########
    @cherrypy.expose
    def suppressPart(self, email=None):
        if email :
            try:
                deletePart(email)
                message = "Vous êtes désinscrit !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = ""
            typ = "warning"
        mytemplate = mylookup.get_template("suppr_part.html")        
        return mytemplate.render(message=message, type=typ)



    ###### Page de connexion pour les admins #####
    @cherrypy.expose
    def login_page(self):
        # Afficher le formulaire de connexion
        mytemplate = mylookup.get_template("login.html")
        return mytemplate.render()

    @cherrypy.expose
    def login(self, username=None, password=None):
        if username == "admin" and password == "admin":
            raise cherrypy.HTTPRedirect("/admin")
        else:
            message = "Login ou mot de passe incorrect !"
            typ = "danger"
            mytemplate = mylookup.get_template("login.html")
            return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def admin(self):
        # Afficher la page d'administration
        mytemplate = mylookup.get_template("admin.html")
        return mytemplate.render()



    ###### Pages de suppression ###########        
    ###### Suppression piscines ###########
    @cherrypy.expose
    def suppressPisc(self, numPisc=None):
        if numPisc :
            try:
                deletePiscine(int(numPisc))
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = ""
            typ = "warning"
        mytemplate = mylookup.get_template("suppr_pisc.html")        
        return mytemplate.render(message=message, piscines=getPiscinesStr(), type=typ)



    ###### Suppression avis ###########
    @cherrypy.expose
    def suppressAvis(self, numAv=None):
        if numAv :
            try:
                deleteAvis(int(numAv))
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = ""
            typ = "warning"
        mytemplate = mylookup.get_template("suppr_avis.html")        
        return mytemplate.render(message=message, avis=getAvisStr(), type=typ)

    ###### Suppression rdv ###########
    @cherrypy.expose
    def suppressRDV(self, numRDV=None):
        if numRDV :
            try:
                deleteRDV(int(numRDV))
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = ""
            typ = "warning"
        mytemplate = mylookup.get_template("suppr_rdv.html")        
        return mytemplate.render(message=message, rdv=getRDVStr(), type=typ)



    ###### Pages pour les modifications ######
    ###### Page pour la modif des piscines ######
    @cherrypy.expose
    def change_pisc(self, nom=None, adresse=None, bas=None, tarif=None, horairo=None, horairf=None):
        if nom and adresse and bas and tarif and horairo and horairf:
            try:
                if ModifPiscine(nom, adresse, bas, tarif, horairo, horairf):
                    message = "Modification réussie !"
                    typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis."
            typ = "warning"

        mytemplate = mylookup.get_template("modif_pisc.html")
        return mytemplate.render(message=message, pisc=getPiscStr(), type=typ)
    
    ###### Page pour la modif des avis #####
    @cherrypy.expose
    def change_avis(self, nom=None, jour=None, heure=None, duree=None, commentaire=None):
        if nom and jour and heure and duree and commentaire :
            try:
                if ModifAvis(nom, jour, heure, duree, commentaire):
                    message = "Modification réussie !"
                    typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis."
            typ = "warning"

        mytemplate = mylookup.get_template("modif_avis.html")
        return mytemplate.render(message=message, avis=getOneAvisStr(), type=typ)









    ###### Page pour le coming soon ######
    @cherrypy.expose
    def soon(self):
        mytemplate = mylookup.get_template("comingsoon.html")
        return mytemplate.render()

if __name__ == '__main__':
    rootPath = os.path.abspath(os.getcwd())
    wb.open('http://127.0.0.1:8080')
    print("la racine du site est :\n\t{}\n\tcontient : {}".format(rootPath,os.listdir()))
    cherrypy.quickstart(InterfaceWebPiscines(), '/', 'config.txt')