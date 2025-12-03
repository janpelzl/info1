class Tier:
    def __init__(self, eineTierart="", einName="", einGeburtsjahr=0, eineFarbe=""):
        self.tierart = eineTierart
        self.jahr = einGeburtsjahr
        self.name = einName
        self.farbe = eineFarbe
    def ausgeben(self):
        print(f"Das Tier {self.name} ist ein {self.tierart} und ist {self.farbe}")


einTier = Tier("Hund","Hasso", 2012, "schwarz")
nocheinTier = Tier("Fisch","Wanda", 2022, "gelb")

#print(f"Das Tier {einTier.name} ist ein {einTier.tierart} und ist {einTier.farbe}")
#print(f"Das Tier {nocheinTier.name} ist ein {nocheinTier.tierart} und ist {nocheinTier.farbe}")
einTier.ausgeben()
nocheinTier.ausgeben()
