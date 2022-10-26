from tabulate import tabulate

#PARTIE AFFICHAGE
# idée : dans mode 1 mettre la ligne en fonction de len for i in range (0,longeur entry)
# l'affichage

class bcolors:
    OK = '\033[92m' #GREEN
    RULE = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    INTRO = '\033[44m' #RED
    RESET = '\033[0m' #RESET COLOR

def Affichage(entry = 0, pile =0, regle =0, mode =3):
    tiret = '|'
    if mode == 0:
        table = [["Entrée","Pile","Action"]]
        print(tabulate(table,tablefmt="simple"))
    elif mode == 1:
        table = [[str(entry),str(pile),"Regle: "+bcolors.RULE+str(regle)+bcolors.RESET]]
        print(tabulate(table,tablefmt="simple"))
    elif mode == 2:
        print(bcolors.FAIL+"⚠ faute de langage ⚠"+bcolors.RESET)
    elif mode == 3:
        table = [["Meilleur Analyseur Syntaxique(objectivement)"]]
        print(tabulate(table,tablefmt="double_grid"))
    elif mode == 5:
        print(bcolors.FAIL+"⚠ Erreur de Syntaxe"+bcolors.RESET)
    elif mode == 6:
        print(bcolors.FAIL+"⚠ Erreur La Chaine est Vide"+bcolors.RESET)
    elif mode == 7:
        print(bcolors.FAIL+"\n⚠ Aucune regle a appliquer"+bcolors.RESET)
        table = [[str(entry),str(pile)]]
        print(tabulate(table,tablefmt="simple"))
        quit()
