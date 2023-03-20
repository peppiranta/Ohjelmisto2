#ALLA OLEVA def = konstruktori
class Koira:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi



koira = Koira("Rekku", 2022)
Lissu = Koira("Lissu", 2011)


print (f"{koira.nimi:s} on syntynyt vuonna {koira.syntymävuosi:d}." )
print (f"{Lissu.nimi:s} on syntynyt vuonna {Lissu.syntymävuosi:d}." )