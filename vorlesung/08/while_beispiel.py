# Beispiel für eine Schleife, die vom Nutzer durch Eingabe des Wortes
# "Ende" beendet wird
weitermachen = True;
while weitermachen:
    eingabe = input("Bitte Ende eingeben für beenden: ")
    if(eingabe == "Ende"):
        weitermachen = False
