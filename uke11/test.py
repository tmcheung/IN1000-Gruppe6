from fag import Fag
from student import Student
from studentsystem import Studentsystem

def main():
    system = Studentsystem()

    filnavn = "emnestudenter.txt"
    system.innlesing(filnavn)
    
    system.ordelokke()



main()
