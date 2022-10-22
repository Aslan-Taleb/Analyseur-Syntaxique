        # PARTIE class
# class Pile
class Pile:

    def __init__(self):
        self.valeurs = []

    def empiler(self, valeur):
        self.valeurs.append(valeur)

    def depiler(self):
        if self.valeurs:
            return self.valeurs.pop()

    def estVide(self):
        return self.valeurs == []

    def __str__(self):
        ch = ''
        for x in self.valeurs:
            ch = "|\t" + str(x) + "\t|" + "\n" + ch
        ch = "\nEtat de la pile:\n" + ch
        return ch


        # PARTIE GRAMMAIRE
# tableau terminaux
tabTerminaux = ["main()", "int", "float", "id", "if", "else",
                "=", "<", ">", "{", "}", "$", '']
# tableau nonTerminaux
tabNonTerminaux = ["programme", "liste_declaration", "liste_instruction", "une_declaration", "une_instruction", "affectation", "type",
                                "test", "condition", "operateur"]

        #PARTIE ENTRY
#ca verifie que le mot donner est dans le tableau terminaux
def check(monSymbole):
    for i in range(0, len(tabTerminaux)-1):
        if monSymbole == tabTerminaux[i]:
            return True
    return False

#a partir de chaine augmente monSymbole jusqu'a trouver un mot
def found(chaine):
    monSymbole = ''
    for i in range(0, len(chaine)+1):
        if check(monSymbole) == False:
            monSymbole += chaine[i]
        else:
            print("j'ai trouvé c'est le mot : " + monSymbole)
            return monSymbole
    return False

#trouve le mot le met dans entry (+met $ a la fin) et l'enleve de chaine puis retourne normalemnet une chaine vide
def fillentry(chaine, entry):
    resultFound = ''
    while(chaine != '' and resultFound != False):
        resultFound = found(chaine)
        if resultFound != False:
            entry.empiler(resultFound)
            chaine = chaine.replace(resultFound, "")
    entry.empiler("$")
    return chaine

        #reste a faire
#Regles (j'ai penser a un switch)
#dans le switch on empile et  depile "pile"

#fonction qui dit quelle regles appliquer une genre de traduction de la table d'analyse 
#ptet genre  exemple : pile == indexNonTerminal[0] and  entry == indexTerminal[0] -> regle 1

#fonction qui dit eh c'est bon le mot a etait trouver

#affichage finale faut faire le tableau j'imagine

