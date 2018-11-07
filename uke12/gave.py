class Gave:

    def __init__(self, navn, pris):
        self._navn = navn
        self._pris = pris

    def hentNavn(self):
        return self._navn

    def hentPris(self):
        return self._pris

    def __str__(self):
        return self.hentNavn() + ": " + str(self.hentPris())
