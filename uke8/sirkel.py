from math import pi

class Sirkel:

    def __init__(self, radius):
        self._radius = radius

    def hentDiameter(self):
        return self._radius * 2

    def hentOmkrets(self):
        return self.hentDiameter() * pi

    def hentAreal(self):
        return self._radius**2 * pi

    def skrivUt(self):
        print("r: {0}, d: {1}, o: {2}, a: {3}".format(self._radius, self.hentDiameter(), self.hentOmkrets(), self.hentAreal()))


def main():
    s1 = Sirkel(2)
    s2 = Sirkel(4)
    s1.skrivUt()
    s2.skrivUt()


main()
