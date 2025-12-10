class HSHL:
    def __init__(self, einStudiengang):
        self.studiengang = einStudiengang
        print(f"Objekt mit Studiengang {self.studiengang} erzeugt")

    def __del__(self):
        print(f"Objekt mit Studiengang {self.studiengang} gelöscht")

# Hauptprogramm
a = HSHL("BMT")
b = HSHL("UFC")

print(a,b)

