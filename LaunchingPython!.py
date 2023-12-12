###Importation des modules nécessaires
from time import sleep


###Try
try:

###DefCours
    ErRoRR = ("54343431425434343425486346965445425465476768464341325209393954")
    def Chapitre1Bases():
        print("Bienvenue dans le chapitre 1, qui porte sur les bases, " + Name + " !")

###CodeMenu
    print("Salut !")
    sleep(1)
    print("Bienvenue danc ce cours de python ! ")
    sleep(1)
    print("Pour commencer, entre ton prénom.")
    Name = str(input("Entre ton prénom : "))
    NameIsCorrect = str(input("Le prénom " + Name + " est il le tien ? : "))
    if NameIsCorrect == ("Non"):
        Name = str(input("Entre ton prénom : "))
    print("Salut, " + Name)
    sleep(1)
    print("Nous allons faire une leçon sur Python")
    sleep(1)
    print("Lorsque tu verras ce symbole : \" /!\ \", fais attention au point montré !")
    sleep(1)
    NIPCode = (1401)
    print("")
    print("Menu")
    print("")
    print("Chapitre 1 : Les bases")
    print("Chapitre 2 : Modules")
    print("Chapitre 3 : Après...")
    print("Chapitre 4 : Et ensuite...")

    ChapterChoice = int(input("Entrez votre choix : "))

    if ChapterChoice == 1:
        while True:
            EnteredNIP = int(input("Entrez le PIN : "))
            if EnteredNIP == NIPCode:
                Chapitre1Bases()
            elif EnteredNIP == 0000:
                break

    if ChapterChoice == 2:
        while True:
            print("/!\ Il semblerait que la phase d'identification soit corrompue.")
            print("/!\ Cherchez dans ce script le code contenu dans la variable ErRoRR")
            EnteredNIP = int(input("Entrez le PIN : "))
            if EnteredNIP == ErRoRR:
                Chapitre2Modules()
            Chapitre1Bases()
                elif EnteredNIP == 0000:
                    break

    if ChapterChoice == 3:
        while True:
            EnteredNIP = int(input("Entrez le PIN : "))
            if EnteredNIP == NIPCode:
                Chapitre3Apres()
            elif EnteredNIP == 0000:
                break
                
    if ChapterChoice == 4:
        while True:
            EnteredNIP = int(input("Entrez le PIN : "))
            if EnteredNIP == NIPCode:
                Chapitre4EtEnsuite()
            elif EnteredNIP == 0000:
                break


###Except
except KeyboardInterrupt:
    try:
        exit("Erreur")
    except:
        exit()