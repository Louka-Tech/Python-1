salutations = str(input("dites bonjour !"))
if salutations == ("bonjour"):
    print("salut a toi !")
    Humeur = str(input("comment-vas-tu ?"))
    if Humeur == ("Bien"):
        print("Bien  aussi !")
elif salutations == ("salut"):
    print("comment vas tu ?")
else:
    print("je n'ai pas compris")