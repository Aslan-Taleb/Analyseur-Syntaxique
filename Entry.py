from asyncio.windows_events import NULL
from Grammaire import *
from Pile import *
from Affichage import *
# PARTIE ENTRY
# ca verifie que le mot donner est dans le tableau terminaux


def check(monSymbole):
    for i in range(0, len(tabTerminaux)-1):
        if monSymbole == tabTerminaux[i]:
            return True
    for i in range(0, len(tabNonTerminaux)-1):
        if monSymbole == tabNonTerminaux[i]:
            return True
    return False

# a partir de chaine augmente monSymbole jusqu'a trouver un mot


def found(chaine):
    monSymbole = ''
    for i in range(0, len(chaine)+1):
        if check(monSymbole) == False:
            # test si mot existe
            if i < len(chaine):
                monSymbole += chaine[i]
            else:
                Affichage(0, 0, 0, 5)
                quit()
        else:
            return monSymbole
    return False

# trouve le mot le met dans entry (+met $ a la fin) et l'enleve de chaine puis retourne normalemnet une chaine vide


def fillentry(chaine, entry):
    if len(chaine) != 0:
        pileTemporaire = Pile()
        resultFound = ''
        while(chaine != '' and resultFound != False):
            resultFound = found(chaine)
            if resultFound != False:
                pileTemporaire.empiler(resultFound)
                chaine = chaine.replace(resultFound, "", 1)
        pileTemporaire.empiler("$")
        taillePile = pileTemporaire.longeur()
        for i in range(0, taillePile):
            entry.empiler(pileTemporaire.depiler())
    else:
        Affichage(0, 0, 0, 6)
        quit()
