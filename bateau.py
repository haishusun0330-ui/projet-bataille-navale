class Bateau:

    marque = "⛵"

    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        resultat = []

        for i in range(self.longueur):
            if self.vertical:
                position = (self.ligne + i, self.colonne)
            else:
                position = (self.ligne, self.colonne + i)

            resultat.append(position)

        return resultat

    def chevauche(self, autre):
        for position in self.positions():
            if position in autre.positions():
                return True

        return False

    def coulé(self, grille):
        for ligne, colonne in self.positions():
            if not grille.dans_grille(ligne, colonne):
                return False

            index = grille.indice(ligne, colonne)

            if grille.grille[index] not in ("x", "💣"):
                return False

        return True


class PorteAvions(Bateau):

    marque = "🚢"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 4, vertical)


class Croiseur(Bateau):

    marque = "⛴"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 3, vertical)


class Torpilleur(Bateau):

    marque = "🚣"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)


class SousMarin(Bateau):

    marque = "🐟"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
