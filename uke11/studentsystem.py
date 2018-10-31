from fag import Fag
from student import Student


class Studentsystem:

    def __init__(self):
        self._studentListe = []
        self._fagListe = []

    def oversikt(self):
        print("\n-----------\n", self._studentListe)
        print(self._fagListe, "\n-----------\n")

    def innlesing(self, filnavn):
        fil = open(filnavn)

        nyttFag = None

        for linje in fil:
            if linje[0] == "*":
                fagNavn = linje[1:-1]
                nyttFag = self.finnFag(fagNavn)
                if nyttFag == None:
                    nyttFag = Fag(fagNavn)
                    self._fagListe.append(nyttFag)
            else:
                studentNavn = linje[:-1]
                nyStudent = self.finnStudent(studentNavn)
                if nyStudent == None:
                    nyStudent = Student(studentNavn)
                    self._studentListe.append(nyStudent)
                nyStudent.leggTilFag(nyttFag)
                nyttFag.leggTilStudent(nyStudent)
        fil.close()




    def finnStudent(self, studentNavn):
        for student in self._studentListe:
            if student.hentStudentNavn() == studentNavn:
                return student
        return None


    def finnFag(self, fagNavn):
        for fag in self._fagListe:
            if fag.hentFagNavn() == fagNavn:
                return fag
        return None


    def skrivStudent(self):
        studentNavn = input("Skriv navn til student")
        studenten = self.finnStudent(studentNavn)
        if studenten == None:
            print("Student med navn", studentNavn, "finnes ikke")
            return
        studenten.skrivFagPaaStudent()

    def skrivFag(self):
        fagNavn = input("Skriv navn til fag")
        faget = self.finnFag(fagNavn)
        if faget == None:
            print("Faget med navn", fagNavn, "finnes ikke")
            return
        faget.skrivStudenterVedFag()

    def finnStudentMedFlestFag(self):
        if len(self._studentListe) > 0:
            studentenMedFlest = self._studentListe[0]
            for student in self._studentListe:
                if studentenMedFlest.hentAntallFag() < student.hentAntallFag():
                    studentenMedFlest = student
            print(studentenMedFlest.hentStudentNavn(), "tar flest fag:", studentenMedFlest.hentAntallFag())
        else:
            print("Ingen studenter tilgjengelig")

    def finnFagMedFlestStudenter(self):
        if len(self._fagListe) > 0:
            fagetMedFlest = self._fagListe[0]
            for fag in self._fagListe:
                if fagetMedFlest.hentAntallStudenter() < fag.hentAntallStudenter():
                    fagetMedFlest = fag
            print(fagetMedFlest.hentFagNavn(), "har flest studenter:", fagetMedFlest.hentAntallStudenter())
        else:
            print("Ingen fag tilgjengelig")

    def leggTilStudent(self, navn):
        studenten = self.finnStudent(navn)
        if studenten == None:
            studenten = Student(navn)
            self._studentListe.append(studenten)

    def leggTilFag(self, navn):
        faget = self.finnFag(navn)
        if faget == None:
            faget = Fag(navn)
            self._fagListe.append(faget)


    def leggTilStudentIFag(self):
        studenten = self.finnStudent(input("Skriv studentnavn"))
        if studenten == None:
            print("Finner ikke student, registrer studenten først for å legge til fag")
            return

        faget = self.finnFag(input("Skriv fagnavn"))
        if faget == None:
            print("Finner ikke fag, registrer faget først for å legge til student")
            return

        if studenten.tarFag(faget):
            print("Studenten tar allerede faget")
        else:
            studenten.leggTilFag(faget)
            faget.leggTilStudent(studenten)

    def ordelokke(self):
        svar = ""
        while svar != "q":

            svar = input(self.menyOversikt())


    def menyOversikt(self):
        return\
        """
        Meny:

        1: Legg til ny student
        2: Legg til nytt fag
        3: Legg til student i fag
        4: Skriv ut studenter ved fag
        5: Skriv ut fag ved student
        6: Finn student med flest fag
        7: Finn fag med flest studenter
        q: Avslutt program

        """
