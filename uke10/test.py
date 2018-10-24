from fag import Fag
from student import Student

def main():
    in1000 = Fag("IN1000")
    mat1100 = Fag("MAT1100")
    thomas = Student("Thomas")
    karan = Student("Karan")
    aurora = Student("Aurora")
# legger studenter i fag
    in1000.leggTilStudent(thomas)
    in1000.leggTilStudent(aurora)
    mat1100.leggTilStudent(karan)
    mat1100.leggTilStudent(aurora)

    in1000.skrivStudenterVedFag() #IN1000 [thomas]
    mat1100.skrivStudenterVedFag() #mat1100 [karan, aurora]

# legger fag i studenter
    thomas.leggTilFag(in1000)
    karan.leggTilFag(mat1100)
    aurora.leggTilFag(mat1100)
    aurora.leggTilFag(in1000)

    thomas.skrivFagPaaStudent()
    karan.skrivFagPaaStudent()
    aurora.skrivFagPaaStudent()

main()
