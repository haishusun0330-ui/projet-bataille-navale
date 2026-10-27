# Projet Bataille Navale

## Présentation

Ce projet consiste à créer un jeu de bataille navale en Python en utilisant la programmation orientée objet.

Le jeu se déroule sur une grille de 8 lignes et 10 colonnes.

## Les bateaux

Le jeu contient quatre bateaux :

- Porte-avions : longueur 4
- Croiseur : longueur 3
- Torpilleur : longueur 2
- Sous-marin : longueur 2

Les bateaux sont placés aléatoirement sur la grille, sans chevauchement.

## Règles du jeu

Le joueur entre une ligne et une colonne pour tirer.

- ∿ : case non attaquée
- x : tir manqué
- 💣 : bateau touché

Lorsqu'un bateau est coulé, sa marque apparaît sur la grille.

Le jeu se termine lorsque les quatre bateaux sont coulés.

## Installation

Créer un environnement virtuel :

```powershell
py -m venv .venv
```

Installer les dépendances :

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Exécution

Pour lancer le jeu :

```powershell
.\.venv\Scripts\python.exe main.py
```

## Tests

Pour exécuter les tests :

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

## Structure

- `grille.py` : classe Grille
- `bateau.py` : classes des bateaux
- `main.py` : jeu principal
- `story_grille.py` : scénario de la grille
- `story_bateau.py` : scénario des bateaux
- `test_grille.py` : tests de la grille
- `test_bateau.py` : tests des bateaux
- `test_main.py` : tests du jeu
