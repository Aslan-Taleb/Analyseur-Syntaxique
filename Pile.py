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

    def longeur(self):
        return len(self.valeurs)

    def printPile(self):
        for i in range(0, self.len()):
            print(self.valeurs[i])
        print("\t")

    def __str__(self):
        ch = ''
        for x in self.valeurs:
            ch = str(x) + ch
        return ch