def median(a, b ,c):
    liste = [a, b, c]
    minimum = min(liste)
    maks = max(liste)


    for tall in liste:
        if tall != max and tall != min:
            return tall
    # løsning 2:
    # if a < b < c or c < b < a:
    #     return b
    #
    # if b < a < c or c < a < b:
    #     return a
    #
    # return c

def oppgave51(liste):
    nyListe = []

    for x in liste:
        nyListe.append(x)
        nyListe.append(0)

    #løsning 2:
    # nyListe = [0]*len(liste)*2
    # nyListe[x] = liste[x]
    #
    # for x in range(1, len(liste)):
    #     nyListe[x+1] = liste[x]

    return nyListe
