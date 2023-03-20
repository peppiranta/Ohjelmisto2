class Auto:

    #KONSTRUKTORI
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    #KIIHDYTYS METODI
    def kiihdytys(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0


#PÄÄOHJELMA
uusi_auto = Auto("ABC-123", 142)

uusi_auto.kiihdytys(30)
uusi_auto.kiihdytys(70)
uusi_auto.kiihdytys(50)

print(f"Nopeus on: {uusi_auto.nopeus}")

uusi_auto.kiihdytys(-200)
print(f"Nopeus on: {uusi_auto.nopeus}")