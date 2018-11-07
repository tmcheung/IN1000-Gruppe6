from gave import Gave

class Barn:

    def __init__(self, navn):
        self._navn = navn
        self._gaver = []
        self._totalverdi = 0

    def hentNavn(self):
        return self._navn

    def hentTotal(self):
        return self._totalverdi

    def skrivBarn(self):
        print(self.hentNavn())
        for gave in self._gaver:
            print(gave)
        print(self.hentTotal())

    def apneGave(self, gave):
        self._gaver.append(gave)
        self._totalverdi += gave.hentPris()
