from Grammaire import *
from Affichage import *

# PARTIE REGLES

# verifier que les deux piles sont vide


def accept(entry, pile):
    if entry.longeur() == 1 and pile.longeur() == 1:
        if entry.valeurs[0] == "$" and pile.valeurs[0] == "$":
            print("| "+str(entry) + " | "+str(pile) + " | accept | ")
            quit()

# supprimer si deux elements au sommet de la pile sont egaux


def suppr(entry, pile):
    while entry.valeurs[entry.longeur()-1] == pile.valeurs[pile.longeur()-1] and entry.valeurs[entry.longeur()-1] != tabTerminaux[11]:
        if entry.valeurs[entry.longeur()-1] != tabTerminaux[11]:
            print("| "+str(entry) + " | "+str(pile) + " | shift | ")
            pile.depiler()
            entry.depiler()

# les regles a appliquer


def Regles(rule, pile):
    match rule:
        case -1:
            return True
        # Programme
        case 0:
            pile.depiler()
            pile.empiler(tabTerminaux[10])
            pile.empiler(tabNonTerminaux[2])
            pile.empiler(tabNonTerminaux[1])
            pile.empiler(tabTerminaux[9])
            pile.empiler(tabTerminaux[0])
            return pile
        # liste_declarations
        case 1:
            pile.depiler()
            pile.empiler(tabNonTerminaux[1])
            pile.empiler(tabNonTerminaux[3])

            return pile
        # vide
        case 2:
            pile.depiler()
            return pile
        # une_declaration
        case 3:
            pile.depiler()
            pile.empiler(tabTerminaux[3])
            pile.empiler(tabNonTerminaux[6])

            return pile
        # liste_instructions
        case 4:
            pile.depiler()
            pile.empiler(tabNonTerminaux[2])
            pile.empiler(tabNonTerminaux[4])

            return pile
        # vide
        case 5:
            pile.depiler()
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
            pile.empiler(tabTerminaux[1])

            return pile
        case 9:
            pile.depiler()
            pile.empiler(tabTerminaux[2])

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
            return pile
        case 14:
            pile.depiler()
            return pile
        case 15:
            pile.depiler()
            pile.empiler(tabTerminaux[6])
            return pile
