from mainHeader import *

print("\n\n\t\t****Bienvenue au meilleur Analyseur Syntaxique(objectivement)****")
chaine = input("Donner une chaine : ")
# enleve les espaces
chaine = chaine.replace(' ', '')
pile = Pile()
pile.empiler("$")
pile.empiler("Programme")
entry = Pile()

chaine = fillentry(chaine, entry)
# tests
print("chaine : " + chaine + "      censé etre vide ")


# affichage
Error = False
Affichage(entry, pile, -1, 0)
while accept(entry, pile) != True and Error != True:
    suppr(entry, pile)
    # Programme
    # cette condition est censé arreter le programme ?
    if pile.valeurs[pile.len()-1] == tabNonTerminaux[0]:
        if entry.valeurs[entry.len()-1] == tabTerminaux[0]:
            pile = Regles(0, pile)
            Affichage(entry, pile, 0, 1)

    # liste_declarations
    elif pile.valeurs[pile.len()-1] == tabNonTerminaux[1]:
        if entry.valeurs[entry.len()-1] == tabTerminaux[1] or entry.valeurs[entry.len()-1] == tabTerminaux[2]:
            pile = Regles(1, pile)
            Affichage(entry, pile, 1, 1)

    # liste_instructions
    elif pile.valeurs[pile.len()-1] == tabNonTerminaux[2]:
        if entry.valeurs[entry.len()-1] == tabTerminaux[3] or entry.valeurs[entry.len()-1] == tabTerminaux[4]:
            pile = Regles(4, pile)
            Affichage(entry, pile, 4, 1)

    # une_declaration
    elif pile.valeurs[pile.len()-1] == tabNonTerminaux[3]:
        if entry.valeurs[entry.len()-1] == tabTerminaux[1] or entry.valeurs[entry.len()-1] == tabTerminaux[2]:
            pile = Regles(3, pile)
            Affichage(entry, pile, 3, 1)

    # une_instruction
    elif pile.valeurs[pile.len()-1] == tabNonTerminaux[4]:
        if entry.valeurs[entry.len()-1] == tabTerminaux[4]:
            pile = Regles(6, pile)
            Affichage(entry, pile, 6, 1)
        elif entry.valeurs[entry.len()-1] == tabTerminaux[3]:
            pile = Regles(7, pile)
            Affichage(entry, pile, 7, 1)

    # type
    elif pile.valeurs[pile.len()-1] == tabNonTerminaux[6]:
        if entry.valeurs[entry.len()-1] == tabTerminaux[1]:
            pile = Regles(8, pile)
            Affichage(entry, pile, 8, 1)
        elif entry.valeurs[entry.len()-1] == tabTerminaux[2]:
            pile = Regles(9, pile)
            Affichage(entry, pile, 9, 1)

    # affectation
    elif pile.valeurs[pile.len()-1] == tabNonTerminaux[5]:
        if entry.valeurs[entry.len()-1] == tabTerminaux[3]:
            pile = Regles(10, pile)
            Affichage(entry,pile,10,1)
    
    # test     
    elif pile.valeurs[pile.len()-1]== tabNonTerminaux[7]: 
        if entry.valeurs[entry.len()-1] == tabTerminaux[4]:
            pile = Regles(11,pile)
            Affichage(entry,pile,11,1)

    # condition     
    elif pile.valeurs[pile.len()-1]== tabNonTerminaux[8]: 
        if entry.valeurs[entry.len()-1] == tabTerminaux[3]:
            pile = Regles(12,pile)
            Affichage(entry,pile,12,1)        
    # opérateur     
    elif pile.valeurs[pile.len()-1]== tabNonTerminaux[9]: 
        if entry.valeurs[entry.len()-1] == tabTerminaux[6]:
            pile = Regles(15,pile)
            Affichage(entry,pile,15,1)
        elif entry.valeurs[entry.len()-1] == tabTerminaux[7]:
            pile = Regles(13,pile)
            Affichage(entry,pile,13,1)
        elif entry.valeurs[entry.len()-1] == tabTerminaux[8]:
            pile = Regles(14,pile)
            Affichage(entry,pile,14,1)
    else:
        Error = Regles(-1,pile)
        Affichage(entry,pile,-1,2)


    
