from Pile import *
from Grammaire import *
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
            monSymbole += chaine[i]
        else:
            return monSymbole
    return False

# trouve le mot le met dans entry (+met $ a la fin) et l'enleve de chaine puis retourne normalemnet une chaine vide
def fillentry(chaine, entry):
    pileTemporaire = Pile()
    resultFound = ''
    while(chaine != '' and resultFound != False):
        resultFound = found(chaine)
        if resultFound != False:
            pileTemporaire.empiler(resultFound)
            chaine = chaine.replace(resultFound, "")
    pileTemporaire.empiler("$")
    taillePile = pileTemporaire.len()
    for i in range(0, taillePile):
        entry.empiler(pileTemporaire.depiler())
    return chaine

# PARTIE REGLES

def accept(entry, pile):
    if entry.len() == 1 and pile.len() == 1:
        if entry.valeurs[0] == "$" and pile.valeurs[0] == "$":
            print("Word Accepted")
            return True
    else:
        return False


def suppr(entry, pile):
    if entry.valeurs[entry.len()-1] == pile.valeurs[pile.len()-1]:
        print("j'ai supprimé :  " + str(entry.valeurs[entry.len()-1]))
        pile.depiler()
        entry.depiler()


def Regles(rule, pile):
    match rule:
        case 0:  # Programme
            pile.depiler()
            pile.empiler(tabTerminaux[10])
            pile.empiler(tabNonTerminaux[2])
            pile.empiler(tabNonTerminaux[3])
            pile.empiler(tabTerminaux[9])
            pile.empiler(tabTerminaux[0])
            return pile
        case 1:  # liste_declarations
            pile.depiler()
            pile.empiler(tabNonTerminaux[1])
            pile.empiler(tabNonTerminaux[3])
            return pile
        case 3:
            pile.depiler()
            pile.empiler(tabTerminaux[3])
            pile.empiler(tabNonTerminaux[6])
            return pile
        case 4:  # liste_instructions
            pile.depiler()
            pile.empiler(tabNonTerminaux[2])
            pile.empiler(tabNonTerminaux[4])
            return pile
        # une_instruction
        case 6:
            pile.depiler()
            pile.empiler(tabNonTerminaux[5])
            return pile
        case 7:
            pile.depiler()
            pile.empiler(tabNonTerminaux[7])
            return pile
        # type
        case 8:
            pile.depiler()
            pile.empiler(tabNonTerminaux[1])
            return pile
        case 9:
            pile.depiler()
            pile.empiler(tabNonTerminaux[2])
            return pile
        # affectation
        case 10:
            pile.depiler()
            pile.empiler(tabTerminaux[13])
            pile.empiler(tabTerminaux[12])
            pile.empiler(tabTerminaux[6])
            pile.empiler(tabTerminaux[3])
            return pile
        # test
        case 11:
            pile.depiler()
            pile.empiler(tabTerminaux[13])
            pile.empiler(tabNonTerminaux[4])
            pile.empiler(tabTerminaux[5])
            pile.empiler(tabNonTerminaux[4])
            pile.empiler(tabNonTerminaux[8])
            pile.empiler(tabTerminaux[4])
            return pile
        # condition
        case 12:
            pile.depiler()
            pile.empiler(tabTerminaux[12])
            pile.empiler(tabNonTerminaux[9])
            pile.empiler(tabTerminaux[3])
            return pile
        # opérateur
        case 13:
            pile.depiler()
            pile.empiler(tabTerminaux[7])
            return pile
        case 14:
            pile.depiler()
            pile.empiler(tabTerminaux[8])
            return pile
        case 15:
            pile.depiler()
            pile.empiler(tabTerminaux[6])
            return pile

        case -1:
            Error = True
            return Error


def Affichage(entry, pile, regle, mode):
    if mode == 0:
        print("------------------------------------------------------------------")
        print("| Entrée  |\t\t\tPile\t\t\t| Action |")
        print("------------------------------------------------------------------")
    elif mode == 1:
        print("| "+str(entry) + " | "+str(pile) +
              " | Regle ->  " + str(regle)+" |")

    elif mode == 2:
        print("⚠ faute de langage ⚠")