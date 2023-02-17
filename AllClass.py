
#class Voiture
class Voiture:
    def __init__(self,mat=39539,mar="GOLF4",car="essence",m=2001,pui=130):
        self._matricule=mat
        self._marque=mar
        self._carburant=car
        self._modele=m
        self._puissance=pui
    #getters/setters
    def getMatricule(self):
        return self._matricule
    def setMatricule(self,m):
        self._matricule=m
    def getMarque(self):
        return self._marque
    def setMarque(self,m):
        self._marque=m
    def getCarburant(self):
        return self._carburant
    def setCarburant(self,c):
        self._carburant=c
    def getModele(self):
        return self._modele
    def setModele(self,m):
        self._modele=m
    def getPuissance(self):
        return self._puissance
    def setPuissance(self,p):
        self._puissance=p
    #Methode
    def __str__(self):
        return f"Matricule:{self._matricule}-Marque:{self._marque}-Carburant:{self._carburant}-Modele:{self._modele}-Puissance:{self._puissance}"

#class VoitureVIP
class VoitureVip(Voiture):
    def __init__(self,mat=39539,mar="GOLF4",car="carburant",m=2001,pui=130,t="4*4"):
        Voiture.__init__(self,mat,mar,car,m,pui)
        self.__type=t
    def getType(self):
        return self.__type
    def setType(self,t):
        if t=="4*4" or t=="SUV" or t=="minibuse" or t=="limousine":
            self.__type=t
        else:
            print("Type invalide")
    def __str__(self):
        return super().__str__() +f"-Type:{self.__type}"

#class ListVoitureVIP
class ListeVoitureVip:
    def __init__(self,LV=[]):
        self._ListVip=LV
    def getListVip(self):
        return self._ListVip
    def setListVip(self,l):
        self._ListVip=l
    def __str__(self):
        for i in self._ListVip:
            print(i.__str__())
    def ajouter(self,v):
        if v in self._ListVip:
            print("voiture exiwt déja")
        else:
            self._ListVip.append(v)     
    def Ajouter(self):
        mat=int(input("entrer votre matricule"))
        mar=input("entrer votre marque")
        car=input("entrer votre carburant")
        m=int(input("entrer modele"))
        pui=int(input("entrer puissance"))
        t=input("entrer type de voiture")
        v=VoitureVip(mat,mar,car,m,pui,t)
        self._ListVip.append(v)
    def Supprimer(self,m):
        exist=False
        for i in self._ListVip:
            if i.getMatricule()==m:
                exist=True
                v=i
        if exist:
            self._ListVip.remove(v)
        else:
            print("voiture n'existe pas")

    def Modifier(self):
        mat=int(input("entrer la matricule de voiture que vou pouver modifier"))
        exist=False
        for i in self._ListVip:
            if i.getMatricule()==mat:
                exist=True
                v=i
        if exist:
            typev=input("entrer nouveu type de voiture")
            v.setType(typev)
        else:
            print("voiture n'existe pas")
            
#class VoitureCitadinne
class VoitureCitadine(Voiture):
    def __init__(self,mat=39539,mar="GOLF4",car="carburant",m=2001,pui=130,g="A"):
        Voiture.__init__(self,mat,mar,car,m,pui)
        self.__gamme=g
    def getGamme(self):
        return self.__gamme
    def setGamme(self,g):
        if g=="A" or g=="B" or g=="C" :
            self.__gamme=g
        else:
            print("Gamme invalide")
    def __str__(self):
        return super().__str__() +f"-Gamme:{self.__gamme}"
    
#class ListVoitureCitadine
class ListeVoitureCitadine:
    def __init__(self,LC=[]):
        self._ListCitadine=LC
    def getListCitadine(self):
        return self._ListCitadine
    def setListCitadine(self,l):
        self._ListCitadine=l
    def __str__(self):
        for i in self._ListCitadine:
            print(i.__str__())
    def Ajouter(self,v):
        if v in self._ListCitadine:
            print("voiture exist déja")
        else:
            self._ListCitadine.append(v)

    def Supprimer(self,v):
        if v in self._ListCitadine:
            self._ListCitadine.remove(v)
        else:
            print("voiture n'existe pas")

    def Modifier(self):
        mat=input("entre matricule de voiture Vip que vous pouvez modifier")
        exist=False
        for i in self._ListCitadine:
            if i.getMatricule()==mat:
                exist=True
                v=i
        if exist:
            gamme=input("entrer nouveu type de voiture")
            v.setGamme(gamme)
        else:
            print("user n'existe pas")



#class Personne
class Personne:
    def __init__(self,cin="LE2000",n="AZG",p="USSM"):
        self._cin=cin
        self._nom=n
        self._prenom=p
    def getCin(self):
        return self._cin
    def setCin(self,c):
        self._cin=c
    def getNom(self):
        return self._nom
    def setNom(self,n):
        self._nom=n
    def getPrenom(self):
        return self._prenom
    def setPrenom(self,p):
        self._prenom=p
    def __str__(self):
        return f"CIN:{self._cin}-Nom:{self._nom}-Prenom:{self._prenom}"

#class Client
class Client(Personne):
    def __init__(self,cin="LE2000",n="AZG",p="USSM",np=121212,t=121666778899):
        Personne.__init__(self,cin,n,p)
        self._NumPermis=np
        self._télé=t
    def getNumP(self):
        return self._NumPermis
    def setNump(self,n):
        self._NumPermis=n
    def getTélé(self):
        return self._télé
    def setTélé(self,n):
        self._télé=n
    def __str__(self):
        return super().__str__()+ f"-NumPermis:{self._NumPermis}-Téléphone:{self._télé}"
#class listCLient
class ListClient:
    def __init__(self,LC=[]):
        self._ListClient=LC
    def getListClient(self):
        return self._ListClient
    def setListClient(self,l):
        self._ListClient=l
    def __str__(self):
        for i in self._ListClient:
            print(i.__str__())
            
    def Ajouter(self,c):
        if user in self._ListClient:
            print("Client exist déja")
        else:
            self._ListClient.append(c)
    def ajouter(self):
        cin=input("entrer votre cin")
        n=input("entrer votre nom")
        p=input("entrer votre prenom")
        np=int(input("entrer numuro permit"))
        t=int(input("entrer numuro téléphone"))
        c=Client(cin,n,p,login,np,t)
        self._ListClient.append(c)
    
    def Supprimer(self,cin):
        exist=False
        for i in self._ListClient:
            if i.getCin()==cin:
                exist=True
                c=i
        if exist:
            self._ListClient.remove(c)
        else:
            print("Client n'éxiste pas")
    def Modifier(self):
        cin=input("entre cin de client que vous pouvez modifier")
        exist=False
        for i in self._ListClient:
            if i.getCin()==cin:
                exist=True
                c=i
        if exist:
            np=int(input("entrer numuro permit"))
            t=int(input("entrer numuro téléphone"))
            c.setNump(np)
            user.setTélé(t)
        else:
            print("Client n'existe pas")
    
#class Utilisateur
class Utilisateur(Personne):
    def __init__(self,cin="LE2000",n="AZG",p="USSM",login="ussm",mdp="123456",email="email@gmail.com"):
        Personne.__init__(self,cin,n,p)
        self._login=login
        self._mdp=mdp
        self._email=email
    def getLogin(self):
        return self._login
    def setLogin(self,l):
        self._login=l
    def getMdp(self):
        return self._mdp
    def setMdp(self,m):
        self._mdp=m
    def getEmail(self):
        return self._email
    def setEmail(self,e):
        self._email=e
    def __str__(self):
        return super().__str__()+f"-Login:{self._login}-email:{self._email}"

#class ListeUtilisateurs
class ListeUtilasateurs:
    def __init__(self,LU=[]):
        self._ListUser=LU
    def getListUser(self):
        return self._ListUser
    def setListUser(self,l):
        self._ListUser=l
    def __str__(self):
        for i in self._ListUser:
            print(i.__str__())
    def Authentifier(self,login,mdp):
        exist=False
        for i in self._ListUser:
            if i.getLogin()==login and i.getMdp()==mdp:
                exist=True
                user=i
        if exist:
            print("Authentification réussi") 
        else:
            print("login or mot de pass invalide essayer un autre fois")
    def Ajouter(self,user):
        if user in self._ListUser:
            print("utilisateur exist déja")
        else:
            self._ListUser.append(user)
    def ajouter(self):
        cin=input("entrer votre cin")
        n=input("entrer votre nom")
        p=input("entrer votre prenom")
        login=input("entrer votre login")
        mdp=input("entre mot de pass")
        email=input("entre email")
        user=Utilisateur(cin,n,p,login,mdp,email)
        self._ListUser.append(user)
    
    def Supprimer(self,login):
        exist=False
        for i in self._ListUser:
            if i.getLogin()==login:
                exist=True
                user=i
        if exist:
            self._ListUser.remove(user)
        else:
            print("user n'éxiste pas")
    def Modifier(self):
        login=input("entre login de utilisateur que vous pouvez modifier")
        exist=False
        for i in self._ListUser:
            if i.getLogin()==login:
                exist=True
                user=i
        if exist:
            login=input("entrer nouveau login")
            mdp=input("entrer nouveau mot de pass")
            email=input("entrer nouveau email")
            user.setLogin(login)
            user.setMdp(mdp)
            user.setEmail(email)
        else:
            print("user n'existe pas")

#class Location
from datetime import date,time
class Location:
    idLocation=0
    def __init__(self,dateL=date(1111,11,1),duréeL=time(),prixL=200,c=Client(),v=Voiture()):
        Location.idLocation+=1
        self._idLocation=Location.idLocation
        self._dateLocation=dateL
        self._duréeLocation=duréeL
        self._prixLocation=prixL
        self._client=c
        self._voiture=v
    def getIdLocation(self):
        return self._idLocation
    def getDateLocation(self):
        return self._dateLocation
    def setDateLocation(self,d):
        self._dateLocation=d
    def getDuréeLocation(self):
        return self._duréeLocation
    def setDuréeLocation(self,d):
        self._duréeLocation=d
    def getPrixLocation(self):
        return self._prixLocation
    def setPrixLocation(self,p):
        self._prixLocation=p
    def getClient(self):
        return self._client
    def setClient(self,c):
        self._client=c
    def getVoiture(self):
        return self._voiture
    def setVoiture(self,v):
        self._voiture=v
    def __str__(self):
        return f"IdLocation:{self._idLocation}-DateLocation:{self._dateLocation}-DuréeLocation:{self._duréeLocation}-PrixLocation:{self._prixLocation}-Client:{self._client}-voiture:{self._voiture}"

#class ListeLocations
class ListeLocations:
    def __init__(self,ListL=[]):
        self._ListLocation=ListL
    def getListLocation(self):
        return self._ListLocation
    def setListLocation(self,l):
        self._ListLocation=l

    def AfficherListeLocation(self):
        for i in self._ListLocation:
            print(i.__str__())
    def AfficherListeLocationCitadine(self):
        ListLocationCitadine=[]
        for i in self._ListLocation:
            if isinstance(i,VoitureCitadinne)==True:
                ListLocationCitadine.append(i)
        for i in ListLocationCitadine:
            print(i.__str__())
    def AfficherListeLocationVip(self):
        ListLocationVip=[]
        for i in self._ListLocation:
            if isinstance(i,VoitureVip)==True:
                ListLocationVip.append(i)
        for i in ListLocationvip:
            print(i.__str__())
    def AfficherLocationMarque(self,m):
        ListLocationMarque=[]
        for i in self._listLocation:
            if i.getMarque()==m:
                ListLocationMarque.append(i)
        for i in ListLocationMarque:
            print(i.__str__())
    def AfficherLocationImma(self,m):
        ListLocationMatricule=[]
        for i in self._ListLocation:
            if i.Matricule()==m:
                ListLocationMatricule.append(i)
        for i in ListLocationMatricule:
            print(i.__str__())
    def AfficherLocationClient(self,cin):
        ListLocationCin=[]
        for i in self._ListLocation:
            if i.getCin()==cin:
                ListLocationCin.append(i)
        for i in ListLocationCin:
            print(i.__str__())
    def AjouterLocation(self,l):
        if l in self._ListLocation:
            print("location exist déja")
        else:
            self._ListLocation.append(l)
    def SupprimerLocation(self,l):
        if l in self._ListLocation:
            self._ListLocation.remove(l)
        else:
            print("location n'exsist pas")
    def FiltrerLocationDate(self,date):
        ListLocationDate=[]
        for i in self._ListLocation:
            if i.getDateLocation()==date:
                ListLocationDate.append(i)
        for i in ListLocationDate:
            print(i.__str__())














            
            
