from random import randint

class Hund:

    def __init__(self, erGutt, navn, alder):
        self._erGutt = erGutt #bool
        self._navn = navn #string
        self._alder = alder #int

    def __str__(self):
        return self.infoTilHund()

    def __eq__(self, other):
        return self.infoTilHund() == other.infoTilHund()

    def infoTilHund(self):
        if self._erGutt:
            return "Navn: " + self._navn + ", Alder: " + str(self._alder) + ", Kjonn: gutt"
        return "Navn: " + self._navn + ", Alder: " + str(self._alder) + ", Kjonn: jente"


class Kennel:

    def __init__(self, rad, kol):
        self._rader = rad
        self._kolonner = kol
        self._hundeListe = self.generer(rad, kol)
        self.skrivUt()

    def generer(self, rader, kolonner):
        navneliste = ["Abe","Ace", "Achillies","Agar", "Aiden", "AJax", "Allegro",
        "Allie","Amazon", "Amigo","Anaconda", "Andres","Android", "Angstrom", "Anise",
        "Aquarius", "Archie", "Argus","Artemis", "Ashes", "Aspen", "Atlas", "August",
        "Avalon", "Armani"]

        maxAlder = 15

        hundeListe = []

        for x in range(rader):
            hundeListe.append([])
            for y in range(kolonner):
                kjonn = randint(0,1)
                if kjonn == 1:
                    kjonn = True #hund skal være gutt
                else:
                    kjonn = False #jente
                navnIndex = randint(0, len(navneliste)-1)
                alder = randint(0, maxAlder)

                hundeListe[x].append(Hund(kjonn, navneliste[navnIndex], alder))

        return hundeListe

    def skrivUt(self):
        for x in range(self._rader):
            tekst = "Rad: " + str(x) + " hunder: "

            for y in range(self._kolonner):
                tekst += self._hundeListe[x][y].infoTilHund()

            print(tekst)

#hentet fra seminar
    def finnNabo(self, rad, kol):
        naboListe = []

        for i in range(-1,2):
            for j in range(-1,2):

                naboRad = rad + i
                naboKol = kol + j

                gyldig = True

                if naboRad == rad and naboKol == kol: #kan ikke være nabo med seg selv
                    gyldig = False

                if naboRad >= self._rader or naboRad < 0: #hundene på toppen og bunnen kan ikke ha naboer over og under seg.
                    gyldig = False

                if naboKol >= self._kolonner or naboKol < 0: #hundene helt til venstre og helt til høyre har ikke naboer til venstre og høyre.
                    gyldig = False

                if gyldig:
                    naboListe.append(self._hundeListe[naboRad][naboKol])

        return naboListe
