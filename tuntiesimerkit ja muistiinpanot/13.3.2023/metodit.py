class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus = "VUH-VUH"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return


koira = Koira("Rekku", 2022)
Lissu = Koira("Lissu", 2011, "vuh-vuh-vuh")

koira.hauku(2)
Lissu.hauku(4)