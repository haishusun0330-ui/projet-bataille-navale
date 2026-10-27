from bateau import Bateau, PorteAvions, Croiseur, Torpilleur, SousMarin
from grille import Grille


def test_init():
    b = Bateau(2, 3)

    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical is False


def test_horizontal():
    b = Bateau(2, 3, longueur=3)

    assert b.positions() == [
        (2, 3),
        (2, 4),
        (2, 5)
    ]


def test_vertical():
    b = Bateau(2, 3, longueur=3, vertical=True)

    assert b.positions() == [
        (2, 3),
        (3, 3),
        (4, 3)
    ]


def test_chevauche():
    b1 = Bateau(0, 0, longueur=3)
    b2 = Bateau(0, 2, longueur=2)
    b3 = Bateau(2, 0, longueur=2)

    assert b1.chevauche(b2)
    assert not b1.chevauche(b3)


def test_coule():
    g = Grille(5, 8)
    b = Bateau(1, 1, longueur=2)

    assert g.ajoute(b)
    assert not b.coulé(g)

    g.tirer(1, 1)
    assert not b.coulé(g)

    g.tirer(1, 2)
    assert b.coulé(g)


def test_types_bateaux():
    b1 = PorteAvions(0, 0)
    b2 = Croiseur(0, 0)
    b3 = Torpilleur(0, 0)
    b4 = SousMarin(0, 0)

    assert b1.longueur == 4
    assert b2.longueur == 3
    assert b3.longueur == 2
    assert b4.longueur == 2

    assert b1.marque == "🚢"
    assert b2.marque == "⛴"
    assert b3.marque == "🚣"
    assert b4.marque == "🐟"


def test_marques_sur_grille():
    g = Grille(8, 10)

    b1 = PorteAvions(0, 0)
    b2 = SousMarin(2, 2)

    assert g.ajoute(b1)
    assert g.ajoute(b2)

    assert g.grille[g.indice(0, 0)] == "🚢"
    assert g.grille[g.indice(0, 3)] == "🚢"
    assert g.grille[g.indice(2, 2)] == "🐟"
