email = input("Gib Deine HSHL-Email Adresse an: ")
# prüfe, ob email eine gültige HSHL-Email ist
print(email.endswith("@hshl.de"))
print(email.find("@"))
print(email.split("@"))
