
from mainHeader import *

def Regles(x):
    match x:
        case 1:
            entry.depiler()


print("\n\n\t\t****Bienvenue au meilleur Analyseur Syntaxique(objectivement)****")
chaine = input("Donner une chaine : ")
# enleve les espaces
chaine = chaine.replace(' ', '')
pile = Pile()
entry = Pile()

chaine = fillentry(chaine,entry)
#tests
print("chaine : " + chaine +"      censé etre vide ")
print(entry)
