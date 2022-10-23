#PARTIE AFFICHAGE
# idée : dans mode 1 mettre la ligne en fonction de len for i in range (0,longeur entry)
# l'affichage


def Affichage(entry = 0, pile =0, regle =0, mode =3):
    tiret = '|'
    if mode == 0:
        for i in range(0,150):
            tiret = tiret +'-' 
        print(tiret +'|')
        print("|\t\t\tEntrée\t\t\t|\t\t\tPile\t\t\t|\t\t\tAction\t\t\t   |")
        print(tiret +'|')
    elif mode == 1:
        print("| "+str(entry) + " | "+str(pile) +
              " | Regle -> " + str(regle)+" |")
    elif mode == 2:
        print("⚠ faute de langage ⚠")
    elif mode == 3:
        print("\n\n\t\tBienvenue au meilleur Analyseur Syntaxique(objectivement)\n")
    elif mode == 5:
        print("⚠ Erreur de Syntaxe")
    elif mode == 6:
        print("⚠ Erreur La Chaine est Vide")
    elif mode == 7:
        print("\n⚠ Aucune regle a appliquer")
        print("| "+str(entry) + " | "+str(pile) +" |")
        quit()

    
    
