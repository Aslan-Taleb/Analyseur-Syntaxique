from Affichage import *
from Entry import *
from Regles import *

Affichage()
#Chaine
chaine = input("Donner une chaine : ")
chaine = chaine.replace(' ' , '')
chaine = chaine.replace('<' , '')
chaine = chaine.replace('>' , '')
#Pile
pile = Pile()
pile.empiler("$")
pile.empiler(tabNonTerminaux[0])
#Entry
entry = Pile()
fillentry(chaine, entry) #mettre chaine dans pile entry

Error = False
#Affichage en-tête
Affichage(0,0,-1,0)

while Error == False:
    suppr(entry, pile)
    accept(entry, pile)
    #vide
    if entry.valeurs[entry.longeur()-1] == tabTerminaux[11]:
        pile = Regles(16,pile)
        Affichage(entry, pile, "vide", 1)
        # Programme
    elif pile.valeurs[pile.longeur()-1] == tabNonTerminaux[0]:
        if entry.valeurs[entry.longeur()-1] == tabTerminaux[0]:
            pile = Regles(0, pile)
            Affichage(entry, pile, 0, 1)
        else:
            Affichage(entry,pile,0,7)

    # liste_declarations
    elif pile.valeurs[pile.longeur()-1] == tabNonTerminaux[1]:
        if entry.valeurs[entry.longeur()-1] == tabTerminaux[1] or entry.valeurs[entry.longeur()-1] == tabTerminaux[2]:
            pile = Regles(1, pile)
            Affichage(entry, pile, 1, 1)
        elif entry.valeurs[entry.longeur()-1] == tabTerminaux[3] or entry.valeurs[entry.longeur()-1] == tabTerminaux[4] or entry.valeurs[entry.longeur()-1] == tabTerminaux[10]:
            pile = Regles(2, pile)
            Affichage(entry, pile, 2, 1)
        else:
            Affichage(entry,pile,0,7)

    # liste_instructions
    elif pile.valeurs[pile.longeur()-1] == tabNonTerminaux[2]:
        if entry.valeurs[entry.longeur()-1] == tabTerminaux[3] or entry.valeurs[entry.longeur()-1] == tabTerminaux[4]:
            pile = Regles(4, pile)
            Affichage(entry, pile, 4, 1)
        elif entry.valeurs[entry.longeur()-1] == tabTerminaux[10]:
            pile = Regles(5, pile)
            Affichage(entry, pile, 5, 1)
        else:
            Affichage(entry,pile,0,7)

    # une_declaration
    elif pile.valeurs[pile.longeur()-1] == tabNonTerminaux[3]:
        if entry.valeurs[entry.longeur()-1] == tabTerminaux[1] or entry.valeurs[entry.longeur()-1] == tabTerminaux[2]:
            pile = Regles(3, pile)
            Affichage(entry, pile, 3, 1)
        else:
            Affichage(entry,pile,0,7)

    # une_instruction
    elif pile.valeurs[pile.longeur()-1] == tabNonTerminaux[4]:
        if entry.valeurs[entry.longeur()-1] == tabTerminaux[4]:
            pile = Regles(6, pile)
            Affichage(entry, pile, 6, 1)
        elif entry.valeurs[entry.longeur()-1] == tabTerminaux[3]:
            pile = Regles(7, pile)
            Affichage(entry, pile, 7, 1)
        else:
            Affichage(entry,pile,0,7)

    # type
    elif pile.valeurs[pile.longeur()-1] == tabNonTerminaux[6]:
        if entry.valeurs[entry.longeur()-1] == tabTerminaux[1]:
            pile = Regles(8, pile)
            Affichage(entry, pile, 8, 1)
        elif entry.valeurs[entry.longeur()-1] == tabTerminaux[2]:
            pile = Regles(9, pile)
            Affichage(entry, pile, 9, 1)
        else:
            Affichage(entry,pile,0,7)

    # affectation
    elif pile.valeurs[pile.longeur()-1] == tabNonTerminaux[5]:
        if entry.valeurs[entry.longeur()-1] == tabTerminaux[3]:
            pile = Regles(10, pile)
            Affichage(entry, pile, 10, 1)
        else:
            Affichage(entry,pile,0,7)

    # test
    elif pile.valeurs[pile.longeur()-1] == tabNonTerminaux[7]:
        if entry.valeurs[entry.longeur()-1] == tabTerminaux[4]:
            pile = Regles(11, pile)
            Affichage(entry, pile, 11, 1)
        else:
            Affichage(entry,pile,0,7)

    # condition
    elif pile.valeurs[pile.longeur()-1] == tabNonTerminaux[8]:
        if entry.valeurs[entry.longeur()-1] == tabTerminaux[3]:
            pile = Regles(12, pile)
            Affichage(entry, pile, 12, 1)
        else:
            Affichage(entry,pile,0,7)
    # opérateur
    elif pile.valeurs[pile.longeur()-1] == tabNonTerminaux[9]:
        if entry.valeurs[entry.longeur()-1] == tabTerminaux[6]:
            pile = Regles(15, pile)
            Affichage(entry, pile, 15, 1)
        
        elif entry.valeurs[entry.longeur()-1] == tabTerminaux[7]:
            pile = Regles(13, pile)
            Affichage(entry, pile, 13, 1)
        elif entry.valeurs[entry.longeur()-1] == tabTerminaux[8]:
            pile = Regles(14, pile)
            Affichage(entry, pile, 14, 1)
        else:
            Affichage(entry,pile,0,7)
    else:
            Error = Regles(-1, pile)
            Affichage(entry, pile, -1, 2)
      
