class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, tunti):
        self.matkamittari += self.huippunopeus * tunti

    def tulosta_tiedot(self):
        print(
            f'Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus}, Matkamittari: {self.matkamittari:.2f} km')


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Akkukapasiteetti: {self.akkukapasiteetti:.2f} kWh')


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Bensatankin koko: {self.bensatankin_koko:.2f} l')


# pääohjelma
sahkoauto = Sähköauto('ABC-15', 180, 52.5)
polttomoottoriauto = Polttomoottoriauto('ACD-123', 165, 32.3)

sahkoauto.aja(3)
polttomoottoriauto.aja(3)

print('Sähköauton tiedot:')
sahkoauto.tulosta_tiedot()
print('\nPolttomoottoriauton tiedot:')
polttomoottoriauto.tulosta_tiedot()
