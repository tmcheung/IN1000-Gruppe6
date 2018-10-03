class Bygning:

    def __init__(self, addr, huseier, leietakere):
        self._addr = addr
        self._huseier = huseier
        self._leietakere = leietakere #int

    def flyttInn(self, antall):
        """
        Metoden tar inn antall leietakere som skal flytte inn
        """

        self._leietakere += antall

    def flyttUt(self, antall, minthreshold=10):
        """
        Metoden tar inn antall leietakere som skal flytte ut
        """
        if (self._leietakere - antall) < 0:
            print("Flere utflytter enn leietakere")
            self._leietakere = minthreshold
        else:
            self._leietakere -= antall


    def nyEier(self, nyEier):
        self._huseier = nyEier



    def skrivInfo(self):
        print("INFO:",self._addr, self._huseier, self._leietakere, end="iojodisdjfiosaf")
