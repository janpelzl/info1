datei = open("staedte.txt", "r")
inhalt = datei.readlines()

for zeile in inhalt:
    print(zeile)