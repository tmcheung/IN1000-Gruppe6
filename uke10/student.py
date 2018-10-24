class Student:

    def __init__(self, navn):
        self._navn = navn
        self._fagListe = []

    def __str__(self):
        return self.hentStudentNavn()

    def leggTilFag(self, fag):
        self._fagListe.append(fag)

    def hentAntallFag(self):
        return len(self._fagListe)

    def hentStudentNavn(self):
        return self._navn

    def skrivFagPaaStudent(self):
        print("\nskrivFagPaaStudent:\n" + self.hentStudentNavn())
        for fag in self._fagListe:
            print(fag)
