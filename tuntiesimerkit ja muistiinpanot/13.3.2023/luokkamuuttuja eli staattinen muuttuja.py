class Koira:
    #ALLA LUOKKAMUUTTUJA
    tehty = 0

    def __init__(self, nimi, syntymävuosi, haukahdus = "VUH-VUH"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        Koira.tehty = Koira.tehty + 1

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return


koira = Koira("Rekku", 2022)
Lissu = Koira("Lissu", 2011, "vuh-vuh-vuh")
#ALLA PRINTATAAN LUOKKAMUUTTUJA
print(f"Koiria tehty: {Koira.tehty}")


koira.hauku(2)
Lissu.hauku(4)