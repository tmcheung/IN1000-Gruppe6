from hund import Hund, Kennel

def main():
    h1 = Hund(False, "Kari", 10)
    h2 = h1
    h3 = Hund(False, "Kari", 10) #"samme" som h1

    k1 = Kennel(3, 3)
    naboListe = k1.finnNabo(0, 0)
    print("Hund:", k1._hundeListe[0][0],"\nAntall naboer:", len(naboListe))
    print("Naboer: ")
    for nabo in naboListe:
        print(nabo)

main()
