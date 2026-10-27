class Grille:

    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.vide = "∿"

        self.grille = [self.vide] * (lignes * colonnes)
        self.bateaux = []

    def indice(self, ligne, colonne):
        return ligne * self.colonnes + colonne

    def dans_grille(self, ligne, colonne):
        return (
            0 <= ligne < self.lignes
            and 0 <= colonne < self.colonnes
        )

    def tirer(self, ligne, colonne, touche="x"):
        if not self.dans_grille(ligne, colonne):
            raise IndexError("Coordonnées invalides")

        index = self.indice(ligne, colonne)
        self.grille[index] = touche

    def __str__(self):
        resultat = ""

        for ligne in range(self.lignes):
            for colonne in range(self.colonnes):
                index = self.indice(ligne, colonne)
                resultat += self.grille[index]

            if ligne < self.lignes - 1:
                resultat += "\n"

        return resultat


    def peut_ajouter(self, bateau):

        for ligne, colonne in bateau.positions():
            if not self.dans_grille(ligne, colonne):
                return False

        for autre in self.bateaux:
            if bateau.chevauche(autre):
                return False

        return True

    def ajoute(self, bateau):

        if not self.peut_ajouter(bateau):
            return False

        for ligne, colonne in bateau.positions():
            index = self.indice(ligne, colonne)
            self.grille[index] = bateau.marque

        self.bateaux.append(bateau)

        return True
