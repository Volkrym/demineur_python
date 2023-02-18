import random
from math import ceil
rejoue = True
print("Bienvenue au jeu de la Roulette !")
print("Triplé votre mise si vous tombé sur le chiffre exact.")
print("Gagné la moitié de votre mise si vous trouvez la bonne couleur! (Rouge = Impair / Noire = Pair)" )
print("Bonne chance !")
print("")
while rejoue == True:
    argent = int(input("Choisissez votre montant initial : "))
    goal = int(input("Choisissez votre objectif de jetons à atteindre : "))
    print("")
    while argent > 0 and argent < goal:
        print(f"Vous avez un montant de {argent} jetons : ")
        mise = int(input("Combien de jetons voulez-vous miser ?: "))
        argent -= mise
        print()
        choix = int(input("Choisissez un nombre entre 0 et 49, Pour rappel: impair = Rouge et Pair = Noir : "))
        resultat = random.randint(0, 49)
        print(f"La bille s'est arrêtée sur le {resultat}")
        if choix == resultat:
            mise *= 3
            argent += mise
            print(f"Bravo, vous avez vu juste! Vous recevez donc {mise * 3} jetons.")
        elif (choix % 2 == resultat % 2 ):
            argent += mise + ceil((mise)/2)
            if resultat % 2 == 1:
                couleur = "Rouge"
            else:
                couleur = "Noire"
            print(f"Bravo, vous gagnez grâce à la couleur qui était {couleur}, vous gagnez donc {mise + ceil((mise)/2)} jetons")
        else:
            print("Raté, vous perdez donc votre mise.")
    if argent >= goal:
        print("Bien joué ! Vous avez atteint votre objectif!")
    else:
        print("Vous avez perdu tout vos jetons ...")
        print("Heureusement que cette argent n'est pas réel ? Enfin... j'espère ?")
    replay =input("Voulez vous rejouer ? Oui/ Non : ")
    if replay == "non":
        rejoue = False
print("À un prochaine fois !")