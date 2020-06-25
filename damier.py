class Damier:

    def longueur(self, y=-1):
        while y <= 0 or y > 200:
            y = int(input("Longueur du damier ? "))
            if y > 200:
                print("Mettre une valeur entre 0 et 200")
            if y < 0:
                print("Mettre une valeur entre 0 et 200")
        return y


    def largeur(self, x=-1):
        while x <= 0 or x > 200:
            x = int(input("Longueur du damier ? "))
            if x > 200:
                print("Mettre une valeur entre 0 et 200")
            if x < 0:
                print("Mettre une valeur entre 0 et 200")
        return x