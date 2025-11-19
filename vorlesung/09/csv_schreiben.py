datei = open("einmaleins.csv","w")

for i in range(1,11):
    for j in range(1,11):
        datei.write(f"{i*j:5d};")
    datei.write("\n")

datei.close()