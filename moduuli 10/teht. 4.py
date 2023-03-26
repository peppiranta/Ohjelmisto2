import random

class Auto:
    def __init__(self, nimi, nopeus):
        self.nimi = nimi
        self.nopeus = nopeus
        self.matka = 0

    def kulje(self, tunti):
        self.matka += self.nopeus * tunti

    def nopeuden_muutos(self):
        return random.randint(-10, 20)

    def __str__(self):
        return f"{self.nimi}: {self.matka:.1f} km"

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.nopeus += auto.nopeuden_muutos()
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Nimi':<10} Matka")
        for auto in self.autot:
            print(f"{auto.nimi:<10} {auto.matka:.1f} km")
        print()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

# pääohjelma
autot = [Auto("Auto1", 80), Auto("Auto2", 90), Auto("Auto3", 100),
         Auto("Auto4", 70), Auto("Auto5", 60), Auto("Auto6", 110),
         Auto("Auto7", 75), Auto("Auto8", 85), Auto("Auto9", 95),
         Auto("Auto10", 65)]

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()
print("Kilpailu on ohi!")
