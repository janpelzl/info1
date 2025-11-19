def steuerzeichenEntfernen(liste):
    ergebnis = []
    for zeile in liste:
        zeileGefiltert = zeile.replace("\n"," ")
        ergebnis.append(zeileGefiltert)
    return ergebnis

datei = open("staedte.txt", "r")
inhalt = datei.readlines()
print(inhalt)

inhaltGefiltert = steuerzeichenEntfernen(inhalt)
print(inhaltGefiltert)

del(inhaltGefiltert[0])
del(inhaltGefiltert[0])
print(inhaltGefiltert)
print(inhaltGefiltert[0].split())
