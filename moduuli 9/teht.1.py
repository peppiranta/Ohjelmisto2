class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

uusi_auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus: {uusi_auto.rekisteritunnus},")
print(f"huippunopeus: {uusi_auto.huippunopeus},")
print(f"tämänhetkinen nopeus: {uusi_auto.tämänhetkinen_nopeus} ja")
print(f"kulkema matka: {uusi_auto.kuljettu_matka}")

