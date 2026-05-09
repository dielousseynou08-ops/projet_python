"""#gestion de bibliotheque


class Livre :
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur= auteur
        self.dispo = True

    def  __str__(self):
        statut = "dispo" if self.dispo == True else "emprunté"
        return f"{self.auteur} : {self.titre} ({statut})"

class Bibliotheque:
    def __init__(self):
        self.liste_de_livre = []

    def ajouter(self, livre):
        self.liste_de_livre.append(livre)
        print(f"un livre {livre.titre} a été ajouté à la liste")
    
    def emprunter(self, titre):
        for livre in  self.liste_de_livre:
            if livre.titre == titre:
                if livre.dispo :
                    livre.dispo = False
                    print("livre déjà emprunté !")
                else:
                    print(f"tu as emprunté un livre {titre} !")
                return
        print(f"Livre non trouvé !")
    
    def rendre(self, titre):
        for livre in self.liste_de_livre:
            if livre.titre == titre:
                if livre.dispo :
                    livre.dispo = True
                    print(f"le livre {titre} est rendu !")
                return
        print(f"le livre rendu n'est pas le bon !!! ")
    


    def afficher(self):
        if not self.liste_de_livre:
            print("biblio vide")
        else:
            for livre in self.liste_de_livre:
                print(f"{livre}")


b = Bibliotheque()
b.ajouter(Livre("Pensées pour moi meme", "Marc Auréle"))
b.ajouter(Livre("Le myhte de  Sisyphe", "Albert Camus"))
b.ajouter(Livre("Equation africaine", "Yasmine Khadara"))

print(f"{"="*50}")

print(f"Liste de livres disponible dans la bibliothèque !\n")
b.afficher()
b.emprunter("Equation africaine")
b.afficher()
b.rendre("Equation africaine")"""





# gestion de rendez-vous

class RVD:
    def __init__(self, titre, date,heure, lieu, terminée):
        self.titre = titre
        self.date = date
        self.heure = heure
        self.lieu = lieu
        self.terminée = False

    def __str__(self):
        statut = "Terminée" if self.terminée == True else "a venir"
        return f" vous avez un RV {self.titre}, le {self.date} à {self.heure} lieu {self.lieu} ({statut})"

class Planning:
    def __init__(self):
        self.planning = []

    def ajouter(self,rv):
        self.planning.append(rv)
        print(f"votre Rendez-vous du {rv.date} à {rv.heure} a été ajouté !")
    
    def annuler(self, rv):
        if not self.planning:
            print(f"Aucun rendez-vous en attente dans votre planning")
        else:
            self.planning.remove(rv)
            print(f"votre du {rv.date} à {rv.heure} a été annulé !")
            
    
    def afficher(self):
        if self.planning:
            for p in self.planning:
                print(p)
        else:
            print("Votre plannig est vide !")
            



p = Planning()
rv1 = RVD("Réunion de comité","10/06/26","10h", "salle du 2er étage", False )
rv2 = RVD("Rencontre juridique","20/06/26","11h", "45 av foch", True)
rv3 = RVD("Rencontre avec le RH","12/06/26","15h", "bureau du RH",False )
p.ajouter(rv1)
p.ajouter(rv2)
p.ajouter(rv3)
p.annuler(rv1)
p.afficher()