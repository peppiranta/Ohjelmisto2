class Hissi:
    def __init__(self, alin_kerros, ylimpia_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylimpia_kerros = ylimpia_kerros

    def kerros_ylos(self):
        if self.kerros < self.ylimpia_kerros:
            self.kerros += 1
        self.ilmoita_kerros()

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        self.ilmoita_kerros()

    def siirry_kerrokseen(self, kerros):
        while self.kerros != kerros:
            if self.kerros < kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()

    def ilmoita_kerros(self):
        print(f"Hissi on kerroksessa {self.kerros}")


# Pääohjelma
hissi = Hissi(1, 10)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)
