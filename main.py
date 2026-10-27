import random

from termcolor import colored

from grille import Grille
from bateau import PorteAvions, Croiseur, Torpilleur, SousMarin


def placer_bateaux(grille):
    types = [
        PorteAvions,
        Croiseur,
        Torpilleur,
        SousMarin
    ]

    for type_bateau in types:
        possibilites = []

        for ligne in range(grille.lignes):
            for colonne in range(grille.colonnes):
                for vertical in (False, True):

                    bateau = type_bateau(
                        ligne, colonne, vertical
                    )

                    if grille.peut_ajouter(bateau):
                        possibilites.append(bateau)

        if not possibilites:
            raise RuntimeError("Placement impossible")

        bateau = random.choice(possibilites)
        grille.ajoute(bateau)


def trouver_bateau(grille, ligne, colonne):
    for bateau in grille.bateaux:
        if (ligne, colonne) in bateau.positions():
            return bateau

    return None


def afficher_grille(grille, tirs):
    print()
    print("   " + " ".join(str(i) for i in range(grille.colonnes)))

    for ligne in range(grille.lignes):
        cases = []

        for colonne in range(grille.colonnes):
            position = (ligne, colonne)
            bateau = trouver_bateau(grille, ligne, colonne)

            if bateau is not None and bateau.coulé(grille):
                symbole = colored(bateau.marque, "green")

            elif position not in tirs:
                symbole = colored("∿", "cyan")

            elif bateau is not None:
                symbole = colored("💣", "red")

            else:
                symbole = colored("x", "yellow")

            cases.append(symbole)

        print(str(ligne) + "  " + " ".join(cases))

    print()


def main():
    grille = Grille(8, 10)

    placer_bateaux(grille)

    tirs = set()
    nombre_coups = 0

    print(colored("=== BATAILLE NAVALE ===", "cyan"))
    print("Bienvenue dans le jeu !")
    print("Vous devez couler les quatre bateaux.")

    while not all(b.coulé(grille) for b in grille.bateaux):

        afficher_grille(grille, tirs)

        try:
            entree = input(
                "Ligne (0-7, q pour quitter) : "
            )

            if entree.lower() == "q":
                print("Au revoir !")
                return

            ligne = int(entree)
            colonne = int(input("Colonne (0-9) : "))

        except ValueError:
            print(colored("Entrée invalide !", "red"))
            continue

        if not grille.dans_grille(ligne, colonne):
            print(colored("Hors de la grille !", "red"))
            continue

        position = (ligne, colonne)

        if position in tirs:
            print(colored("Vous avez déjà tiré ici !", "yellow"))
            continue

        tirs.add(position)
        nombre_coups += 1

        bateau = trouver_bateau(grille, ligne, colonne)

        if bateau is None:
            grille.tirer(ligne, colonne)

            print(colored("À l'eau !", "blue"))

        else:
            grille.tirer(ligne, colonne, touche="💣")

            print(colored("Touché !", "red"))

            if bateau.coulé(grille):
                nom = type(bateau).__name__

                print(colored(
                    nom + " coulé !",
                    "green"
                ))

    afficher_grille(grille, tirs)

    print(colored("VICTOIRE !", "green"))
    print("Tous les bateaux sont coulés !")
    print("Nombre de coups :", nombre_coups)


if __name__ == "__main__":
    main()
