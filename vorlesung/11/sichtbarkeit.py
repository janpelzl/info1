class Patient:
    def __init__(self, einName, einGeburtsjahr, einGewicht, eineGroesse):
        self.__name = einName
        self.__geburtsjahr = einGeburtsjahr
        self.__gewicht = einGewicht
        self.__groesse = eineGroesse

    def ausgabe(self):
        print(f"{self.__name} ist {self.__geburtsjahr} geboren, wiegt {self.__gewicht}kg und ist {self.__groesse}m groß.")

    def aendereGewicht(self, neuesGewicht):
        if 0 <= neuesGewicht <= 500:
            self.__gewicht = neuesGewicht
        else:
            print("Bitte richtiges Gewicht angeben.")


# Hauptprogramm
patientA = Patient("Müller",1999, 120, 1.55)
patientA.ausgabe()

patientA.aendereGewicht(100)
#patientA.gewicht = 110
patientA.ausgabe()
