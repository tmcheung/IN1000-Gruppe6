from gave import Gave
from barn import Barn


class Julekalender:

    def __init__(self, navnListe, filnavn):
        self._apnere = []
        self._kalender = []
        self._nesteApner = 0
        self._dag = 0

        for navn in navnListe:
            self._apnere.append(Barn(navn))

        self._lesGavefil(filnavn)


    def _lesGavefil(self, filnavn):
        for linje in open(filnavn):
            linjeInfo = linje.split(", ")
            self._kalender.append(Gave(linjeInfo[0], float(linjeInfo[1])))


    def nyDag(self):
        if self._nesteApner >= len(self._apnere):
            self._nesteApner = 0

        if self._dag >= len(self._kalender):
            print("Julen er over")
            return

        nesteBarn = self._apnere[self._nesteApner]
        nesteGave = self._kalender[self._dag]
        nesteBarn.apneGave(nesteGave)

        self._dag += 1
        self._nesteApner += 1


    def gaveOversikt(self):
        for apner in self._apnere:
            apner.skrivBarn()
