class Haus:
    Besitzer = str
    Farbe = str
    Adresse = str
    Baujahr = int
    Wohnflaeche = float
    Zimmer = float
    Preis = float
    Grunstueckgroeße = int
    Badezimmer = int
    Heizart = str


    def Grundbucheintrag_ändern(self, person):
        self.Besitzer = person

    def Anbauen(self, neueWohnfläche):
        if (self.Wohnfläche < neueWohnfläche):
            self.Wohnfläche = neueWohnfläche

        else:
            print("Das Haus sollte nach dem Anbau größer sein")

    def attribute_ausgeben(self):
        print("Besitzer: ", self.Besitzer)

        print("Baujahr: ", self.Baujahr)
        print("Wohnfläche {} qm² ".format(self.Wohnfläche))
        print("Zimmeranzahl: ", self.Anzahl_Zimmer)
        print("Farbe: ", self.Farbe)
