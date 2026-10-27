from grille import Grille


def main():
    grille = Grille(5, 8)

    while True:
        print()
        print(grille)

        try:
            ligne = input("Ligne (0-4, q pour quitter) : ")

            if ligne.lower() == "q":
                break

            ligne = int(ligne)
            colonne = int(input("Colonne (0-7) : "))

            grille.tirer(ligne, colonne)

        except (ValueError, IndexError):
            print("Coordonnées invalides !")


if __name__ == "__main__":
    main()
