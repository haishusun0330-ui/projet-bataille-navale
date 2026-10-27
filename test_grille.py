import pytest
from grille import Grille
from bateau import Bateau


def test_init():
    g = Grille(5, 8)

    assert g.lignes == 5
    assert g.colonnes == 8
    assert len(g.grille) == 40


def test_indice():
    g = Grille(5, 8)

    assert g.indice(2, 3) == 19


def test_tirer():
    g = Grille(5, 8)

    g.tirer(2, 3)

    assert g.grille[19] == "x"


def test_affichage():
    g = Grille(2, 3)

    assert str(g) == "∿∿∿\n∿∿∿"

    g.tirer(1, 2)

    assert str(g) == "∿∿∿\n∿∿x"


def test_coordonnees_invalides():
    g = Grille(5, 8)

    with pytest.raises(IndexError):
        g.tirer(5, 3)



def test_ajoute():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2)

    assert g.ajoute(b)

    assert g.grille == [
        "∿", "∿", "∿",
        "⛵", "⛵", "∿"
    ]


def test_depassement():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2, vertical=True)

    assert not g.ajoute(b)

    assert g.grille == ["∿"] * 6


def test_bateaux_chevauchent():
    g = Grille(5, 8)

    b1 = Bateau(0, 0, longueur=3)
    b2 = Bateau(0, 2, longueur=2)

    assert g.ajoute(b1)
    assert not g.ajoute(b2)
