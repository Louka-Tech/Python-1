###Importation des modules nécessaires
from time import sleep


###Try
try:

###DefCours
    def Chapitre1Bases():
        print("Bienvenue dans le chapitre 1, qui porte sur les bases" + Name + " !")

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
    print("")
    print("Menu")
    print("")
    print("Chapitre 1 : Les bases")
    print("Chapitre 2 : Modules")
    print("Chapitre 3 : Après...")
    print("Chapitre 4 : Et ensuite...")

    ChapterChoice = int(input("Entrez votre choix : "))

    if ChapterChoice == 1:
        EnteredNIP = int(input("Entrez le PIN : "))
        if EnteredNIP == NIPCode:
            Chapitre1Bases()


###Except
except KeyboardInterrupt:
    try:
        exit("Erreur")
    except:
        exit()