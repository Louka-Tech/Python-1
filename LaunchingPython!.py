###Importation des modules nécessaires
from time import sleep


###Try
try:
###Code
    print("Salut !")
    sleep(1)
    print("Bienvenue danc ce cours de python ! ")
    sleep(1)
    print("Pour commencer, entre ton prénom.")
    Name = str(input("Entre ton prénom : "))
    NameIsCorrect = str(int("Le prénom " + Name + " est il le tien ? : "))
    if NameIsCorrect == ("Non"):
        Name = str(input("Entre ton prénom : "))

###Except
except KeyboardInterrupt:
    try:
        exit("Erreur")
    except:
        exit()