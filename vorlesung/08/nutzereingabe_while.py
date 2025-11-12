# Nutzer wird solange gefragt, bis eine gültige Zahl eingegeben wurde

abbruchbedingung = True;
while abbruchbedingung:
    eingabe = input("Bitte eine ganze Zahl eingeben: ")
    if eingabe.isdecimal():
        abbruchbedingung = False
        print("Vielen Dank. Das Programm endet jetzt.")
    else:
        print("Das war keine ganze Zahl.")
