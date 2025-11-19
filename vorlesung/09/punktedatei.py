import turtle

def steuerzeichenEntfernen(liste):
    ergebnis = []
    for zeile in liste:
        zeileGefiltert = zeile.replace("\n"," ")
        ergebnis.append(zeileGefiltert)
    return ergebnis

datei = open("punkte.dat","r")
inhalt = datei.readlines()
inhalt2 = steuerzeichenEntfernen(inhalt)

print(inhalt)
print(inhalt2)

turtle.reset()

for element in inhalt2:
    x, y = element.split(",")
    x = int(x)
    y = int(y)
    turtle.goto(x,y)

turtle.exitonclick()