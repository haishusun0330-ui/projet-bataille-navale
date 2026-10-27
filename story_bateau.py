from bateau import Bateau


b1 = Bateau(0, 0, longueur=3)
b2 = Bateau(0, 2, longueur=2)
b3 = Bateau(2, 0, longueur=2)

print("Bateau 1 :", b1.positions())
print("Bateau 2 :", b2.positions())
print("Bateau 3 :", b3.positions())

print("B1 et B2 se chevauchent :", b1.chevauche(b2))
print("B1 et B3 se chevauchent :", b1.chevauche(b3))
