class Fag:

    def __init__(self, navn):
        self._navn = navn
        self._studentListe = []

    def __repr__(self):
        return self.hentFagNavn()

    def leggTilStudent(self, student):
        self._studentListe.append(student)

    def hentAntallStudenter(self):
        return len(self._studentListe)

    def hentFagNavn(self):
        return self._navn

    def skrivStudenterVedFag(self):
        print("\nskrivStudenterVedFag:\n" + self.hentFagNavn())
        for student in self._studentListe:
            print(student)
