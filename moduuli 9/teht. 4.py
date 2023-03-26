from prettytable import PrettyTable
import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nykyinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        matka = self.nykyinen_nopeus * tuntimaara
        self.kuljettu_matka += matka

auto = Auto("ABC-123", 142)
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print("Nykyinen nopeus:", auto.nykyinen_nopeus)
auto.kulje(1.5)
print("Kuljettu matka:", auto.kuljettu_matka, "km")
