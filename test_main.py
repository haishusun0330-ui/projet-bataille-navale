
from grille import Grille
from main import placer_bateaux


def test_placement_aleatoire():
    grille = Grille(8, 10)

    placer_bateaux(grille)

    assert len(grille.bateaux) == 4

    positions = []

    for bateau in grille.bateaux:
        for position in bateau.positions():
            assert grille.dans_grille(*position)

            assert position not in positions
            positions.append(position)

    assert len(positions) == 11
